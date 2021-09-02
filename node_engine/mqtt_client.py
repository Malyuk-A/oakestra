import os
import uuid
from flask_mqtt import Mqtt
import json
import re
import time

from cpu_mem import get_cpu_memory, get_memory
from dockerclient import start_container, stop_container
from mirageosclient import run_unikernel_mirageos
from coordinates import get_coordinates


mqtt = None
app = None


def mqtt_init(flask_app, mqtt_port=1883, my_id=None):
    global mqtt
    global app
    global req

    app = flask_app

    app.config['MQTT_BROKER_URL'] = os.environ.get('CLUSTER_MANAGER_IP')
    app.config['MQTT_BROKER_PORT'] = int(mqtt_port)
    app.config['MQTT_REFRESH_TIME'] = 3.0  # refresh time in seconds
    mqtt = Mqtt(app)
    app.logger.info('initialized mqtt')
    mqtt.subscribe('nodes/' + my_id + '/control/+')
    mqtt.subscribe('nodes/' + my_id + '/ack')

    @mqtt.on_message()
    def handle_mqtt_message(client, userdata, message):
        data = dict(
            topic=message.topic,
            payload=json.loads(message.payload.decode())
        )
        app.logger.info(data)

        topic = data.get('topic')
        # if topic starts with nodes and ends with controls
        re_nodes_topic_control_deploy = re.search("^nodes/" + my_id + "/control/deploy$", topic)
        re_nodes_topic_control_delete = re.search("^nodes/" + my_id + "/control/delete$", topic)
        re_nodes_topic_ack = re.search("^nodes/" + my_id + "/ack$", topic)
        if re_nodes_topic_ack is not None:
            payload = data.get('payload')
            req = payload.get('request_time')
            resp = time.time()
            latency = (resp - req) * 1000 # in ms
            app.logger.info('CO - Worker latency: {}'.format(latency))
        else:
            payload = data.get('payload')
            image_technology = payload.get('image_runtime')
            image_url = payload.get('image')
            job_name = payload.get('job_name')
            port = payload.get('port')

        if re_nodes_topic_control_deploy is not None:
            app.logger.info("MQTT - Received .../control/deploy command")
            if image_technology == 'docker':
                start_container(image=image_url, name=job_name, port=port)
            if image_technology == 'mirage':
                commands = payload.get('commands')
                run_unikernel_mirageos(image_url, job_name, job_name, commands)
        elif re_nodes_topic_control_delete is not None:
            app.logger.info('MQTT - Received .../control/delete command')
            if image_technology == 'docker':
                stop_container(job_name)


def publish_cpu_mem(my_id):
    app.logger.info('Publishing CPU+Memory usage... my ID: {0}'.format(my_id))
    cpu_used, free_cores, memory_used, free_memory_in_MB = get_cpu_memory()
    mem_value = get_memory()
    topic = 'nodes/' + my_id + '/information'
    lat, long = get_coordinates()
    mqtt.publish(topic, json.dumps({'cpu': cpu_used, 'free_cores': free_cores,
                                    'memory': memory_used, 'memory_free_in_MB': free_memory_in_MB,
                                    'lat': lat, 'long': long, 'request_time': time.time()}))

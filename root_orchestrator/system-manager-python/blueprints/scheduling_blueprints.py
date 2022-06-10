import logging
import traceback
import json
from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint, Api, abort
from services.instance_management import instance_scale_up_scheduled_handler
from sm_logging import get_csv_logger
csv_logger = get_csv_logger()

schedulingbp = Blueprint(
    'Scheduling', 'scheduling-completed', url_prefix='/api/result'
)

auth_schema = {
    "type": "object",
    "properties": {
        "job_id": {"type": "string"},
        "cluster_id": {"type": "string"},
    }
}


@schedulingbp.route('/deploy')
class SchedulingController(MethodView):

    @schedulingbp.arguments(schema=auth_schema, location="json", validate=False, unknown=True)
    def post(self, *args, **kwargs):
        data = request.get_json()
        logging.log(logging.INFO, data)
        job_id = data.get('job_id')
        cluster_id = data.get('cluster_id')
        instance_scale_up_scheduled_handler(job_id, cluster_id)
        csv_logger.SCHEDULED(json.dumps({"sid":job_id,"cluster":cluster_id}))
        return 'ok'

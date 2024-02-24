import threading

from api.main import handle_api
from mqtt.main import handle_mqtt
from utils.certificate_generator import handle_certificate


def main():
    handle_certificate()
    threading.Thread(target=handle_api).start()
    handle_mqtt()


if __name__ == "__main__":
    main()

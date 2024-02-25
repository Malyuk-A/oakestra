import threading

from api.main import handle_api
from mqtt.main import handle_mqtt
from utils.pki_management import handle_pki


def main():
    handle_pki()
    threading.Thread(target=handle_api).start()
    handle_mqtt()


if __name__ == "__main__":
    main()

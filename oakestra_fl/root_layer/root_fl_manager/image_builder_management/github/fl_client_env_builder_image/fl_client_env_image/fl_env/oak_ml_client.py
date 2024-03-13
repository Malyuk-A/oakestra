import logging

import flwr
from custom_client import Client as CustomClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OakMLClient(flwr.client.NumPyClient, CustomClient):

    def get_parameters(self, config=None):
        return self.get_model_parameters()

    def fit(self, parameters, config):
        self.set_model_parameters(parameters)
        number_of_training_examples = self.fit_model()
        return self.get_parameters(), number_of_training_examples, {}

    def evaluate(self, parameters, config):
        self.set_model_parameters(parameters)
        loss, accuracy, number_of_evaluation_examples = self.evaluate_model()
        return loss, number_of_evaluation_examples, {"accuracy": accuracy}


def _start_fl_client():
    try:
        # client = Client(args).to_client()
        # flwr.client.start_client(server_address="server:8080", client=OakMLClient)
        flwr.client.start_numpy_client(server_address="server:8080", client=OakMLClient())
    except Exception as e:
        logger.error("Error starting FL client: %s", e)
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    _start_fl_client()

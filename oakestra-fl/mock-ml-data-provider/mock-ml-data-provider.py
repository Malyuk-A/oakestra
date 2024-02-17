import random

import flwr_datasets

random.randint(1, 100)


def load_data(
    hugging_face_dataset: str = "cifar10",
    seed: int = None,
):
    partition_type = "train"

    if seed:
        random.seed(seed)

    total_partitions = random.randint(1, 10)
    federated_dataset = flwr_datasets.FederatedDataset(
        dataset=hugging_face_dataset, partitioners={partition_type: total_partitions}
    )
    selected_partition = random.randint(1, total_partitions)
    partition = federated_dataset.load_partition(selected_partition - 1, partition_type)

    return partition

def send_data_to_colocated_data_manager(dataset_partition):
    

def main():
    dataset_partition = load_data()


if __name__ == "__main__":
    main()

from pathlib import Path

import pytest
import torch

from src.datamodules.cifar_datamodule import CifarDataModule


import unittest

import requests
import json
import base64
from requests import Response


class TestCifar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("deployment.json") as f:
            cls.base_url = json.load(f)["base_url"]

        print(f"using base_url={cls.base_url}\n\n")

        cls.image_paths = ["cat.png", "ship.png", "automobile.png", "dog.png"]

        # convert image to base64

    def test_predict(self):
        for image_path in self.image_paths:
            print(f"testing: {image_path}")

            with open(image_path, "rb") as f:
                ext = image_path.split('.')[-1]
                prefix = f'data:image/{ext};base64,'
                base64_data = prefix + base64.b64encode(f.read()).decode('utf-8')

            payload = json.dumps({
            "data": [
                base64_data
            ]
            })

            headers = {
            'Content-Type': 'application/json'
            }

            response: Response = requests.request("POST", self.base_url, headers=headers, data=payload, timeout=15)

            print(f"response: {response.text}")

            data = response.json()['data'][0]

            predicted_label = data['label']

            print(f"predicted label: {predicted_label}")

            self.assertEqual(image_path.split(".")[0], predicted_label)

            print(f"done testing: {image_path}")

            print()


@pytest.mark.parametrize("batch_size", [32, 128])
def test_mnist_datamodule(batch_size):
    data_dir = "data/"

    dm = CifarDataModule(data_dir=data_dir, batch_size=batch_size)
    dm.prepare_data()

    assert not dm.data_train and not dm.data_val and not dm.data_test
    assert Path(data_dir, "CIFAR10").exists()
    assert Path(data_dir, "CIFAR10", "raw").exists()

    dm.setup()
    assert dm.data_train and dm.data_val and dm.data_test
    assert dm.train_dataloader() and dm.val_dataloader() and dm.test_dataloader()

    num_datapoints = len(dm.data_train) + len(dm.data_val) + len(dm.data_test)
    assert num_datapoints == 60_000

    batch = next(iter(dm.train_dataloader()))
    x, y = batch
    assert len(x) == batch_size
    assert len(y) == batch_size
    assert x.dtype == torch.float32
    assert y.dtype == torch.int64
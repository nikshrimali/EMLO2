from pathlib import Path

import pytest
import torch

# from src.datamodules.cifar_datamodule import CifarDataModule
import os

import unittest

import requests
import json
import base64
from requests import Response


class TestCifar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("test_serve/deployment.json") as f:
            cls.base_url = json.load(f)["base_url"]

        print(f"using base_url={cls.base_url}\n\n")

        cls.image_paths = [file for file in os.listdir('test_serve/images') if file.endswith('.png') or file.endswith('.jpg') ]
        print('cls.image_paths')

        # convert image to base64

    def test_predict(self):
        for image_path in self.image_paths:
            print(f"testing: {image_path}")


            with open(f'test_serve/images/{image_path}', 'rb') as f:
                response: Response  = requests.post(self.base_url, files={'data': f}, timeout=15)

            print(f"response: {response.text}")

            predicted_label = list(response.json().keys())[0]



            print(f"predicted label: {predicted_label}")

            self.assertEqual(image_path.split("/")[-1].split(".")[0], predicted_label)

            print(f"done testing: {image_path}")

            print()


# @pytest.mark.parametrize("batch_size", [32, 128])
# def test_mnist_datamodule(batch_size):
#     data_dir = "data/"

#     dm = CifarDataModule(data_dir=data_dir, batch_size=batch_size)
#     dm.prepare_data()

#     assert not dm.data_train and not dm.data_val and not dm.data_test
#     assert Path(data_dir, "CIFAR10").exists()
#     assert Path(data_dir, "CIFAR10", "raw").exists()

#     dm.setup()
#     assert dm.data_train and dm.data_val and dm.data_test
#     assert dm.train_dataloader() and dm.val_dataloader() and dm.test_dataloader()

#     num_datapoints = len(dm.data_train) + len(dm.data_val) + len(dm.data_test)
#     assert num_datapoints == 60_000

#     batch = next(iter(dm.train_dataloader()))
#     x, y = batch
#     assert len(x) == batch_size
#     assert len(y) == batch_size
#     assert x.dtype == torch.float32
#     assert y.dtype == torch.int64

if __name__ == '__main__':
    unittest.main()
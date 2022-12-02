from pathlib import Path

import pytest
import torch

# from src.datamodules.cifar_datamodule import CifarDataModule
import os, subprocess

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
    
    # @pytest.mark.parametrize("batch_size", [32, 128])
    def test_predict(self):
        # open(f'test_serve/images/{image_path}', 'rb') as f:
        for file in self.image_paths:
            # print(f"testing: {os.path.join(file)}")
            file_path = f'test_serve/images/{file}'
            print(f'test_serve/images/{file}')

            str = f"python3 serve/ts_scripts/torchserve_grpc_client.py infer cifar {file_path}"

            response =  subprocess.Popen(str, shell=True, stdout=subprocess.PIPE).stdout
            pred = json.loads(response.read().decode())
            print(pred)
            predicted_label = list(pred.items())[0][0]
            print(f"predicted label: {predicted_label}")
            self.assertEqual(file_path.split("/")[-1].split(".")[0], predicted_label)



if __name__ == '__main__':
    unittest.main()
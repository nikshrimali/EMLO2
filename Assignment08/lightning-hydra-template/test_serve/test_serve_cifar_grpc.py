import unittest

import requests
import json
import base64
from requests import Response
import os, subprocess
import warnings
warnings.filterwarnings("ignore")

class TestFargateGradio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("deployment.json") as f:
            cfg = json.load(f)
            
        cls.base_url = cfg["base_url"]
        cls.image_path = cfg["Image_path"]

        cls.file_list = os.listdir(cls.image_path)
        print(cls.file_list)


    def test_predict(self):
        for file in self.file_list:
            print(f"testing: {os.path.join(self.image_path, file)}")

            
            str = "python serve/ts_scripts/torchserve_grpc_client.py infer mnist " + os.path.join(self.image_path, file)
            response =  subprocess.Popen(str, shell=True, stdout=subprocess.PIPE).stdout
            pred = json.loads(response.read().decode())
            print(pred)
            print(list(pred.items())[0][0])
            print(file.split("_")[1].split(".")[0])
            self.assertEqual(list(pred.items())[0][0], file.split("_")[1].split(".")[0])
           


if __name__ == '__main__':
    unittest.main()
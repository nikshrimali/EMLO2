import unittest

import requests
import json
import base64
from requests import Response
import os

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

            
            with open(os.path.join(self.image_path, file), 'rb') as img:
                data = img.read()
                
            headers = {
            'Content-Type': 'application/json'
            }

            response: Response = requests.put(self.base_url, data=data, timeout=15)

            print(f"response: {response.text}")
            
            pred = response.json()
            print(list(pred.items())[0][0])
            print(file.split("_")[1].split(".")[0])
            self.assertEqual(list(pred.items())[0][0], file.split("_")[1].split(".")[0])
           


if __name__ == '__main__':
    unittest.main()
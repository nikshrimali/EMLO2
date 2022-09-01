from tabnanny import verbose
import hydra
import timm
from omegaconf import DictConfig
import urllib
import torch
from PIL import Image
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform
import json
import logging

logging.disable('INFO')

@hydra.main(config_path="config", config_name="config")
def predict(cfg: DictConfig):
    model_name = cfg.model
    image_path = cfg.image
    result = []
    model = timm.create_model(model_name, pretrained=True)
    model.eval()

    config = resolve_data_config({}, model=model)
    transform = create_transform(**config)
    url, filename = (image_path, image_path.rsplit('/', 1)[-1])
    # url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg")
    # try:
    urllib.request.urlretrieve(url, filename)
    img = Image.open(filename).convert('RGB')
    tensor = transform(img).unsqueeze(0) # transform and add batch dimension

    category = get_image_mappings()
    with torch.no_grad():
        out = model(tensor)
    probabilities = torch.nn.functional.softmax(out[0], dim=0)
    top_prob, top_catid = torch.topk(probabilities, 1)

    result = {
        "predicted": category[top_catid], 
        "confidence": top_prob.item()
    }
    # print("################### Reuslt here ##########################")
    # print(result)
    print(json.dumps(result))
    return json.dumps(result)
    # except:
    #     print("Please give proper image link")
    #     raise IOError("Please give proper image link")
    
    

def get_image_mappings():
    url, filename = ("https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt", "imagenet_classes.txt")
    urllib.request.urlretrieve(url, filename) 
    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]
    
    return categories

if __name__ == "__main__":
    predict()


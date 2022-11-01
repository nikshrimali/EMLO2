import json
import timm
import torch
import argparse

import urllib
from PIL import Image
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform

# Load pretrained model

def main():

    # parser = argparse.ArgumentParser(description="")

    # parser.add_argument("--model", dest="model", help="ss")
    # parser.add_argument("--image", dest="image", help="ss")

    model = timm.create_model('resnet18', pretrained=True)
    model.eval()


    # Preprocess

    config = resolve_data_config({}, model=model)
    transform = create_transform(**config)

    url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg")
    urllib.request.urlretrieve(url, filename)
    img = Image.open(filename).convert('RGB')
    tensor = transform(img).unsqueeze(0) # transform and add batch dimension

    # Model predictions

    with torch.no_grad():
        out = model(tensor)
    probabilities = torch.nn.functional.softmax(out[0], dim=0)


    # Top 5 classes predictions
    top1_prob_idx = torch.argmax(probabilities).item()
    top1_prob = torch.max(probabilities).item()

    # Get imagenet class mappings
    url, filename = ("https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt", "imagenet_classes.txt")
    urllib.request.urlretrieve(url, filename) 
    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]


    # Print top categories per image
    top1_class = categories[top1_prob_idx]
    out = {"predicted": top1_class, "confidence": top1_prob}
    # print(out)
    return json.dumps(out)

if __name__ == "__main__":
    main()
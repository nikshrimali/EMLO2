import torch
import json

import torchvision.transforms as T
import torch.nn.functional as F

from PIL import Image


device = "cuda" if torch.cuda.is_available() else "cpu"


def model_fn(model_dir):
    model = torch.jit.load(f"{model_dir}/model.scripted.pt")

    model.to(device).eval()
    
    return model

def input_fn(request_body, request_content_type):
    assert request_content_type == "application/json"
    data = json.loads(request_body)["inputs"]
#     # print(f'!!!###%%% {data}')
#     img = Image.open(data)
#     transforms = T.Compose([
#                     T.ToTensor(),
#                     T.Resize((224, 224)),
#                     T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
# ])
#     img_t = transforms(img)
#     img_t = {"inputs": img_t[None, ...].numpy().tolist()}

#     return img_t

    data = torch.tensor(data, dtype=torch.float32, device=device)
    return data


# inference
def predict_fn(input_object, model):
    with torch.no_grad():
        prediction = model(input_object)
    return prediction


# postprocess
def output_fn(predictions, content_type):
    assert content_type == "application/json"
    res = predictions.cpu().numpy().tolist()
    return json.dumps(res)

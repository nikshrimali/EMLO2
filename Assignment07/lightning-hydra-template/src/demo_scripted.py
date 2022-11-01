from typing import List, Tuple

import torch
import gradio as gr
import torchvision.transforms as T
import torch.nn.functional as F
from s3_util import S3download

def demo() -> Tuple[dict, dict]:
    """Demo function.
    Args:
        cfg (DictConfig): Configuration composed by Hydra.

    Returns:
        Tuple[dict, dict]: Dict with metrics and dict with all instantiated objects.
    """

    #assert cfg.ckpt_path

    print("Running Demo")

    print("Start downloading model")
    
    BUCKET_NAME = "emlo"
    model_name = "model.script.pt"
    destination_file = "/opt/src/model.script.pt"
    s3_connect = S3download(BUCKET_NAME)
    s3_connect.download_model(model_name, destination_file)
    
    print("Complete downloading model")
    
    model = torch.jit.load("./model.script.pt")

    print("Loaded Model")

    def recognize_digit(image):
        if image is None:
            return None
        image = T.ToTensor()(image).unsqueeze(0)
        #image = torch.tensor(image[None, None, ...], dtype=torch.float32)
        preds = model.forward_jit(image)
        preds = preds[0].tolist()
        label = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
        return {label[i]: preds[i] for i in range(10)}

    #im = gr.Image(shape=(32, 32))

    demo = gr.Interface(
        fn=recognize_digit,
        inputs="image",
        outputs=[gr.Label(num_top_classes=10)],
        live=True,
    )

    demo.launch(server_port=8080, share=True)

def main() -> None:
    demo()

if __name__ == "__main__":
    main()
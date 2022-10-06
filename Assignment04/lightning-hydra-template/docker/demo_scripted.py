#import pyrootutils

# root = pyrootutils.setup_root(
#     search_from=__file__,
#     indicator=[".git", "pyproject.toml"],
#     pythonpath=True,
#     dotenv=True,
# )

from typing import List, Tuple

import torch
#import hydra
import gradio as gr
#from omegaconf import DictConfig
import torchvision.transforms as T
import torch.nn.functional as F

#from src import utils

#log = utils.get_pylogger(__name__)

def demo() -> Tuple[dict, dict]:
    """Demo function.
    Args:
        cfg (DictConfig): Configuration composed by Hydra.

    Returns:
        Tuple[dict, dict]: Dict with metrics and dict with all instantiated objects.
    """

    #assert cfg.ckpt_path

    print("Running Demo")

    #log.info(f"Instantiating scripted model <{cfg.ckpt_path}>")
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
**Model: timm.create_model("vit_base_patch32_224", pretrained=True)**
- complete. Required small change in cifar_datamodule.py - transforms.RandomResizedCrop(224) to convert size from 32*32 to 224*224


**Dataset: CIFAR10**
- complete


**Epochs: >25 **
- Complete - changed setting to run 25 epochs

Train ViT Base using FSDP (4 GPU)

Train ViT Base using DDP (4 GPU x 2 Nodes)
Use the highest batch_size possible for both strategies
Store the best checkpoint of both to AWS S3
In your repository add a training log book folder and create a .md file for above experiments
Add Model Validation Metrics, Training Time, GPU memory usage, GPU Utilization (nvidia-smi dump) for both strategies
you can run the testing script after training the model to get the final model metrics
Add the maximum batch_size number you were able to achieve
Upload Tensorboard logs to Tensorboard.dev and add link to it
All the above MUST be in a github repository markdown file
Submit the link to the markdown file in the github repository

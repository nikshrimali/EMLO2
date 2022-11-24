**Model: timm.create_model("vit_base_patch32_224", pretrained=True)**
- complete. Required small change in cifar_datamodule.py - transforms.RandomResizedCrop(224) to convert size from 32X32 to 224X224


**Dataset: CIFAR10**
- complete


**Epochs: >25 **
- Complete - changed setting to run 25 epochs

**Train ViT Base using FSDP (4 GPU)**
- Could not get any machine with multiple GPU. Also could not get multiple spot machines for this experiment in last 2-3 days

**Train ViT Base using DDP (4 GPU x 2 Nodes)**
- Complete

**Use the highest batch_size possible for both strategies**
- Complete
- Experimented with batch sizes 128m 192, 256 and 512. 
- It failed for 512
- So, maximum batch size achieved is 256
- could not store all the experiments. I lost spot instances 2 times and log has data only for the final experiment

**Store the best checkpoint of both to AWS S3**
- Complete - location - s3://emlo/assignment06/

**In your repository add a training log book folder and create a .md file for above experiments**
location of the log folder - https://github.com/atulgupta01/EMLO/tree/main/Assignment06/lightning-hydra-template/logs

**Add Model Validation Metrics, Training Time, GPU memory usage, GPU Utilization (nvidia-smi dump) for both strategies**
- location of the log folder - https://github.com/atulgupta01/EMLO/tree/main/Assignment06/lightning-hydra-template/logs
- Location of the nvidia-smi screenshots 
  -   https://github.com/atulgupta01/EMLO/blob/main/Assignment06/DDP-MasterNode.jpg
  -   https://github.com/atulgupta01/EMLO/blob/main/Assignment06/DDP-WorkerNode.jpg

**you can run the testing script after training the model to get the final model metrics**
- Complete

**Add the maximum batch_size number you were able to achieve**
- Complete - tried multiple batche sizes and highest batch size achieved is 256
- could not store all the experiments. I lost spot instances 2 times and log has data only for the final experiment

**Upload Tensorboard logs to Tensorboard.dev and add link to it**
- Complete - https://tensorboard.dev/experiment/DILuXqGGT2eqoWSL3bKKEw/#scalars

<i>**Some Important Things for personal reference**</i>

MASTER_PORT=29500 MASTER_ADDR=172.31.13.222 WORLD_SIZE=2 NODE_RANK=0 python src/train.py trainer=ddp trainer.devices=1 trainer.num_nodes=2 logger=tensorboard trainer.default_root_dir=$(date + '%Y-%m-%d_%H_%M_%S') callbacks.model_checkpoint.dirpath=logs/train/runs

tensorboard dev upload --logdir ./logs/tensorboard --name "DDP Multinode with CIFAR" --description "Training results from EMLO Assignment06 DDP" --one_shot

aws s3 cp ./logs/* s3://emlo/assignment06/ddp/*

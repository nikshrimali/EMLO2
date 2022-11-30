## 08-Model Serving

This branch contains the code for serving the model

Steps Done
- Train the pretrained model on CIFAR10 dataset using Hydra template - Resnet18 (Timm)
    - ```python src/train.py trainer=gpu trainer.max_epochs=20```

- Create a mar file using scripted resnet18 model + Model Handler** + Index to name json file***
    - ```torch-model-archiver --model-name cifar_resnet --version 1.0 --serialized-file /mnt/d/EMLO2/logs/train/runs/2022-11-28_13-50-04/model.script.pt --handler /mnt/d/EMLO2/src/torch_handlers/cifar_handler.py --extra-files /mnt/d/EMLO2/src/torch_handlers/cifar_classes/index_to_name.json```

- Get and run the torchserve latest docker image using the below command
    - ```docker run -it --rm --net=host -v `pwd`:/opt/src pytorch/torchserve:latest bash```
    - ```cd /opt/src```

- Deploy your model using the below command
    - ```torchserve --start --model-store model_store --models cifar=cifar_resnet.mar```

- Download serve from Git and install GRPC binaries via pip
    - ```git clone https://github.com/pytorch/serve```
    - ```cd serve```
    - ```pip install -U grpcio protobuf grpcio-tools```
- Compile the binaries
    - ```python -m grpc_tools.protoc --proto_path=frontend/server/src/main/resources/proto/ --python_out=ts_scripts --grpc_python_out=ts_scripts frontend/server/src/main/resources/proto/inference.proto frontend/server/src/main/resources/proto/management.proto```

- Do the inferencing using the below command
    - ```python ts_scripts/torchserve_grpc_client.py infer mnist ../test_images/10003_ship.png```
### Stuff we learnt
- Torch Serve
- GRPC


### Some Useful links
 
 
**File that contains code for transformations and does the inference
***File that contains code for class index to class names mapping
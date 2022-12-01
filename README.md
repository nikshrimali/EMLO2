## 08-Model Serving

### Agenda

-  Deploy your model to TorchServe in an EC2 Instance/GitPod - :white_check_mark:
- You have to use scripted model for creating your .mar file - :white_check_mark:
- Write PyTest script (test_serve_cifar.py) for testing REST API Inference Test if the inference output for 10 Images from CIFAR10 - :white_check_mark:
    
- Links to an external site.
- Check if the classname is correct - :white_check_mark:
- testing gRPC API Inference - 
- testing captum model explanation
- Check if the Model Explanation Values Shape returned by Server is correct
- Also Save the Model Explanations Image 
- Do for any 1 Image from CIFAR10


- Create a folder test_serve - :white_check_mark:
- Put all your tests inside that  - :white_check_mark:
- Along with any files if needed - :white_check_mark:
- Run tests with pytest test_serve - :white_check_mark:
- This should run all your torchserve related test - :white_check_mark:

- The parameter to the test functions should be your TorchServe Server Public IP and Model Name (as per your registered mar name)

- APIs of TorchServe will not be accessible over internet because it binds to 127.0.0.1 so only 127.0.0.1 can call APIs, to fix it bind to 0.0.0.0, now you can use the public IP of the instance to call APIs https://pytorch.org/serve/configuration.html#configure-torchserve-listening-address-and-port 

Links to an external site. for inference API
You can use PyTest fixtures for command line arguments
https://docs.pytest.org/en/7.1.x/how-to/parametrize.html



Create TORCHSERVE.md
 file in your logbook

    Copy/Paste output of pytest test_serve to it
    Attach Model Explanation Image to it
    Add Inference metrics (curl output of metrics api)
    Upload Tensorboard Profiler to tensorboard.dev 

    Links to an external site. and add link of it (this might not work, so instead just upload screenshots of the profiling page)

Submit link to TORCHSERVE.md
Links to an external site. file from your Github Repository

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
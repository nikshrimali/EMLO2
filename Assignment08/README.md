
**1. Do it for your CIFAR trained model**
- **Complete** - used the scripted model from the assignment-4

**2. Deploy your model to TorchServe in an EC2 Instance/GitPod**
  - You have to use scripted model for creating your .mar file
  
  **Complete**
 
 **3. Write PyTest script (test_serve_cifar.py) for**
 
  **1. testing REST API Inference**
    - Test if the inference output for 10 Images from CIFAR10
    - Images can be taken from here: https://github.com/RubixML/CIFAR-10/tree/master/trainLinks to an external site.
    - Check if the classname is correct
 
  **Complete**
    - Script - https://github.com/atulgupta01/EMLO/blob/main/Assignment08/lightning-hydra-template/test_serve/test_serve_cifar.py
    - output of the script - https://github.com/atulgupta01/EMLO/blob/main/Assignment08/lightning-hydra-template/logs/rest_api_output.txt
    - used deployment.json for URL and Image Path
  
  **2. testing gRPC API Inference**
    - Same thing as above, just do with gRPC
  
    **Complete** 
      - Script - https://github.com/atulgupta01/EMLO/blob/main/Assignment08/lightning-hydra-template/test_serve/test_serve_cifar_grpc.py
      - output of the script - https://github.com/atulgupta01/EMLO/blob/main/Assignment08/lightning-hydra-template/logs/grpc_api_output.txt
      - used deployment.json for URL and Image Path
  
  **3. testing captum model explanation**
    - Check if the Model Explanation Values Shape returned by Server is correct
    - Also Save the Model Explanations Image
    - Do for any 1 Image from CIFAR10
    
    **Complete**
    - jupyter notebook - https://github.com/atulgupta01/EMLO/blob/main/Assignment08/lightning-hydra-template/notebooks/Test.ipynb
    - please refer to images - 
    ![alt text](https://github.com/atulgupta01/EMLO/blob/main/Assignment08/model_explanation-1.png)
    ![alt text](https://github.com/atulgupta01/EMLO/blob/main/Assignment08/model_explanation-2.png)
    
    *There is some issue with the shapes. I tried a workaround for that but not sure if that is correct*

**4. Take inspiration from https://github.com/The-School-of-AI/emlov2-session-5-satyajitghanaLinks to an external site. and  https://github.com/ashleve/lightning-hydra-template/blob/main/tests/test_mnist_datamodule.pyLinks to an external site.**
  - Create a folder test_serve
  - Put all your tests inside that
  - Along with any files if needed
  - Run tests with pytest test_serve
  - This should run all your torchserve related test
  
  **Complete** - https://github.com/atulgupta01/EMLO/blob/main/Assignment08/lightning-hydra-template/logs/total_output.txt

**5. The parameter to the test functions should be your TorchServe Server Public IP and Model Name (as per your registered mar name)**
- APIs of TorchServe will not be accessible over internet because it binds to 127.0.0.1 so only 127.0.0.1 can call APIs, to fix it bind to 0.0.0.0, now you can use the public IP of the instance to call APIs https://pytorch.org/serve/configuration.html#configure-torchserve-listening-address-and-portLinks to an external site. for inference API
- You can use PyTest fixtures for command line arguments
- https://docs.pytest.org/en/7.1.x/how-to/parametrize.htmlLinks to an external site.
**TBC**

**6. Create TORCHSERVE.mdLinks to an external site. file in your logbook**
  - Copy/Paste output of pytest test_serve to it
  - Attach Model Explanation Image to it
  - Add Inference metrics (curl output of metrics api)
  - Upload Tensorboard Profiler to tensorboard.devLinks to an external site. and add link of it (this might not work, so instead just upload screenshots of the profiling page)
  
  **Complete**
  
  - log file - https://github.com/atulgupta01/EMLO/tree/main/Assignment08/lightning-hydra-template/pytorch_profiler
  ![alt text](https://github.com/atulgupta01/EMLO/blob/main/Assignment08/tensorboard_profiler.jpg)
    
Submit link to TORCHSERVE.md file from your Github Repository

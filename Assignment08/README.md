
**1. Do it for your CIFAR trained model**
- Complete - used the scripted model from the assignment-4

**2. Deploy your model to TorchServe in an EC2 Instance/GitPod**
  -- You have to use scripted model for creating your .mar file
Write PyTest script (test_serve_cifar.py) for
testing REST API Inference
Test if the inference output for 10 Images from CIFAR10
Images can be taken from here: https://github.com/RubixML/CIFAR-10/tree/master/trainLinks to an external site.
Check if the classname is correct
testing gRPC API Inference
Same thing as above, just do with gRPC
testing captum model explanation
Check if the Model Explanation Values Shape returned by Server is correct
Also Save the Model Explanations Image
Do for any 1 Image from CIFAR10
Take inspiration from https://github.com/The-School-of-AI/emlov2-session-5-satyajitghanaLinks to an external site. and  https://github.com/ashleve/lightning-hydra-template/blob/main/tests/test_mnist_datamodule.pyLinks to an external site.
Create a folder test_serve
Put all your tests inside that
Along with any files if needed
Run tests with pytest test_serve
This should run all your torchserve related test
The parameter to the test functions should be your TorchServe Server Public IP and Model Name (as per your registered mar name)
APIs of TorchServe will not be accessible over internet because it binds to 127.0.0.1 so only 127.0.0.1 can call APIs, to fix it bind to 0.0.0.0, now you can use the public IP of the instance to call APIs https://pytorch.org/serve/configuration.html#configure-torchserve-listening-address-and-portLinks to an external site. for inference API
You can use PyTest fixtures for command line arguments
https://docs.pytest.org/en/7.1.x/how-to/parametrize.htmlLinks to an external site.
Create TORCHSERVE.mdLinks to an external site. file in your logbook
Copy/Paste output of pytest test_serve to it
Attach Model Explanation Image to it
Add Inference metrics (curl output of metrics api)
Upload Tensorboard Profiler to tensorboard.devLinks to an external site. and add link of it (this might not work, so instead just upload screenshots of the profiling page)
Submit link to TORCHSERVE.mdLinks to an external site. file from your Github Repository

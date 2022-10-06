**Rquired files are in folder ./lightning-hydra-template/docker**
1. demo_scripted.py (to run inside the docker)
2. Dockerfile - creates the docker
3. model.script.pt - it is also copied in docker to load the model.

**Command to run the docker**

docker run -t -p 8080:8080 assignment04:latest

**Size of the image is 1.11 GB**

![image](https://user-images.githubusercontent.com/13270810/194217945-02fca16e-677e-4bd1-8a23-e160fa6a62b6.png)

**Location of the docker hub**

https://hub.docker.com/repository/docker/samatul/assignment04

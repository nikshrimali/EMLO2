Following are two docker image URI

public.ecr.aws/i3r4j2e5/emlo-test - (does not get the torch scripted model from S3 but copies at the time of creation of docker)

public.ecr.aws/i3r4j2e5/emlo_s3 - (Pulls the torch scripted model from S3)
The has also been pushed to the docker hub

https://hub.docker.com/repository/docker/samatul/assignment05

Tasks Completed

- Take the TRAINED MODEL deployment from previous assignment
  - CIFAR10 trained RESNET18 model
  - you have to use scripted model

**Complete**

Push the Model to S3 - **Complete** 

Modify your deploy script to download model from S3 - **Complete** Refer to demo_scripted.py

Push the Docker Image to ECR - **Complete**

Create a Fargate Spot Deployment on ECS - **Complete**

docker run -t -p 80:80 <image_name>:latest

**Image name will depend on creation of docker**

I created docker with name "assignment05" but pushed with different names

docker run -t -p 80:80 assignment05:latest

Submit your deployment ip address in Github Classroom which will test your deployment
try to keep your commits as less as possible <5 commits
before pushing test it
- could not try this.




# DiabetesPrediction_Docker
Created a docker image for c

An example Dockerfile for Diabetes Prediction ML model, + a few dependencies:

JDK 8
Nginx
git 1.7
Maven 3.1.1

# Prerequisites

I assume you have installed Docker and it is running.

See the Docker website for installation instructions.

# Build

Steps to build a Docker image:

1. Clone this repo

```python
git clone https://github.com/vishalsharbidar/DiabetesPrediction_Docker.git
```

2. Build the image
```python
cd ..
docker build -t diabetes_prediction .
```
This will take a few minutes.

3. Run the image's default command, which should start everything up. The -p option forwards the container's port 80 to port 8000 on the host. (Note that the host will actually be a guest if you are using boot2docker, so you may need to re-forward the port in VirtualBox.)

```python
cd ..
docker run -p 5000:5000 diabetes_prediction
```

4. Once everything has started up, you should be able to access the webapp via http://localhost:8000/ on your host machine.

open http://localhost:5000/



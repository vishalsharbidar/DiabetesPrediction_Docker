# DiabetesPrediction_Docker
Created a docker image for c

An example Dockerfile for Diabetes Prediction ML model, + a few dependencies:

1. Python 3.8
2. git 2.30.2


# Prerequisites

I assume you have installed Docker and it is running.

See the [Docker website](https://www.docker.com/get-started#h_installation) for installation instructions.

# Build

Steps to build a Docker image:

1. Clone this repo

```python
git clone https://github.com/vishalsharbidar/DiabetesPrediction_Docker.git
```

2. Build the image
```python
cd DiabetesPrediction_Docker-main
docker build -t diabetes_prediction .
```
This will take a few minutes.

3. Check for the docker image
```python
docker images
```

4. Run the image's default command, which should start everything up. The -p option forwards the container's port 5000 to port 5000 on the host.

```python
docker run -p 5000:5000 diabetes_prediction
```

4. Once everything has started up, you should be able to access the webapp via http://localhost:5000/apidocs on your host machine.

```python
open http://localhost:5000/apidocs
```

5. The web page will look as per image

![A Swagger API](/extra/swaggerAPI.png)

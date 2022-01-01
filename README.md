# dtc0002

This is a continuation of yesterday's challenge, which was to deploy Django to
K8s. I'm starting with a dockerized version of Django. Now I need to write the
Kubernetes resource files.

To run locally, copy `example.env` to `.env` and make any changes you deem
necessary. Next, run `docker-compose up`. You should have your very own Django
running on http://127.0.0.1:8000.

## Kubernetes prerequisites

In order to deploy to Kubernetes, I need to store my image in a Docker registry
somewhere. I chose [a Docker
Hub repo](https://hub.docker.com/repository/docker/textninja/hellodjango).

To build and push to Docker hub, I ran the following commands.

```console
$ docker login
$ docker build -t textninja/hellodjango .
$ docker push textninja/hellodjango
```

## Deploying to Kubernetes

To deploy to Kubernetes, follow the instructions in the [deployment](deployment) folder.

## Project notes

 - I need to create django locally
 - I then need to dockerize it and push to an image registry
 - I'll use kustomize to override the settings file

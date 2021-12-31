# dtc0002

This is a continuation of yesterday's challenge, which was to deploy Django to
K8s. I'm starting with a dockerized version of Django. Now I need to write the
Kubernetes resource files.

To run locally, modify `example.env` as needed and rename it to `.env`. Then run
`docker-compose up`.

To build and push to Docker hub, use the following (substituting "textninja" for
your own docker id):

```console
$ docker login
$ docker build -t textninja/hellodjango .
$ docker push textninja/hellodjango
```

To deploy to kubernetes (instructions forthcoming).

## Project notes

 - I need to create django locally
 - I then need to dockerize it and push to an image registry
 - I'll use kustomize to override the settings file

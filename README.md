# dtc0002

This is a continuation of yesterday's challenge, which is to deploy
Django to K8s.

To run locally, modify `example.env` as needed and rename it to `.env`. Then run
`docker-compose up`.

To deploy to kubernetes (instructions forthcoming).

## Project notes

 - I need to create django locally
 - I then need to dockerize it and push to an image registry
 - I'll use kustomize to override the settings file

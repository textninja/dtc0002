# Django App Deployment

Deployments can be performed via make:

```console
$ make deployment.dev
$ make deployment.test
$ make deployment.prod
```
A namespace called dtc0002-`env` will be created automatically.

The deployment will then fail, because the secret has to be created separately.

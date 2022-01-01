# Django App Deployment

Deployments can be performed via make:

```console
$ make deployment.dev
$ make deployment.test
$ make deployment.prod
```
A namespace called dtc0002-`env` will be created automatically. The deployment
will then fail, because the secret has to be created separately.

Below is an example of the secrets that need to be defined.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: postgres-creds
stringData:
  username: postgres
  password: postgres
---
apiVersion: v1
kind: Secret
metadata:
  name: django-secrets
stringData:
  secretkey: super-secret-django-key
```

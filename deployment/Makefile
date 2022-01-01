.PHONY: secret.dev clean k8s/dev.yml deployment.dev

clean:
	rm -rf venv k8s

venv:
	python3 -mvenv venv	
	( \
		source ./venv/bin/activate; \
		pip install kubernetes; \
	)

deployment.dev: k8s/dev.yml
	kubectl apply -f k8s/dev.yml

k8s/dev.yml: venv
	mkdir -p k8s
	( \
		source ./venv/bin/activate; \
		python ./_scripts/deploy-dev.py > k8s/dev.yml \
	)

secret.dev:
	kubeseal \
      --controller-name=my-release-sealed-secrets \
      --controller-namespace=dtc0002-dev \
      --format yaml

.phony: clean

clean:
	rm -rf venv

venv:
	python3 -mvenv venv	
	( \
		source ./venv/bin/activate; \
		pip install kubernetes; \
	)

deployment.dev: venv
	( \
		source ./venv/bin/activate; \
		python ./_scripts/deploy-dev.py \
	)


setup:
	python -m venv venv; \
	source venv/bin/activate; \
	python -m pip install pip-tools
	@echo "Setup complete; don't forget to run..."
	@echo "\tsource venv/bin/activate"
	@echo "Followed by..."
	@echo "\tmake deps"

deps:
	python -m piptools compile \
		--upgrade \
		--resolver=backtracking \
		--generate-hashes \
		--allow-unsafe \
		-o requirements.txt \
		pyproject.toml
	python -m piptools compile \
		--upgrade \
		--resolver=backtracking \
		--generate-hashes \
		--allow-unsafe \
		--extra test \
		-o test-requirements.txt \
		pyproject.toml
	python -m piptools sync requirements.txt test-requirements.txt

clean:
	rm -r venv || true
	rm -r *.egg-info || true
	rm -r **/*.egg-info || true
	rm -r .pytest_cache || true
	@echo "Cleaning complete; run..."
	@echo "\tdeactivate"
	@echo "to deactivate the virtual env"

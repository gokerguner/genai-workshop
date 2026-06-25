.PHONY: install run deploy teardown

install:
	pip install -r requirements.txt

run:
	uvicorn backend.main:app --reload --port 8080

deploy:
	bash deploy.sh

teardown:
	bash teardown.sh

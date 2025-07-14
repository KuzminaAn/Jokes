PYTHON ?= python3
APP ?= src
TESTS ?= tests

install-requirements:
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

ruff-check:
	${PYTHON} -m ruff check ${APP} ${TESTS}

flake8-check:
	${PYTHON} -m flake8 ${APP} ${TESTS}

lint: ruff-check flake8-check

test:
	${PYTHON} -m pytest ${TESTS}

run-app:
	uvicorn src.app.main:app --reload

build-db:
	docker buildx build -t jockes_db -f database/Dockerfile .

run-db:
	docker run --name jockes_db -p 5432:5432 -d jockes_db

run-dev-env: build-db run-db

stop-dev-env:
	docker stop jockes_db
	docker rm jockes_db

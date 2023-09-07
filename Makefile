docker: #run docker
	sudo docker-compose up --build -d

db: #запуск базы данных
	psql "host=127.0.0.1 port=5432 dbname=project  user=postgres"

app: #запуск приложения
	uvicorn src.app.main:app --reload --port 7000

test: #запуск тестов
	pytest tests/tests.py -sl -vv

isort: #запуск flake8-isort
	isort ./src
	isort ./tests

black: #запуск flake8-black
	black ./src
	black ./tests

flake8: #запуск flake8
	flake8

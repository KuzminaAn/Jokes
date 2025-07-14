# Jokes REST API Service

Этот проект представляет собой RESTful сервис для хранения и управления шутками, построенный на FastAPI с использованием SQLAlchemy для работы с PostgreSQL.

## Функциональность

Сервис предоставляет следующие эндпоинты:

`GET /joke/` - Получить список шуток конкретного пользователя

`GET /joke/{joke_id}` - Получить конкретную шутку по ID

`POST /joke/` - Создать новую шутку

`PUT /joke/{joke_id}` - Обновить существующую шутку

`DELETE /joke/{joke_id}` - Удалить шутку

`POST /joke/random` - Добавить случайную шутку (используется внешний API Chuck Norris)

## Запуск

1. Подготовка
```
make install-requirements
```
2. Запуск БД
```
make run-dev-env
```
3. Запуск приложения
```
make run-app
```

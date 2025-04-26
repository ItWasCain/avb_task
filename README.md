УКОРАЧИВАТЕЛЬ — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой.

API проекта:
- / — POST-запрос на создание новой короткой ссылки;
- /<shorten_url_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

## Технологии:
* Python
* FastAPI
* SQLAlchemy
* Pydantic

## Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ItWasCain/avb_task.git
```

```
cd avb_task/shortener
```

Запуск проекта:

```
docker compose up
```

## Документация:
Документация проекта доступна по ссылкам:
* [http://localhost:8000/docs](http://localhost:8000/docs)
* [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Автор

[Никита Песчанов](https://github.com/ItWasCain)
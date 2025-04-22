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
cd avb_task
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать .env в директории /shortener.
Пример файла:
```
DATABASE_URL=sqlite+aiosqlite:///./fastapi.dba
```

Применить миграции:
```
cd shortener
```

```
alembic upgrade head
```

Запустить Проект:
```
uvicorn app.main:app --reload
```

## Документация:
Документация проекта доступна по ссылкам:
* [127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* [127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Автор

[Никита Песчанов](https://github.com/ItWasCain)
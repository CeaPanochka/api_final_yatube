# Yatube API
## Описание

Проект разработки API для Yatube.
Технологии:
- django
- REST API

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке.

```sh
git clone https://github.com/CeaPanochka/api_final_yatube.git
cd api_final_yatube
```

Создать и активировать виртуальное окружение.

```sh
python -m venv venv
source venv/Scripts/activate
```

Установить зависимости.

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции.

```sh
python manage.py migrate
```

Запустить проект.

```sh
python manage.py runsrver
```

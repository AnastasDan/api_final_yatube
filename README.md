# Проект «API для Yatube»

Yatube — это платформа для блогов. Yatube дает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone <ваша ссылка на репозиторий>
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Где посмотреть примеры запросов к API:

После запуска проекта переходим по этой ссылке:

http://127.0.0.1:8000/redoc/

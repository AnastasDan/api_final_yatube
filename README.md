# Проект «API для Yatube»

Yatube — это платформа для блогов. Yatube дает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

## Стек технологий

Python, Django, Django Rest Framework

## Как запустить проект:

Клонируем себе репозиторий:

```
git clone <ваша ссылка на репозиторий>
```

Переходим в директорию:

```
cd api_final_yatube
```

Cоздаем и активируем виртуальное окружение:

* Если у вас Linux/MacOS:

    ```
    python3 -m venv venv
    ```

    ```
    source venv/bin/activate
    ```

* Если у вас Windows:

    ```
    python -m venv venv
    ```

    ```
    source venv/Scripts/activate
    ```

Устанавливаем зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Создаем файл .env и заполняем его. Список данных указан в файле env.example.

Выполняем миграции:

```
python manage.py migrate
```

Запускаем проект:

```
python manage.py runserver
```

## Где посмотреть примеры запросов к API:

После запуска проекта переходим по этой ссылке:

http://127.0.0.1:8000/redoc/

## Автор проекта

[Anastas Danielian](https://github.com/AnastasDan)
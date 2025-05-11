# API для Yatube.

## Описание:
Проект, предоставляет интерфейс для работы с постами, где пользователи могут подписываться на других пользователей, просматривать и комментировать их посты и управлять своим контентом.

### Основные функции:
- Получение списка постов.
- Управление контентом (создание, изменение, удаление постов).
- Просмотр комментариев к постам.
- Создание, изменение, удаление комментариев.
- Получение списка подписок пользователя.
- Подписка на других пользователей.

### Использованы следующие технологии:

- Python
- Django
- Django ORM
- Django REST Framework
- JWT-аутентификация

## Запуск проекта:

**Клонировать репозиторий и перейти в него в командной строке:**
```
git clone https://github.com/Dmitriy-Vasilkin/api_final_yatube.git
```
```
cd api_final_yatube
```

**Cоздать и активировать виртуальное окружение:**
```
python -m venv venv
```
```
source venv/Scripts/activate
```

**Установить зависимости из файла requirements.txt:**
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

**Выполнить миграции:**
```
python manage.py migrate
```

**Запустить проект:**
```
python manage.py runserver
```

## Доступные запросы:

Публикации:
```
POST, GET
http://127.0.0.1:8000/api/v1/posts/

GET, PUT, PATCH, DELETE
http://127.0.0.1:8000/api/v1/posts/{id}/

(Анонимные запросы POST, PUT, PATCH, DELETE запрешены)
```

Комментарии:
```
POST, GET
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

GET, PUT, PATCH, DELETE
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

(Анонимные запросы POST, PUT, PATCH, DELETE запрешены)
```

Список сообществ:
```
GET
http://127.0.0.1:8000/api/v1/groups/

GET
http://127.0.0.1:8000/api/v1/groups/{id}/
```

Подписки:
```
POST
http://127.0.0.1:8000/api/v1/follow/

GET
http://127.0.0.1:8000/api/v1/follow/

(Анонимные запросы запрешены)
```

JWT-токен:
```
POST
http://127.0.0.1:8000/api/v1/jwt/create/
http://127.0.0.1:8000/api/v1/jwt/refresh/
http://127.0.0.1:8000/api/v1/jwt/verify/
```

## Примеры запросов и ответов:

**Создать пост (доступно для авторизованного пользователя)**
```
POST http://127.0.0.1:8000/api/v1/posts/
Authorization: Bearer <JWT_токен>
```
Тело запроса:
```json
{
    "text": "some text"
}
```
Ответ:
```json
{
    "id": 1,
    "author": "username",
    "text": "some text",
    "pub_date": "2025-05-10T20:38:31.608545+03:00",
    "image": null,
    "group": null
}
```

**Получить список постов**
```
GET http://127.0.0.1:8000/api/v1/posts/
```
Ответ:
```json
[
    {
        "id": 2,
        "author": "user1",
        "text": "text",
        "pub_date": "2025-05-10T20:54:20.560477+03:00",
        "image": null,
        "group": null
    },
    {
        "id": 1,
        "author": "user2",
        "text": "some text",
        "pub_date": "2025-05-10T20:38:31.608545+03:00",
        "image": null,
        "group": null
    }
]
```
**Подписаться на автора (доступно для авторизованного пользователя)**
```
POST http://127.0.0.1:8000/api/v1/follow/
Authorization: Bearer <JWT_токен>
```
Тело запроса:
```json
{
    "following": "user_1"
}
```
Ответ:
```json
{
    "following": "user_1",
    "user": "user"
}
```

# Разработал Василькин Д.Н.
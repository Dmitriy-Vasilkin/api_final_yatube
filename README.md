# api_final
## Финальный проект спринта: API для Yatube

В проекте реализовано:
> 1. Создание, редактирование, удаление постов.
> 2. Создание, редактирование, удаление комментариев к постам.
> 3. Подписка на авторов постов.

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

**Обрабатываемые запросы**

После запуска проекта список поддерживаемых запросов доступен по адресу:
```
http://127.0.0.1:8000/redoc/
```
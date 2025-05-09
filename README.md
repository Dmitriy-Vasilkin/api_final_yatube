# api_final
## Финальный проект спринта: API для Yatube

**В проекте реализовано:**

    Создание, редактирование, удаление постов.

    Создание, редактирование, удаление комментариев к постам.

    Подписка на авторов постов.

## Запуск проекта:

**Клонировать репозиторий и перейти в него в командной строке:**
```
git clone https://github.com/Dmitriy-Vasilkin/api_final_yatube.git

cd api_final_yatube
```

**Cоздать и активировать виртуальное окружение:**
```
python -m venv env

source env/bin/activate
```

**Установить зависимости из файла requirements.txt:**
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Выполнить миграции:**
```
python3 manage.py migrate
```

**Запустить проект:**
```
python3 manage.py runserver
```
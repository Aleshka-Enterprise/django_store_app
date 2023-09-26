# django_store_app

## Окружение
- python 3.11

## Установка
```
pip install -r requirements.txt
```

## Запуск
### Произвести миграции
```
python manage.py migrate
```
### Загрузить фикстуры
```
python manage.py loaddata products/fixtures/categories.json
python manage.py loaddata products/fixtures/products.json
```
### Запуск сервера
```
python manage.py runserver
```
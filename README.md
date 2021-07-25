# feature_yandex
Фича - Отправка отчета о поездке на почту.

### Зависимости
Зависимости для проекта описаны в файле requirements.txt

Сборка проекта в docker-compose.yml

### Установка и запуск
```
docker-compose build
docker-compose up
```

### Тестирование
Команда для запуска unit тестов
```
docker-compose exec app python manage.py test
```
Команда для запуска статических тестов
```
flake8 . --exclude=venv
```

### Метрики
Grafana http://0.0.0.0:3000/

### Мониторинг тасков Celery
Flower http://0.0.0.0:5555

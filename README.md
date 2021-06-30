# feature_yandex
Фича - Отправка отчета о поездке на почту.

### Зависимости
Должно быть установлено: Redis, Python

Зависимости для проекта описаны в файле requirements.txt

### Установка
1)Склонировать репозиторий с приложением в домашнюю директорию
```
git clone https://github.com/Borutia/feature_yandex.git
```
2)Перейти в директорию с проектом 
```
cd feature_yandex
```
3)Создать базу данных для приложения и его тестирования 
```
sudo su -c "sh create_db.sh" postgres
```
4)Создать виртуальное окружение
```
python -m venv venv
```
5)Активировать виртуальное окружение
```
source ./venv/bin/activate
```
6)Установить зависимости для приложения
```
pip install -r requirements.txt
```
7)Применить миграции к базе данных PostgreSQL
```
python manage.py migrate
```

### Запуск приложения
Команда для запуска Rides
```
redis-server
```
Команда для запуска Celery
```
celery -A feature_yandex worker -l INFO
```
Команда для запуска приложения
```
python manage.py runserver
```
Команда для обработки задач по расписанию
```
celery -A feature_yandex beat
```
Команда для запуска фоновых задач
```
python manage.py run_tasks
```

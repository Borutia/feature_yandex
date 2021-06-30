from django.db import models


class Email(models.Model):
    user_id = models.PositiveIntegerField('id пользователя', unique=True)
    email = models.EmailField('email', null=True, unique=True)
    is_confirmed = models.BooleanField('Подтвержден', default=False)
    is_send = models.BooleanField('Отправлено', default=False)


class Report(models.Model):
    send_time = models.DateTimeField('Время отправки', null=True)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)


class OrderPeriod(models.Model):
    date_from = models.DateField('Дата с')
    date_to = models.DateField('Дата по')
    report = models.ForeignKey(Report, on_delete=models.CASCADE)


class Order(models.Model):
    order_id = models.PositiveIntegerField('id заказа', unique=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

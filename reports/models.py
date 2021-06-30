from django.db import models


class Email(models.Model):
    user_id = models.PositiveIntegerField('id пользователя', unique=True)
    email = models.EmailField('email', null=True, unique=True)
    is_confirmed = models.BooleanField('Подтвержден', default=False)


class Report(models.Model):
    date_from = models.DateField('Дата с', null=True)
    date_to = models.DateField('Дата по', null=True)
    send_time = models.DateTimeField('Время отправки', null=True)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)


class Order(models.Model):
    order_id = models.PositiveIntegerField('id заказа')
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

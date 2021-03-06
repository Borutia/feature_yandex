# Generated by Django 3.2.4 on 2021-06-30 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')
                 ),
                ('user_id', models.PositiveIntegerField(
                    unique=True, verbose_name='id пользователя')
                 ),
                ('email', models.EmailField(
                    max_length=254, null=True,
                    unique=True, verbose_name='email')
                 ),
                ('is_confirmed', models.BooleanField(
                    default=False, verbose_name='Подтвержден')
                 ),
                ('is_send', models.BooleanField(
                    default=False, verbose_name='Отправлено')
                 ),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')
                 ),
                ('send_time', models.DateTimeField(
                    null=True, verbose_name='Время отправки')
                 ),
                ('email', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='reports.email')
                 ),
            ],
        ),
        migrations.CreateModel(
            name='OrderPeriod',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')
                 ),
                ('date_from', models.DateField(verbose_name='Дата с')),
                ('date_to', models.DateField(verbose_name='Дата по')),
                ('report', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='reports.report')
                 ),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')
                 ),
                ('order_id', models.PositiveIntegerField(
                    unique=True, verbose_name='id заказа')
                 ),
                ('report', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='reports.report')
                 ),
            ],
        ),
    ]

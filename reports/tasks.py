from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import get_template

from .models import Email, Order, Report, OrderPeriod
from .utils import get_email_link, get_order_info, get_order_period_info
from .consts import EMAIL_SUBJECT, ORDER_SUBJECT, ORDER_SUBJECT_PERIOD


def send_email_link_task():
    """Отправка сообщения на почту для подтверждения email"""
    users = Email.objects.filter(is_confirmed=False).exclude(email=None)
    for user in users:
        message = get_template("reports/email_confirm.html").render(
            {
                'link': get_email_link(email=user.email, user_id=user.user_id)
            }
        )
        send_mail(
            EMAIL_SUBJECT,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=message
        )


def send_report_task():
    """Отправка отчетов по каждому заказу"""
    orders = Order.objects.filter(
        report__send_time=None, report__orderperiod=None
    )
    for order in orders:
        order_info = get_order_info(order.id)
        message = get_template("reports/order_report.html").render(
            {
                'orders_info': order_info['data'],
            }
        )
        send_mail(
            ORDER_SUBJECT.format(order.order_id),
            message,
            settings.EMAIL_HOST_USER,
            [order.report.email.email],
            html_message=message,
        )
        order.report.send_time = timezone.now()
        order.report.save()


def send_report_period_task():
    """Отправка отчетов за период"""
    orders = OrderPeriod.objects.filter(
        report__send_time=None, report__order=None
    )
    for order in orders:
        orders_info = get_order_period_info(
            order.date_from, order.date_to
        )
        message = get_template("reports/order_report.html").render(
            {
                'orders_info': orders_info['data'],
            }
        )
        send_mail(
            ORDER_SUBJECT_PERIOD.format(
                order.date_from,
                order.date_to,
            ),
            message,
            settings.EMAIL_HOST_USER,
            [order.report.email.email],
            html_message=message,
        )
        order.report.send_time = timezone.now()
        order.report.save()

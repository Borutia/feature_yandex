from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.exceptions import NotFound

from .models import Email
from .consts import EMAIL_URL_CONFIRM


def get_email_instance(user_id):
    """Получить инстанс email по user_id"""
    try:
        return Email.objects.get(user_id=user_id)
    except Email.DoesNotExist:
        raise NotFound(detail='Instance not found')


def get_email_link(
        email,
        user_id,
        protocol=settings.CURRENT_PROTOCOL,
        host=settings.CURRENT_HOST,
        url=EMAIL_URL_CONFIRM,
):
    """Формирование строки для подтвеждения email"""
    return '{protocol}://{host}/{url}?email={email}' \
           '&confirmation_code={confirmation_code}:'.format(
                protocol=protocol,
                host=host,
                url=url,
                email=email,
                confirmation_code=urlsafe_base64_encode(
                    force_bytes(user_id)
                ),
           )


def get_order_info(order_id):
    """Запрос информации по заказу"""
    # Mock request order_id
    response = {
        'data': [
            {
                'order_id': 1,
                'date': '2021-01-10',
                'time': '09:32:14',
                'address_from': 'Ленина 1',
                'address_to': 'Ленина 100',
                'cost': 1000,
                'rate': 'Эконом',
                'travel_time': 50,
            }
        ]
    }
    return response


def get_order_period_info(date_from, date_to):
    """Запрос информации о заказах за период"""
    # Mock request orders period
    response = {
        'data': [
            {
                'order_id': 1,
                'date': '2021-01-10',
                'time': '09:32:14',
                'address_from': 'Ленина 1',
                'address_to': 'Ленина 100',
                'cost': 1000,
                'rate': 'Эконом',
                'travel_time': 50,
            },
            {
                'order_id': 2,
                'date': '2021-01-10',
                'time': '09:32:14',
                'address_from': 'Ленина 1',
                'address_to': 'Ленина 100',
                'cost': 1000,
                'rate': 'Эконом',
                'travel_time': 50,
            }
        ]
    }
    return response

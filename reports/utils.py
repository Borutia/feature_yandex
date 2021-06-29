from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .consts import EMAIL_URL_CONFIRM


def get_email_link(
        email,
        user_id,
        protocol=settings.CURRENT_PROTOCOL,
        host=settings.CURRENT_HOST,
        url=EMAIL_URL_CONFIRM,
):
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

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template

from .models import Email
from .utils import get_email_link
from .consts import EMAIL_SUBJECT


def send_email_task():
    users = Email.objects.filter(is_confirmed=False).exclude(email=None)
    for user in users:
        message = get_template("reports/email_confirm.html").render(
            {
                'link': get_email_link(email=user.email, user_id=user.user_id)
            }
        )
        send_mail(
            EMAIL_SUBJECT, message, settings.EMAIL_HOST_USER, [user.email],
            html_message=message
        )

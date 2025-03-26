from django.core.mail import send_mail
import uuid
from django.conf import settings


def send_forgot_password_mail(email , token):
    token = str(uuid.uuid4())

    subject = 'You forgot password link'
    message = f'Hi , click on the link to reset your password http://localhost:8000/account/password_change/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
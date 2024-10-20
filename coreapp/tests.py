from django.test import TestCase

# Create your tests here.
from django.core.mail import send_mail
from django.conf import settings

def test_email():
    send_mail(
        'Test Email Subject',
        'This is a test email.',
        settings.DEFAULT_FROM_EMAIL,
        ['nicksonwekongo@gmail.com'],  # Change to a valid recipient
        fail_silently=False,
    )

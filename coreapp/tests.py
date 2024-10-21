from django.test import TestCase

# Create your tests here.
from django.core.mail import send_mail
from django.conf import settings



# Test the email settings and send functionality for any errors that may occur during development 
def test_email():
    send_mail(
        'Test Email Subject',
        'This is a test email.',
        settings.DEFAULT_FROM_EMAIL,
        ['nicksonwekongo@gmail.com'],  # Change to a valid recipient email address
        fail_silently=False,
    )


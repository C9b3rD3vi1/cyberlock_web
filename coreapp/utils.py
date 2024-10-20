from django.conf import settings
from django.core.mail import send_mail
from .models import ContactMessage

# Save email addresses to database and send them to the user, admin
def save_contact_message(name, email, subject, message):
    # Create an instance of the ContactMessage model
    contact_message = ContactMessage(
        name=name,
        email=email,
        subject=subject,
        message=message
    )

    # Save the message to the database
    contact_message.save()

    # Commenting out the email sending part until we have a valid email
    """
    company_email = 'yourcompany@example.com'
    email_subject = f"New Contact Message: {subject}"
    email_body = fYou have received a new message from {name} ({email}).
    """

    Subject: {subject}
    Message: {message}
    
    """

    send_mail(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [company_email],
        fail_silently=False,
    )
    """

    return contact_message

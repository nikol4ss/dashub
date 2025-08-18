from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string

from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(reset_password_token, **kwargs):
    """
    Signal receiver for password reset token creation.

    This function listens for the `reset_password_token_created` signal triggered
    by the django-rest-passwordreset package. When a new token is generated, it
    constructs a password reset URL and sends it to the user's email.

    Args:
        reset_password_token: Instance of the generated password reset token.
        **kwargs: Additional keyword arguments, including:
            - request: Optional HTTP request object, used to build absolute URLs.

    Functionality:
        - Constructs the password reset URL using the token.
        - Prepares the email context with the reset URL and current year.
        - Renders HTML email template (`password_reset.html`) and a plain text fallback.
        - Sends the email to the user's registered email address.
    """
    request = kwargs.get("request")

    reset_url = (
        f"{request.build_absolute_uri('/password_reset/confirm/')}?token={reset_password_token.key}"
        if request
        else f"http://localhost:8000/password_reset/confirm/?token={reset_password_token.key}"
    )

    context = {
        "reset_url": reset_url,
        "year": datetime.now().year,
    }

    subject = "Password Reset – Dashub"
    from_email = "noreply@dashub.app"
    to_email = [reset_password_token.user.email]

    html_content = render_to_string("password_reset.html", context)
    text_content = f"Use the following link to reset your password: {reset_url}"

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

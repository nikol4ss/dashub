from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django_rest_passwordreset.signals import reset_password_token_created

from datetime import datetime


@receiver(reset_password_token_created)
def password_reset_token_created(sender, reset_password_token, **kwargs):
    request = kwargs.get("request")

    context = {
        "reset_url": "",
        "year": datetime.now().year,
    }

    if request:
        context["reset_url"] = (
            f"{request.build_absolute_uri('/password_reset/confirm/')}?token={reset_password_token.key}"
        )
    else:
        context["reset_url"] = (
            f"http://localhost:8000/password_reset/confirm/?token={reset_password_token.key}"
        )

    subject = "Redefinição de senha – Dashub"
    from_email = "noreply@dashub.app"
    to_email = [reset_password_token.user.email]

    html_content = render_to_string("password_reset.html", context)
    text_content = f"Acesse o link para redefinir sua senha: {context['reset_url']}"

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


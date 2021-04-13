from django.template.loader import render_to_string
from django.template.defaultfilters import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings 

def send_mail_template(assunto, template_html, context, para_email, de_email=settings.DEFAULT_FROM_EMAIL, fail_silently=False):
    mensagem_html = render_to_string(template_html, context)
    mensagem_txt = strip_tags(template_html)

    #subject, body, from_email e to, são padrões da classe EmailLMultiAlternatives
    email = EmailMultiAlternatives(
        subject = assunto, body = mensagem_txt, from_email = de_email, to = para_email 
    )

    email.attach_alternative(mensagem_html, "text/html")
    email.send(fail_silently=fail_silently)
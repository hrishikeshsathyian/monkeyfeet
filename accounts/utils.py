from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings




def send_account_activation_email(request,user):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    mail_subject = 'Please activate your account'
    message = render_to_string('accounts/emails/send_account_activation_email.html',{
        'user': user,
        'domain': current_site,
        'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
        # above 4 are the variables that we will pass in our template to create a link that will verify the user clicking the link and send them to the activate functio



    })
    to_email = user.email
    mail = EmailMessage(mail_subject,message,from_email,to=[to_email])
    mail.send()


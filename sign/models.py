from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user

        html_content_register = render_to_string(
            'register_mail.html',
            {'link': settings.SITE_URL,}
        )

        msg = EmailMultiAlternatives(
            subject='Регистрация на портале',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email]
        )

        msg.attach_alternative(html_content_register, 'text/html')
        msg.send()
        return user


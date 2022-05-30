from cProfile import label

from unicodedata import name
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']


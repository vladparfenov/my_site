from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Documents
from .models import Comments
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class DocumentForm(forms.ModelForm):
    docfile = forms.FileField(label='Select a file')

    class Meta:
        model = Documents
        fields = ('docfile', 'text',)


class CommentForm(ModelForm):

    class Meta:
        model = Comments
        fields = ('text', )

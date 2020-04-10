from django import forms
from django.contrib.auth.models import User

from holders.models import Holder


class HolderCreateForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=16)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name', max_length=32)
    last_name = forms.CharField(label='Last Name', max_length=32)
    password_1 = forms.CharField(widget=forms.PasswordInput,
                                 label='Password', max_length=32)
    password_2 = forms.CharField(widget=forms.PasswordInput,
                                 label='Repeat Passwprd', max_length=32)

    class Meta:
        model = Holder
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name',
                  'telephone',
                  'password_1',
                  'password_2']

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('The username already exists')
        return self.cleaned_data['username']

    def clean_password_2(self):
        if self.cleaned_data['password_2'] != self.cleaned_data['password_1']:
            raise forms.ValidationError('The passwords dont match')
        return self.cleaned_data['password_2']

    def save(self, commit=True):
        user = User.objects.create(username=self.cleaned_data['username'],
                                   email=self.cleaned_data['email'],
                                   first_name=self.cleaned_data['first_name'],
                                   last_name=self.cleaned_data['last_name'],)
        user.set_password(self.cleaned_data['email'])
        user.save()

        self.instance.user = user
        self.instance.save()
        return self.instance
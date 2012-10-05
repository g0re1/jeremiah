# _*_ coding: utf-8 _*_
from django import forms
import re
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class FormularzRejestracji(forms.Form):
    username = forms.CharField(label="Login:",max_length=30)
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Hasło:",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtórz hasło:",widget=forms.PasswordInput())
	
    def clean_username(self):
	    username = self.cleaned_data['username']
	    if not re.search(r'^\w+$',username):
	       raise forms.ValidationError("Dopuszczalne są tylko cyfry, litery angielskie i _")
	    try:
	       User.objects.get(username=username)
	    except ObjectDoesNotExist:
	       return username
	    raise forms.ValidationError("Taki użytkownik już istnieje")

    def clean_email(self):
	email = self.cleaned_data['email']
	try:
	    User.objects.get(email=email)
	except ObjectDoesNotExist:
	    return email
	raise forms.ValidationError("Taki email już istnieje")

    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1==password2:
            return password2
        else:    
            raise forms.ValidationError("Hasła się różnią")

class FormularzLogowania(forms.Form):
    username = forms.CharField(label="Login:",max_length=30)
    password = forms.CharField(label="Hasło:",widget=forms.PasswordInput())
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
            return username
        except ObjectDoesNotExist:
            raise forms.ValidationError("Niepoprawny login")        
    def clean_password(self):
        if self.cleaned_data.has_key('username'):
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user = User.objects.get(username=username)
            if user.check_password(password):
                return password
            raise forms.ValidationError("Niepoprawne hasło")                
        raise forms.ValidationError("Niepoprawny login")


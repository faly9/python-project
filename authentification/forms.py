from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Userform(UserCreationForm):
    username = forms.CharField(required=True ,widget=forms.TextInput(attrs={
        'placeholder' : 'your user username',
        'class' : 'username'
        }
        ))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
        'placeholder' : 'your email here',
        'class' : 'email'
    }))
    password1 = forms.CharField(required=True ,label="Password", widget=forms.PasswordInput(attrs={
        'placeholder' : 'your password',
        'class' : 'password'
    }))
    password2 = forms.CharField(required=True,label="Confirm password" , widget=forms.PasswordInput(attrs={
        'placeholder' : 'your password',
        'class' : 'password'
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        
    def clean_email(self):
        email = self.cleaned_data.get('email' ,'').strip().lower()
        if email and not email.endswith("gmail.com"):
            raise forms.ValidationError("Donnez une email valid")
        elif User.objects.filter(email =  email).exists():
            raise forms.ValidationError("Cet email existe deja")
        else:
            return email
        
    def clean_username(self):
        username = self.cleaned_data.get('username').strip()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ce nom utilisateur existe deja")
        if len(username) < 3:
            raise forms.ValidationError("Trop courte")
        else:
            return username
        
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 5:
            raise forms.ValidationError("Mot de passe trop court")
        else:
            return password1
        
    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')
        if password1 == password2:
            return password2
        else:
            raise forms.ValidationError('Mot de passe incorrect')


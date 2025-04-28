from django.shortcuts import render
from .forms import Userform
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    form = Userform()
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a ete cree")
            print("faly randriantsoa")
            return redirect('connexion')
    return render(request, 'templates_auth/register.html' , { 'form' : form })


def connexion(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, "vous etes connecte")
            return redirect('afficher')
        elif username == "":
            errors['username'] = "Veuillez remplir le champ username"
        elif not password:
            errors['password'] = "veillez remplir le champ password"
        elif User.objects.filter(username=username).exists() and not User.objects.filter(password = password).exists():
            errors['password'] = "Mot de passe incorrect"
        else:
            messages.error(request, "erreur d'authentification")
    return render(request, 'templates_auth/login.html' , {'errors' : errors} )



@login_required
def deconnection(request):
    logout(request)
    messages.success(request , 'vous etes deconnecte')
    return redirect('connexion')

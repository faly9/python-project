from unicodedata import name
from django.urls import path
from authentification.views import connexion,register,deconnection

urlpatterns = [
    path('' , register , name='register'),
    path('login/' , connexion , name = 'connexion'),
    path('logout/' , deconnection , name='deconnexion')
]


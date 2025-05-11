from unicodedata import name
from django.urls import path
from authentification.views import connexion,register,deconnection

urlpatterns = [
<<<<<<< HEAD
    path('register/' , register , name='register'),
=======
    path('' , register , name='register'),
>>>>>>> faly
    path('login/' , connexion , name = 'connexion'),
    path('logout/' , deconnection , name='deconnexion')
]


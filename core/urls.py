from django.urls import path
from .views import index, contacto, equipo, login, productos, recuperacion_de_contrasena, registro 
    
urlpatterns = [
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto'),
    path('equipo/', equipo, name='equipo'),
    path('login/', login, name='login'),
    path('productos/', productos, name='productos'),
    path('recuperacion_de_contrasena/', recuperacion_de_contrasena, name='recuperacion_de_contrasena'),
    path('registro/', registro, name='registro'),
]
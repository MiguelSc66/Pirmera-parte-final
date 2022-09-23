from django.urls import path
from AppCoder import *
from AppCoder.views import entregables, estudiantes, inicio, profesores

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("estudiantes/", estudiantes, name="Estudiantes"),
    path("profesores/", profesores, name="Profesores"),
    path("entregables/", entregables, name="Entregables"),
    ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.lista_cursos, name='cursos'),
    path('curso/<int:curso_id>/inscribirse/', views.inscribirse, name='inscribirse'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('novedades/', views.novedades, name='novedades'),
    path('contacto/', views.contacto, name='contacto'),
]

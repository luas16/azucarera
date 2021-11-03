from django.urls import path

from core.homepage.views import *
app_name = 'home'

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('nosotros/', NosotrosView.as_view(), name='nosotros'),
    path('anuncios/', AnunciosView.as_view(), name='anuncios'),
    path('contactos/', ContactoView.as_view(), name='contactos'),

]
from django.urls import path
from . import views

app_name='gendata'
urlpatterns = [
    path('', views.index, name="index"),
    path('prompt/', views.prompt, name='prompt'),
    path('generate_rsa/', views.generate_rsa, name='generate_rsa')
]
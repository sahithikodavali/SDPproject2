from . import views
from django.urls import path


urlpatterns = [
    path('', views.send_emails, name='send_emails'),
    path('tinyurl/', views.tiny_url, name='TinyURL'),
]
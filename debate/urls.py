from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start_debate, name='start_debate'),
    path('chat/', views.chat, name='chat'),
    path('chat_api/', views.chat_api, name='chat_api'),
    path('result/', views.result, name='result'),
]

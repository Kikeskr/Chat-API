from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('chat/', views.chat_view, name='chat'),
    path('tokens/', views.token_balance, name='token_balance'),
]


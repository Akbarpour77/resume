from django.urls import path
from user_auth_app import views


app_name = 'user_auth_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout')
]
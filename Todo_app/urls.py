from django.urls import path
from Todo_app import views


app_name = 'Todo_app'

urlpatterns = [
    path('create/', views.add, name='create'),
    path('show/', views.show, name='show'),
]

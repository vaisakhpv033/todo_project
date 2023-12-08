from django.urls import path

from .import views
app_name = 'todoapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>', views.delete, name='delete'),
]
from django.urls import path
from app2 import views

#template tagging
#globl name to use in html
app_name = 'app2'

urlpatterns = [
    path(r'homepage/', views.index1, name='homepage'),
    path(r'register/', views.register, name='register'),
    path(r'login/', views.user_login, name='user_login'),
    
]
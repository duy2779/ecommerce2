from django.urls import path

from .views import register, sign_in

app_name = 'account'

urlpatterns = [
    path('register', register, name='register'),
    path('login', sign_in, name='login'),
]

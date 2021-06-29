from django.urls import path

from .views import register, sign_in, log_out

app_name = 'account'

urlpatterns = [
    path('register', register, name='register'),
    path('login', sign_in, name='login'),
    path('logout', log_out, name='logout'),
]

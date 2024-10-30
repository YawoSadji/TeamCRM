from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loggedIn/', views.loggedIn, name='loggedIn'),
    path('logout', views.logout_user, name='logout')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loggedIn/', views.loggedIn, name='loggedIn'),
    path('logout/', views.logout_user, name='logout'),
    path('addRecord/', views.addRecord, name='addRecord'),
    path('single_record/<int:record_id>', views.single_record, name='single_record'),
    path('delete_record/<int:record_id>', views.delete_record, name='delete_record'),
    path('update_record/<int:record_id>', views.update_record, name='update_record'),
]
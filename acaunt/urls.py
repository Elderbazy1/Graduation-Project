from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('edituser/',views.edit_user,name = 'edituser'),
    path('logout/',views.logout,name='logout'),
    path('singup/', views.singup, name='singup'),
    path('view_message/<int:user_id>/', views.view_message, name='view'),
    path('read/<int:massage_id>',views.make_reader,name= 'markread'),
    path('delet/<int:delet_id>',views.delet_massage,name= 'delet'),
    path('send_message/', views.send_message, name='send_message'),
    path('message_success/', views.message_success, name='message_success'),
]

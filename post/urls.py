from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adnew/', views.addnew, name='addnew'),
    path('userposts/', views.user_posts, name='user_posts'),
    path('delete/<int:postdelet>',views.deletpost,name ='deletpost'),
    path('deletecomment/<int:delete_comment>',views.delete_comment,name ='deletecomment'),
    path('deletereplay/<int:replay_id>',views.delete_replay,name ='deletereplay'),
    path('showpost/<int:show>',views.show_post,name='showpost'),
    path('addcomment/<int:addcomment>',views.add_comment,name='addcomment'),
    path('search/',views.search,name='search'),
    path('showcatogry/<int:catogery_id>',views.catogery, name = 'showcatogry'),
    path('editpost/<int:editpost_id>', views.edit_post, name= 'editpost'),

    path('post/<int:post_id>/<str:action>/', views.like_dislike_post, name='like_dislike_post'),
    path('showuser/<str:name>',views.show_user,name = 'showuser'),
    path('replaycomments/<int:comment_id>',views.reaplaycommnet , name = 'reaplaycommnet'),


    # rest api

    path('restapi/',views.show_api),
    path('showpk/<int:pk>',views.show_with_pk),
    path('showapiwithclass/',views.show_api_withclass.as_view()),
    path('showapiwithclasspk/<int:pk>',views.show_api_withclass_pk.as_view()),



]

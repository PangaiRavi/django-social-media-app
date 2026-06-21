from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('home/', views.home, name='home'),

    path('create_post/', views.create_post, name='create_post'),

    path('like/<int:id>/', views.like_post, name='like_post'),

    path('comment/<int:id>/', views.comment, name='comment'),

    path('delete_comment/<int:id>/', views.delete_comment, name='delete_comment'),

    path('profile/<int:id>/', views.profile, name='profile'),

    path('follow/<int:id>/', views.follow, name='follow'),

    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    path('search/', views.search_user, name='search_user'),

    path(
    'notifications/',
    views.notifications,
    name='notifications'
),
]
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('users/<str:username>/', views.user_detail, name='user_detail'),
    path('follow/<str:username>/', views.toggle_follow, name='toggle_follow'),
]
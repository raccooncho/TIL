from django.urls import path
from . import views



app_name = 'board_ad'

urlpatterns = [
    # Read
    path('', views.article_list, name='article_list'),
    path('<int:id>/', views.article_detail, name='article_detail'),
    # Create
    path('create/', views.article_create, name='article_create'),
    # Update
    path('<int:id>/edit/', views.article_edit, name='article_edit'),
    # Delete
    path('<int:id>/delete/', views.article_delete, name='article_delete'),

]

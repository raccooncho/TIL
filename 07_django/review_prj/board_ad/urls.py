from django.urls import path
from . import views



app_name = 'board_ad'

urlpatterns = [
    # Read
    path('', views.posting_list, name='posting_list'),
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),
    # Create
    path('create/', views.posting_create, name='posting_create'),
    # Update
    path('<int:posting_id>/update/', views.posting_update, name='posting_update'),
    # Delete
    path('<int:posting_id>/delete/', views.posting_delete, name='posting_delete'),

]

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:post_id>/update/', views.post_update, name='post_update'),
    path('<int:post_id>/comment/create/', views.comment_create, name='comment_create'),
    path('<int:post_id>/like/', views.toggle_like, name='toggle_like'),
    # /insta/tags/hihi
    path('tags/<str:tag_name>/', views.tag_posts_list, name='tag_posts_list'),
]
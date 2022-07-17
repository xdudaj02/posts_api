from django.urls import path
from posts import views

urlpatterns = [
    path('post/<int:post_id>', views.get_post),
    path('user/<int:user_id>/posts', views.get_user_posts),
    path('post/create', views.create_post),
    path('post/<int:post_id>/patch', views.patch_post),
    path('post/<int:post_id>/put', views.put_post),
    path('post/<int:post_id>/delete', views.delete_post),
]

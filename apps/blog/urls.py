from django.urls import path

from . import api_endpoints as views

app_name = 'blog'

urlpatterns = [
    path('post/list/', views.PostListAPIView.as_view(), name='post_list'),
    path('post/retrieve/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post_retrieve'),
    path('comment/create/', views.CommentCreateAPIView.as_view(), name='comment_create')
]

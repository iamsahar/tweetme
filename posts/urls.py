from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/comment/',
         views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/favourite/', views.favourite_post, name='favourite_post'),
    path('post/<int:pk>/bookmark/', views.bookmark_post, name='bookmark_post'),
    path('post/bookmarks/', views.bookmark_post_list, name='bookmark_post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('', views.PostListView.as_view(), name='home'),
    path('search/', views.search, name='search')
]

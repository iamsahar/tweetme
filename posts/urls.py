from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    re_path(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
    re_path(r'^post/(?P<pk>\d+)/favourite/$', views.favourite_post, name='favourite_post'),
    re_path(r'^post/(?P<pk>\d+)/bookmark/$', views.bookmark_post, name='bookmark_post'),
    re_path(r'^post/bookmarks/$', views.bookmark_post_list, name='bookmark_post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    re_path(r'^$', views.PostListView.as_view(), name='home'),
    re_path(r'^search/$', views.search, name='search')
]

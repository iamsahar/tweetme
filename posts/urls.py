from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/(?P<pk>\d+)/comment/$',
         views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>\d+)/favourite/$', views.favourite_post, name='favourite_post'),
    url(r'^post/(?P<pk>\d+)/bookmark/$', views.bookmark_post, name='bookmark_post'),
    url(r'^post/bookmarks/$', views.bookmark_post_list, name='bookmark_post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    url(r'^$', views.PostListView.as_view(), name='home'),
    url(r'^search/$', views.search, name='search')
]

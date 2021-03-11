from django.conf.urls import url
from . import views


app_name= 'accounts'


urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', views.activate_user_view, name="activate"),
    url(r'^profile/$', views.user_profile, name="profile"),
]

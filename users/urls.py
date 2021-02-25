from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.SignUpView.as_view(), name="register"),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^profile/$', views.profile, name="profile"),
]

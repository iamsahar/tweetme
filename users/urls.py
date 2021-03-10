from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^register/$', views.SignUpView.as_view(), name="register"),
    re_path(r'^login/$', views.LoginView.as_view(), name="login"),
    re_path(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    re_path(r'^profile/$', views.profile, name="profile"),
]

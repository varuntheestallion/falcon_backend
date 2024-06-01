"""
URL configuration for falcon_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from falconcup.views import (
    LoginView, SignUpView, add_team_member, proxy_add_team_member)


urlpatterns = [
    path("falconcup/", include("falconcup.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("teams/<int:team_id>/team-members/add", add_team_member, name="add_team_member"),
    path("register/<str:url_code>", proxy_add_team_member, name="proxy_add_team_member"),
]

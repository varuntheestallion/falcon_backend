from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("team_member_create/", views.team_member_create, name="team_member_create"),
]

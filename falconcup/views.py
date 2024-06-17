from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, SignUpForm, TeamMemberForm
from .models import Team, TeamMember


# Create your views here.

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("home")

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

def add_team_member(request, team_id):
    team = Team.objects.get(id=team_id)
    captains = TeamMember.objects.filter(team=team_id, player_level=TeamMember.CAPTAIN)
    if request.method == "POST":
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            team_member = form.save(commit=False)
            team_member.team = team
            team_member.player_level = TeamMember.TEAMMEMBER
            team_member.save()
            request.session["team_name"] = team.name
            return redirect("register_success")
    else:
        form = TeamMemberForm()
    return render(
        request, "add_team_member.html",
        {"form": form, "team_name": team.name, "captains": captains},
    )

def proxy_add_team_member(request, url_code):
    team = Team.objects.get(url_code=url_code)
    return add_team_member(request, team_id=team.id)

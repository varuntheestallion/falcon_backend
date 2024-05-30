from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginForm, RegisterForm, TeamMemberForm
from .models import Team, TeamMember


# Create your views here.

def index(request):
    return HttpResponse("Once you pop you don't stop.")

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

def team_member_create(request):
    if request.method == "POST":
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            # team_member = form.save(commit=False)
            # team_member.user = request.user
            # team_member.save()
            team_member = form.save()
            return redirect("home")
    else:
        form = TeamMemberForm()

    return render(
        request, 
        "team_member_create.html", 
        {"form": form}
    )

def add_team_member(request, team_id):
    team = Team.objects.get(id=team_id)
    captains = TeamMember.objects.filter(team=team_id, player_level=TeamMember.CAPTAIN)
    if request.method == "POST":
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            team_member = form.save(commit=False)
            team_member.team = team
            team_member.save()
            return redirect("home")
    else:
        form = TeamMemberForm()
    
    return render(
        request,
        "add_team_member.html",
        {"form": form, "team_name": team.name, "captains": captains}
    )

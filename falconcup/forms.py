from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import CustomUser, TeamMember


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'
        exclude = ("user", "team", "ghin_status", "player_level")

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    email = forms.CharField(label='Email')

from django import forms

from .models import TeamMember


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'
        exclude = ('team',)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Team, TeamMember


# Register your models here.

admin.site.register(TeamMember)
admin.site.register(Team)

class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    can_delete = True

class TeamAdmin(admin.ModelAdmin):
    model = Team
    can_delete = True
    inlines = [
        TeamMemberInline,
    ]

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    inlines = (TeamMemberInline,)

admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, TeamMember, Team


class TeamMemberAdmin(admin.ModelAdmin):
    model = TeamMember
    can_delete = True
    fields = [
        "player_level", "team", "name", "email", "phone",
        "gender", "corporate_title", "ghin_status", "ghin_number",
        "tshirt_size", "meal_preference", "cart_sitting_preference"
    ]

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    can_delete = True
    extra = 0
    show_change_link = True
    fields = [
        "player_level", "name", "email", "phone", "gender",
        "corporate_title", "ghin_status", "ghin_number",
        "tshirt_size", "meal_preference", "cart_sitting_preference"
    ]
    ordering = ["player_level"]

class TeamAdmin(admin.ModelAdmin):
    model = Team
    can_delete = True
    inlines = [TeamMemberInline]

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

admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

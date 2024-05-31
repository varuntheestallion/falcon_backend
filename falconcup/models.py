from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from .utils import create_random_code

URL_CODE_SIZE = getattr(settings, "REGISTER_URL_CODE_SIZE", 6)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=200)
    url_code = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def save_new_url_code(self, custom_code=None, size=URL_CODE_SIZE):
        if custom_code:
            new_code = custom_code
        else:
            new_code = create_random_code(size)

        if Team.objects.filter(url_code=new_code).exists():
            if custom_code:
                raise ValueError("Provided custom_code is being used by an existing team.")
            else:
                self.save_new_url_code(size=size)
        else:
            self.url_code = new_code
            self.save()
            print(f"Team's register form URL code is now '{self.url_code}'")

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)

    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = {
        MALE: "Male",
        FEMALE: "Female",
        OTHER: "Other",
    }
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)

    ACTIVE = "ACT"
    INACTIVE = "INA"
    DONT_HAVE_ONE = "DHO"
    GHIN_STATUS_CHOICES = {
        ACTIVE: "Active",
        INACTIVE: "Inactive",
        DONT_HAVE_ONE: "Don't have one",
    }
    ghin_status = models.CharField(
        "GHIN Status",
        max_length=3, 
        choices=GHIN_STATUS_CHOICES, 
        default=ACTIVE,
    )
    
    ghin_number = models.CharField("GHIN Number", max_length=200)

    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"
    TSHIRT_SIZE_CHOICES = { XS: "XS", S: "S", M: "M", L: "L", XL: "XL", XXL: "XXL" }
    tshirt_size = models.CharField("T-Shirt Size", max_length=3, choices=TSHIRT_SIZE_CHOICES)

    MEAT = "MEAT"
    VEGETARIAN = "VEG"
    MEAL_PREFERENCE_CHOICES = { MEAT: "Meat", VEGETARIAN: "Vegetarian" }
    meal_preference = models.CharField("Meal Preference", max_length=4, choices=MEAL_PREFERENCE_CHOICES)

    WALK = "WALK"
    CART = "CART"
    CART_SITTING_PREFERENCE_CHOICES = { WALK: "Walk", CART: "Cart" }
    cart_sitting_preference = models.CharField(
        "Cart Sitting Preference",
        max_length=4, 
        choices=CART_SITTING_PREFERENCE_CHOICES,
    )

    TEAMMEMBER = "TM"
    CAPTAIN = "CP"
    PLAYER_LEVEL_CHOICES = {
        TEAMMEMBER: "Team Member",
        CAPTAIN: "Captain",
    }
    player_level = models.CharField(
        "Player Level",
        max_length=2, 
        choices=PLAYER_LEVEL_CHOICES, 
        default=TEAMMEMBER,
    )

    def __str__(self):
        return f"{self.name}, Team: {self.team.name if self.team else None}"

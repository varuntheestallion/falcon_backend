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
    
    def save(self, *args, **kwargs):
        if not self.url_code:
            self.save_new_url_code()
        super().save(*args, **kwargs)

class TeamMember(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)

    SELECT_PLACEHOLDER = "— Please choose an option —"

    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = {
        "": SELECT_PLACEHOLDER,
        MALE: "Male",
        FEMALE: "Female",
        OTHER: "Other",
    }
    gender = models.CharField(
        max_length=200,
        choices=GENDER_CHOICES,
    )

    corporate_title = models.CharField(max_length=200, null=True, blank=True)

    ACTIVE = "ACT"
    INACTIVE = "INA"
    DONT_HAVE_ONE = "DHO"
    GHIN_STATUS_CHOICES = {
        "": SELECT_PLACEHOLDER,
        ACTIVE: "Active",
        INACTIVE: "Inactive",
        DONT_HAVE_ONE: "Don't have one",
    }
    ghin_status = models.CharField(
        "GHIN Status",
        max_length=3, 
        choices=GHIN_STATUS_CHOICES, 
        default=ACTIVE,
        null=True,
        blank=True
    )
    
    ghin_number = models.CharField("GHIN Number", max_length=200)

    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"
    TSHIRT_SIZE_CHOICES = {
        "": SELECT_PLACEHOLDER,
        XS: "XS", S: "S", M: "M",
        L: "L", XL: "XL", XXL: "XXL",
    }
    tshirt_size = models.CharField(
        "T-Shirt Size",
        max_length=3,
        choices=TSHIRT_SIZE_CHOICES,
        blank=True
    )

    MEAT = "MEAT"
    VEGETARIAN = "VEG"
    MEAL_PREFERENCE_CHOICES = {
        "": SELECT_PLACEHOLDER,
        MEAT: "Meat",
        VEGETARIAN: "Vegetarian",
    }
    meal_preference = models.CharField(
        "Meal Preference", 
        max_length=4,
        choices=MEAL_PREFERENCE_CHOICES,
        blank=True
    )

    WALK = "WALK"
    CART = "CART"
    CART_SITTING_PREFERENCE_CHOICES = {
        "": SELECT_PLACEHOLDER,
        WALK: "Walk",
        CART: "Cart",
    }
    cart_sitting_preference = models.CharField(
        "Cart Sitting Preference",
        max_length=4,
        choices=CART_SITTING_PREFERENCE_CHOICES,
        blank=True
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

    terms_accepted = models.BooleanField("Has Accepted Terms", default=False, blank=True)

    def __str__(self):
        return f"{self.name}, Team: {self.team.name if self.team else None}"

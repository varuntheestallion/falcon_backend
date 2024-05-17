from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=200)

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
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
        max_length=3, 
        choices=GHIN_STATUS_CHOICES, 
        default=ACTIVE,
    )
    
    ghin_number = models.CharField(max_length=200)

    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"
    TSHIRT_SIZE_CHOICES = { XS: "XS", S: "S", M: "M", L: "L", XL: "XL", XXL: "XXL" }
    tshirt_size = models.CharField(max_length=3, choices=TSHIRT_SIZE_CHOICES)

    MEAT = "MEAT"
    VEGETARIAN = "VEG"
    MEAL_PREFERENCE_CHOICES = { MEAT: "Meat", VEGETARIAN: "Vegetarian" }
    meal_preference = models.CharField(max_length=4, choices=MEAL_PREFERENCE_CHOICES)

    WALK = "WALK"
    CART = "CART"
    CART_SITTING_PREFERENCE_CHOICES = { WALK: "Walk", CART: "Cart" }
    cart_sitting_preference = models.CharField(
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
        max_length=2, 
        choices=PLAYER_LEVEL_CHOICES, 
        default=TEAMMEMBER,
    )

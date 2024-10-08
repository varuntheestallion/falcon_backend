# Generated by Django 5.0.6 on 2024-05-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("falconcup", "0002_teammember_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teammember",
            name="cart_sitting_preference",
            field=models.CharField(
                choices=[("WALK", "Walk"), ("CART", "Cart")],
                max_length=4,
                verbose_name="Cart Sitting Preference",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="ghin_number",
            field=models.CharField(max_length=200, verbose_name="GHIN Number"),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="ghin_status",
            field=models.CharField(
                choices=[
                    ("ACT", "Active"),
                    ("INA", "Inactive"),
                    ("DHO", "Don't have one"),
                ],
                default="ACT",
                max_length=3,
                verbose_name="GHIN Status",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="meal_preference",
            field=models.CharField(
                choices=[("MEAT", "Meat"), ("VEG", "Vegetarian")],
                max_length=4,
                verbose_name="Meal Preference",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="player_level",
            field=models.CharField(
                choices=[("TM", "Team Member"), ("CP", "Captain")],
                default="TM",
                max_length=2,
                verbose_name="Player Level",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="tshirt_size",
            field=models.CharField(
                choices=[
                    ("XS", "XS"),
                    ("S", "S"),
                    ("M", "M"),
                    ("L", "L"),
                    ("XL", "XL"),
                    ("XXL", "XXL"),
                ],
                max_length=3,
                verbose_name="T-Shirt Size",
            ),
        ),
    ]

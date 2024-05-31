# Generated by Django 5.0.6 on 2024-05-31 20:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("falconcup", "0003_alter_teammember_cart_sitting_preference_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="url_code",
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="falconcup.team",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

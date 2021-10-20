# Generated by Django 3.2.8 on 2021-10-11 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Logic", "0002_alter_blogtable_date_of_creation"),
    ]

    operations = [
        migrations.CreateModel(
            name="AbstractUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "reference",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Socials",
            fields=[
                (
                    "abstractuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="Logic.abstractuser",
                    ),
                ),
                (
                    "GitHub",
                    models.CharField(
                        blank=True,
                        default="No GitHub UserName specifiied",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "Instagram",
                    models.CharField(
                        blank=True,
                        default="No Instagram UserName specifiied",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "Twitter",
                    models.CharField(
                        blank=True,
                        default="No Twitter UserName specifiied",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "LinkedIn",
                    models.CharField(
                        blank=True,
                        default="No LinkedIn UserName specifiied",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "YouTube",
                    models.CharField(
                        blank=True,
                        default="No YouTube UserName specifiied",
                        max_length=100,
                        null=True,
                    ),
                ),
                ("Website", models.URLField()),
            ],
            bases=("Logic.abstractuser",),
        ),
    ]

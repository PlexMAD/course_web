# Generated by Django 4.2.2 on 2024-06-23 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("students", "0006_historicalworkexperiences_historicalstudents_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PageVisit",
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
                ("visited_at", models.DateTimeField(auto_now_add=True)),
                ("url", models.CharField(max_length=255)),
                ("http_method", models.CharField(max_length=10)),
                ("user_agent", models.CharField(max_length=255)),
                ("ip_address", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
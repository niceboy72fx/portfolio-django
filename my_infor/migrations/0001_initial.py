# Generated by Django 5.0.1 on 2024-01-08 04:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("date_of_birth", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=100)),
                ("mobile_phone", models.CharField(max_length=10)),
                ("description", models.TextField(blank=True)),
                ("cv_path", models.CharField(blank=True, max_length=255)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("skill_name", models.CharField(max_length=255)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skills",
                        to="my_infor.person",
                    ),
                ),
            ],
        ),
    ]

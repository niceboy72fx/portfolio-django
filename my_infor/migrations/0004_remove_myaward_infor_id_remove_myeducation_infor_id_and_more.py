# Generated by Django 5.0.1 on 2024-01-08 18:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("my_infor", "0003_contact_myexperience_myframework_myinfor_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="myaward",
            name="infor_id",
        ),
        migrations.RemoveField(
            model_name="myeducation",
            name="infor_id",
        ),
        migrations.RemoveField(
            model_name="myproject",
            name="infor_id",
        ),
    ]

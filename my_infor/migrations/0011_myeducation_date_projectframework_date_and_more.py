# Generated by Django 5.0.1 on 2024-01-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_infor", "0010_auto_20240108_1851"),
    ]

    operations = [
        migrations.AddField(
            model_name="myeducation",
            name="date",
            field=models.DateField(default="2022-01-01"),
        ),
        migrations.AddField(
            model_name="projectframework",
            name="date",
            field=models.DateField(default="2022-01-01"),
        ),
        migrations.AddField(
            model_name="projectskill",
            name="date",
            field=models.DateField(default="2022-01-01"),
        ),
        migrations.AlterField(
            model_name="myinfor",
            name="date",
            field=models.DateField(default="2022-01-01"),
        ),
    ]

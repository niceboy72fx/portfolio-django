# Generated by Django 5.0.1 on 2024-01-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_infor", "0008_alter_contact_id_alter_frameworkexperience_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myinfor",
            name="date",
            field=models.DateField(),
        ),
    ]
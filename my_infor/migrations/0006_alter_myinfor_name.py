# Generated by Django 5.0.1 on 2024-01-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_infor", "0005_alter_myinfor_cv_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myinfor",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "my_infor",
            "0004_remove_myaward_infor_id_remove_myeducation_infor_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="myinfor",
            name="cv_path",
            field=models.FileField(upload_to="cv_files/"),
        ),
    ]

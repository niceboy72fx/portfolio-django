# Generated by Django 5.0.1 on 2024-01-08 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_infor", "0002_alter_person_table_alter_skill_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("email", models.CharField(max_length=200)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="MyExperience",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("company_name", models.CharField(max_length=255)),
                ("time", models.DateTimeField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="MyFramework",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="MyInfor",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("date", models.DateTimeField()),
                ("email", models.CharField(max_length=100)),
                ("mobile_phone", models.CharField(max_length=10)),
                ("description", models.TextField()),
                ("cv_path", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="skill",
            name="person",
        ),
        migrations.AlterField(
            model_name="skill",
            name="skill_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name="skill",
            table=None,
        ),
        migrations.CreateModel(
            name="FrameworkExperience",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "experience_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.myexperience",
                    ),
                ),
                (
                    "framework_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.myframework",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="myframework",
            name="infor_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="my_infor.myinfor",
            ),
        ),
        migrations.CreateModel(
            name="MyEducation",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=255)),
                (
                    "infor_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.myinfor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MyAward",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=255)),
                (
                    "infor_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.myinfor",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="skill",
            name="infor_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="my_infor.myinfor",
            ),
        ),
        migrations.CreateModel(
            name="MyProject",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                (
                    "infor_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.myinfor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectFramework",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "fw_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.myframework",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.myproject",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectSkill",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "infor_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.myinfor",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.myproject",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SkillExperience",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "experience_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.myexperience",
                    ),
                ),
                (
                    "skill_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_infor.skill",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Person",
        ),
    ]

from django.db import models

# Create your models here.

class MyInfor(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=255)
    date = models.DateField(default='2022-01-01')
    email = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=10)
    description = models.TextField()
    cv_path = models.FileField(upload_to='cv_files/')
    password = models.CharField(max_length=255)

class Skill(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    infor_id = models.ForeignKey(MyInfor, on_delete=models.CASCADE , default=1)
    skill_name = models.CharField(max_length=100)

class MyExperience(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    company_name = models.CharField(max_length=255)
    date = models.DateField(default='2022-01-01')
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField()

class SkillExperience(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    experience_id = models.ForeignKey(MyExperience, on_delete=models.CASCADE, default=1)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE , default=1)

class MyProject(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=200)
    date = models.DateField(default='2022-01-01')
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField()

    

class MyFramework(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    infor_id = models.ForeignKey(MyInfor, on_delete=models.CASCADE , default=1)
    name = models.CharField(max_length=200)

class FrameworkExperience(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    experience_id = models.ForeignKey(MyExperience, on_delete=models.CASCADE, default=1)
    framework_id = models.ForeignKey(MyFramework, on_delete=models.CASCADE, default=1)

class MyAward(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)

class MyEducation(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    
    name = models.CharField(max_length=200)
    date = models.DateField(default='2022-01-01')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)

class ProjectSkill(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    infor_id = models.ForeignKey(MyInfor, on_delete=models.CASCADE, default=1)
    date = models.DateField(default='2022-01-01')
    project_id = models.ForeignKey(MyProject, on_delete=models.CASCADE, default=1)

class ProjectFramework(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    fw_id = models.ForeignKey(MyFramework, on_delete=models.CASCADE, default=1)
    date = models.DateField(default='2022-01-01')
    project_id = models.ForeignKey(MyProject, on_delete=models.CASCADE, default=1)

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()


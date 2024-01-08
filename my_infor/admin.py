from django.contrib import admin
from .models import MyAward,MyEducation,MyFramework,MyExperience,MyInfor,MyProject,Skill,SkillExperience, Contact
# Register your models here.



@admin.register(MyInfor)
class MyInforAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'email', 'mobile_phone', 'cv_path','description')
    def has_add_permission(self, request):
        return False
    

    
@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    list_display =  ('name','date', 'title', 'description')
    
@admin.register(MyFramework)
class MyFrameworkAdmin(admin.ModelAdmin):
    list_display = [ 'name']
    
        
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name']

@admin.register(MyAward)
class MyAwardAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description')
   

@admin.register(MyEducation)
class MyEducationAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'title', 'description')
    
@admin.register(MyExperience)
class MyExperience(admin.ModelAdmin):
    list_display = ( 'company_name','date', 'title', 'description')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'message')
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
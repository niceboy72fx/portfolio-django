from django.shortcuts import render, redirect
from .models import MyAward,MyEducation,MyFramework,MyExperience,MyInfor,MyProject,Skill,SkillExperience, Contact
from django import forms
# Create your views here.

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            Contact.objects.create(email=email, subject=subject, message=message)
            return redirect('/') 
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

def home_page(request):
    my_infor = MyInfor.objects.first()  
    skills = Skill.objects.all()
    experiences = MyExperience.objects.all()
    projects = MyProject.objects.all()
    frameworks = MyFramework.objects.all()
    awards = MyAward.objects.all()
    educations = MyEducation.objects.all()
    contacts = Contact.objects.all()

    context = {
        'my_infor': my_infor,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
        'frameworks': frameworks,
        'awards': awards,
        'educations': educations,
        'contacts': contacts,
    }
    return render(request, 'index.html',context)
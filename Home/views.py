from ContactMe.models import ContactMe
from Projects.models import Projects
from django.shortcuts import render
from Skills.models import Skills
from .models import Settings




def home_page(request):
    projects = Projects.objects.all()
    skills = Skills.objects.all()
    settings = Settings.objects.first()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['name']

        if len(name) > 0 and len(email) > 0 and len(message)> 0:
            contactme = ContactMe.objects.create(name=name,email=email,message=message)
            context = {
                'projects': projects,
                'skills': skills,
                'settings': settings,
                'sent': 'Sent',
            }
            return render(request, 'Home/home_page/home_page.html', context)
        else:
            context = {
                'projects': projects,
                'skills': skills,
                'settings': settings,
                'notsent': 'Not Sent',
            }
            return render(request, 'Home/home_page/home_page.html', context)


    context = {
        'projects': projects,
        'skills': skills,
        'settings': settings,
    }
    return render(request,'Home/home_page/home_page.html',context)

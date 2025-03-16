from django.shortcuts import render, HttpResponse
from .models import Home, About, SocialLinks, SkillCategory, Skill, Portfolio, Contact, ContactMessage

def index(request):
    home = Home.objects.latest('updated_at')
    about = About.objects.latest('updated_at')
    social_links = SocialLinks.objects.all()  
    skill_category = SkillCategory.objects.all()
    skills = Skill.objects.all()
    if not skill_category:
        return HttpResponse("No skill categories found!")
    portfolio = Portfolio.objects.latest('id')  # updated_at if you have it
    contact = Contact.objects.latest('updated_at')


    context = {
        'home': home,
        'about': about,
        'social_links': social_links, 
        'skill_categories': skill_category,
        'skills': skills,
        'portfolio': portfolio,
        'contact': contact,
    }
    return render(request, 'index.html', context)
from django.shortcuts import render, HttpResponse, redirect
from .models import Home, About, SocialLinks, SkillCategory, Skill, Portfolio, Contact, ContactMessage

def index(request):
   
    
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not email:
            return HttpResponse("Email is required")
        elif not message:
            return HttpResponse("Message is required")
        elif not name:
            return HttpResponse("Name is required")
        else:  
            # Save the message to the database
            ContactMessage.objects.create(name=name, email=email, message=message)

            return redirect('/')  # R
    
    
    home = Home.objects.latest('updated_at')
    about = About.objects.latest('updated_at')
    social_links = SocialLinks.objects.all()  
    skill_category = SkillCategory.objects.all()
    skills = Skill.objects.all()
    if not skill_category:
        return HttpResponse("No skill categories found!")
    portfolio_projects = Portfolio.objects.all()  # updated_at if you have it
    contact = Contact.objects.latest('updated_at')


    context = {
        'home': home,
        'about': about,
        'social_links': social_links, 
        'skill_categories': skill_category,
        'skills': skills,
        'portfolio_projects': portfolio_projects,
        'contact': contact,
    }
    return render(request, 'index.html', context)
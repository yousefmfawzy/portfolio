from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError
import os
from datetime import datetime





#constrain the size of image of home and about 
def validate_home_image_size(image):
    img=Image.open(image)
    if img.width !=931 or img.height !=1010 :
        raise ValidationError("Image must be exactly 931*1010 pixels.")
    
    
# Home Section Model
class Home(models.Model):
    name = models.CharField(max_length=100, default="my_name")
    ProfileImage = models.ImageField(upload_to='home/',validators=[validate_home_image_size])
    greeting_1 = models.CharField(max_length=100, default="He")
    greeting_2 = models.CharField(max_length=100, default="llo.")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    


def rename_cv(instance,filename):
    ext = filename.split('.')[-1]
    filename = f"my_cv_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    return os.path.join('cv/', filename)


# Clearly validate file size max 5MB
def validate_cv_size(value):
    filesize = value.size
    if filesize > 5 * 1024 * 1024:  # 5MB limit
        raise ValidationError("The maximum file size allowed is 5MB.")    

# About Section Model
class About(models.Model):
    home = models.OneToOneField(Home, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    cv= models.FileField(upload_to=rename_cv, null=True, blank=True, validators=[validate_cv_size])
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.home.name


class SocialLinks(models.Model):
    About = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=100)
    social_icon = models.ImageField(upload_to='About_icon/', null=True, blank=True)
    social_url = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)# Skills Section Models
    
    def __str__(self):
        return self.social_name
    
    # 



class SkillCategory(models.Model):
    category_name  = models.CharField(max_length=100)  # e.g., "Development", "Design"
    uptaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Skills category'

    def __str__(self):
        return self.category_name 


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    skill_name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.category.category_name} : {self.skill_name}" 



#constrain the size of image of portfolio
def validate_image_size(image):
    img=Image.open(image)
    if img.width !=640 or img.height != 425:
        raise ValidationError("Image must be exactly 640x425 pixels.")
    

# Portfolio Section Model
class Portfolio(models.Model):
    project_nu=models.IntegerField(null=False,)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/' ,validators =[validate_image_size])
    description = models.TextField(blank=True)
    project_link = models.URLField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return  "".join(str(self.project_nu))+ " " +self.title


# Contact Section Model (for displayed contact info)
class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Contact Info: {self.email}"


#  for contact form submissions
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
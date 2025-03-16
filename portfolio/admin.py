from django.contrib import admin
from .models import Home, About, SocialLinks, SkillCategory, Skill,Contact,ContactMessage,Portfolio


# Register your models here.
admin.site.register(Home)

class SocialLinksInline(admin.TabularInline):
    model = SocialLinks
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [SocialLinksInline]

admin.site.register(SocialLinks)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(ContactMessage)
admin.site.register(Portfolio)
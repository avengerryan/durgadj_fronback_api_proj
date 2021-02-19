from django.contrib import admin
from .models import Hydjobs, Chennaijobs, Blorejobs, Punejobs


# Register your models here.

class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']


class BlorejobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']


class ChennaijobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']


class PunejobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']





admin.site.register(Hydjobs, HydjobsAdmin)
admin.site.register(Blorejobs, BlorejobsAdmin)
admin.site.register(Chennaijobs, ChennaijobsAdmin)
admin.site.register(Punejobs, PunejobsAdmin)







































from django.contrib import admin
from afterlogin.models import Complain

# Register your models here.

class Complainadmin(admin.ModelAdmin):
    readonly_fields = ('username','problem','description', 'image',
                            'address','zip','ward')
admin.site.register(Complain,Complainadmin)
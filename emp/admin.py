from django.contrib import admin
from .models import Emp, Testimonial
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','mobile','email','address')
    list_editable=('working',)
    search_fields=('name','mobile')
    list_filter=('working',)


admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)

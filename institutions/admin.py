from django.contrib import admin

# Register your models here.
from .models import MOHArea, DSDivision, Institution, District

admin.site.register(District)
admin.site.register(DSDivision)
admin.site.register(Institution)
admin.site.register(MOHArea)

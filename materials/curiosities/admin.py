from django.contrib import admin
from materials.curiosities.models import Curiosities


@admin.register(Curiosities)
class CuriositiesAdmin(admin.ModelAdmin):
    list_display = ('name',)

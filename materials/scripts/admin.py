from django.contrib import admin

from materials.scripts.models import Scripts


@admin.register(Scripts)
class ScriptsAdmin(admin.ModelAdmin):
    list_display = ('name',)

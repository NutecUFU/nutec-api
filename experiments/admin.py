from django.contrib import admin
from experiments.models import Experiment

# admin.site.register(Experiment)
@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'status',)
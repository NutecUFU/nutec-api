from rest_framework import serializers
from schedules.models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('name', 'email', 'institution', 'date', 'time_init', 'time_end', 'number_users', 'register', 'experiment')
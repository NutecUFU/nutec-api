from rest_framework import generics

from schedules.models import Schedule
from schedules.serializers import ScheduleSerializer


class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

from django.urls import path
from schedules import views

urlpatterns = [
    path('', views.ScheduleList.as_view())
]
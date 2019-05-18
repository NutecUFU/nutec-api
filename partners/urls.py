from django.urls import path
from partners import views

urlpatterns = [
    path('', views.PartnerList.as_view())
]
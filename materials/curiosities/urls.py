from django.urls import path
from materials.curiosities import views

urlpatterns = [
    path('', views.CuriositiesList.as_view()),
    path('<int:pk>/', views.CuriositiesDetail.as_view())
]

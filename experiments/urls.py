from django.urls import path
from experiments import views

urlpatterns = [
    path('', views.ExperimentList.as_view()),
    path('<int:pk>/', views.ExperimentDetail.as_view())
]
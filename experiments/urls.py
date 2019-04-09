from django.urls import path
from experiments import views

urlpatterns = [
    path('', views.ExperimentViewSet.as_view({'get': 'list', 'post': 'create'}), name='experiment-list')
]
from django.urls import path
from materials.scripts import views

urlpatterns = [
    path('', views.ScriptsList.as_view()),
    path('<int:pk>/', views.ScriptsDetail.as_view())
]

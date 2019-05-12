from django.urls import path
from contacts import views

urlpatterns = [
    path('', views.ContactList.as_view()),
    path('<int:pk>/', views.ContactDetail.as_view())
]
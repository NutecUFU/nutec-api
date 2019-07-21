from django.urls import path
from users import views

urlpatterns = [
    path('', views.NewUser),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('groups/', views.TeamList.as_view(), name="users-groups")
]
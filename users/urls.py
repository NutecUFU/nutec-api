from django.urls import path
from users import views

urlpatterns = [
    path('', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list')
]
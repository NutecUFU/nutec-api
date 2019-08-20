from django.urls import path, include

urlpatterns = [
    path('curiosities/', include('materials.curiosities.urls')),
    path('scripts/', include('materials.scripts.urls'))
]

from rest_framework import generics, permissions

from materials.curiosities.serializers import CuriositiesSerializer
from materials.curiosities.models import Curiosities


class CuriositiesList(generics.ListCreateAPIView):
    queryset = Curiosities.objects.all()
    serializer_class = CuriositiesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CuriositiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curiosities.objects.all()
    serializer_class = CuriositiesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

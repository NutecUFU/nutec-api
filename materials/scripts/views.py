from rest_framework import generics, permissions

from materials.scripts.models import Scripts
from materials.scripts.serializers import ScriptsSerializer


class ScriptsList(generics.ListCreateAPIView):
    queryset = Scripts.objects.all()
    serializer_class = ScriptsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ScriptsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scripts.objects.all()
    serializer_class = ScriptsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

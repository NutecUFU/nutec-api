from rest_framework import generics, permissions
from partners.models import Partner
from partners.serializers import PartnerSerializer


class PartnerList(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PartnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

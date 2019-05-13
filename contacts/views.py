from rest_framework import permissions, generics
from contacts.models import Contact
from contacts.serializer import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.order_by('date')
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

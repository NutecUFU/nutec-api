from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer


def getUsers():
    return User.objects.all()


@api_view(['POST'])
def NewUser(request):
    user = UserSerializer(data=request.data)

    if user.is_valid():
        user.save()
        return Response(user.data)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class UserDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @staticmethod
    def getUser(pk):
        return User.objects.get(pk=pk)

    def get(self, request, pk):
        users = self.getUser(pk)
        serializer = UserSerializer(users)
        return Response(serializer.data)

    def put(self, request, pk):
        users = self.getUser(pk)
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        users = self.getUser(pk)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

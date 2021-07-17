from .models import Author, User
from .serializers import AuthorSerializer, UsersSerializer
from rest_framework.viewsets import ModelViewSet


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class UsersViewSet(ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()

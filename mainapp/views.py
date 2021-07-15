from django.shortcuts import render

from .models import Author
from .serializers import AuthorSerializer
from rest_framework.viewsets import ModelViewSet


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


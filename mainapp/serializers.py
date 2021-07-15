from rest_framework.serializers import ModelSerializer
from .models import Author, Users


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '_all_'


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '_all_'

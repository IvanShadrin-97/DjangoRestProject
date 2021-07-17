from rest_framework.serializers import ModelSerializer
from .models import Author, User


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

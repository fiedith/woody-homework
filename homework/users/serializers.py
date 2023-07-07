from rest_framework import serializers
from .models import User
from boards.serializers import BoardSerializer

class UserSerializer(serializers.ModelSerializer):
    user = BoardSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'
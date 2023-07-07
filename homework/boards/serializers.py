from rest_framework import serializers
from .models import Board
# from users.serializers import UserSerializer

class BoardSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'title', 'content', 'user_id']


    # def create(self, validated_data):
    #     validated_data['author'] = self.context['request'].user
    #     return super().create(validated_data)
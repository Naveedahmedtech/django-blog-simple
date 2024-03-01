from rest_framework import serializers
from .models import Category, Post, ProfileName

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileName
        fields = '__all__'

from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['big', 'detail', 'url', 'title', 'author', 'date']

class CategorySaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['big', 'detail']
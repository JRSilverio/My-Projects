from rest_framework import serializers
from .models import Tag, Category

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CategorytSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
from django.shortcuts import render
from rest_framework import generics
from .models import Tag, Category
from .serializers import TagSerializer, CategorytSerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorytSerializer
from django.urls import path
from .views import TagListCreateView, CategoryListCreateView

urlpatterns = [
    path('articles/tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('articles/category/', CategoryListCreateView.as_view(), name='category-list-create'),
]

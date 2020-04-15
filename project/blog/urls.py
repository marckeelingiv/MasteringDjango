from django.urls import path,include
from .views import BlogListView,BlogDetailView
urlpatterns = [
    path('post/<int:pk>/',BlogDetailView.as_view(),name='blogpost_detail'),
    path('',BlogListView.as_view(),name='blogposts'),
]
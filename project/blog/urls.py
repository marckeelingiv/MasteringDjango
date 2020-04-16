from django.urls import path,include
from .views import BlogListView,BlogDetailView,BlogPostCreateView,BlogPostUpdateView,BlogPostDeleteView
urlpatterns = [
    path('post/<int:pk>/delete',BlogPostDeleteView.as_view(),name='blogpost_delete'),
    path('post/<int:pk>/update',BlogPostUpdateView.as_view(),name='blogpost_update'),
    path('post/new/',BlogPostCreateView.as_view(),name='blogpost_create'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='blogpost_detail'),
    path('',BlogListView.as_view(),name='blogposts'),
]
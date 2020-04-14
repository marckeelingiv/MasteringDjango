from django.urls import path
from .views import HomePageView,AboutPageView,ResumePageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('resume/',ResumePageView.as_view(),name='resume'),
]
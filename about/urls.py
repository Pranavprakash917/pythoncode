from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('about1/',views.about1,name='about'),
]
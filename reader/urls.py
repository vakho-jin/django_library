from django.urls import path
from . import views

urlpatterns = [
    path('success/<int:pk>/', views.success_page, name = 'success_page'),
]
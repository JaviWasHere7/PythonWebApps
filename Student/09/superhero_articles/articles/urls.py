from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('create/', views.create_article, name='create_article'),  # Create Article
    path('edit/<int:pk>/', views.edit_article, name='edit_article'),  # Edit Article
]
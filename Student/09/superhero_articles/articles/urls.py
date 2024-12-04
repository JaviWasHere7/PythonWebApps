from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.SuperheroListView.as_view(), name='list'),
    path('<int:pk>/', views.SuperheroDetailView.as_view(), name='detail'),
    path('add/', views.SuperheroCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', views.SuperheroUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.SuperheroDeleteView.as_view(), name='delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

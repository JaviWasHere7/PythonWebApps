from django.urls import path
from .views import BlackWidow, HulkView, IndexView, IronManView, RajangView

urlpatterns = [
    path('', IndexView.as_view()),
    path('nergigante', HulkView.as_view()),
    path('espinas', IronManView.as_view()),
    path('bazelgeuse', BlackWidow.as_view()),
    path('rajang', RajangView.as_view()),
]

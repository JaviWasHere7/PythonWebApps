from django.urls import path
from .views import BatmanView, DeadPoolView, IndexView, SpiderManView, IronmanView, GambitView

urlpatterns = [
    path('', IndexView.as_view()),
    path('deadpool', DeadPoolView.as_view()),
    path('spiderman', SpiderManView.as_view()),
    path('batman', BatmanView.as_view()),
    path('ironman', IronmanView.as_view()),
    path('gambit', GambitView.as_view()),
]
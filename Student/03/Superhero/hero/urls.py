from django.urls import path
from .views import BazelgeuseView, EspinasView, IndexView, NergiganteView, RajangView, VaalHazakView

urlpatterns = [
    path('', IndexView.as_view()),
    path('nergigante', NergiganteView.as_view()),
    path('espinas', EspinasView.as_view()),
    path('bazelgeuse', BazelgeuseView.as_view()),
    path('rajang', RajangView.as_view()),
    path('vaal_hazak', VaalHazakView.as_view()),
]

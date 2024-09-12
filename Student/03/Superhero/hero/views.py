from typing import Any
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class NergiganteView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Nergigante',
            'body': 'Monster Type: Elder Dragon',
            'image': '/static/images/nergigante.jpg'
        }


class EspinasView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Espinas',
            'body': 'Monster Type: Flying Wyverns',
            'image': '/static/images/espinas.jpg'
        }


class BazelgeuseView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Bazelgeuse',
            'body': 'Monster Type: Flying Wyverns',
            'image': '/static/images/bazelgeuse.jpg'
        }
    

class RajangView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Rajang',
            'body': 'Monster Type: Fanged Beast',
            'image': '/static/images/rajang.jpg'
        }
    

class VaalHazakView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Vaal Hazak',
            'body': 'Monster Type: Elder Dragon',
            'image': '/static/images/vaal_hazak.jpg'
        }
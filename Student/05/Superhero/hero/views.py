from typing import Any
from django.views.generic import TemplateView

from .models import Superhero

class HeroListView(TemplateView):
    template_name = 'heros.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Superhero.objects.all()
        }
    
class HeroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'hero': Superhero.objects.get(pk=kwargs['pk'])
        }

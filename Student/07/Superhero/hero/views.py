from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Superhero
from django.contrib.auth.mixins import LoginRequiredMixin

class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero
    context_object_name = 'heros'

class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero
    context_object_name = 'hero'

class HeroCreateView(CreateView):
    template_name = 'hero/add.html'
    model = Superhero
    fields = '__all__'

class HeroUpdateView(UpdateView):
    template_name = 'hero/edit.html'
    model = Superhero
    fields = '__all__'

class HeroDelateView(DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'

class HeroCreative(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'
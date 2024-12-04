from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Superhero
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm

class SuperheroListView(ListView):
    model = Superhero
    template_name = 'articles/list.html'
    context_object_name = 'superheroes'

class SuperheroDetailView(DetailView):
    model = Superhero
    template_name = 'articles/detail.html'

class SuperheroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    fields = ['name', 'identity', 'description', 'strength', 'weakness', 'image']
    template_name = 'articles/form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SuperheroUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Superhero
    fields = ['name', 'identity', 'description', 'strength', 'weakness', 'image']
    template_name = 'articles/form.html'

    def test_func(self):
        superhero = self.get_object()
        return self.request.user == superhero.author

class SuperheroDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Superhero
    success_url = reverse_lazy('articles:list')
    template_name = 'articles/confirm_delete.html'

    def test_func(self):
        superhero = self.get_object()
        return self.request.user == superhero.author

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'articles/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'articles/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('articles:list')
from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView
# Create your views here.

class blogListView(ListView):
    model = Publication 
    template_name = 'home.html'

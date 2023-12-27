from django.shortcuts import render
from .models import Adherent, Abonement, Sport
from django.views.generic import ListView, DetailView, CreateView, DeleteView

# Create your views here.

class AdherentList(ListView):
    model = Adherent



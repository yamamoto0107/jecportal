from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from .forms import AttendForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class AttendCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = AttendForm
    success_url = reverse_lazy('diary:diary_create_complete')

class AttendCreateCompleteView(TemplateView):
    template_name = 'attend_create_complete.html'
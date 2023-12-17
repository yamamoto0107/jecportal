from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from .forms import AttendForm
from .models import Attend
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    

class AttendCreateView(CreateView):
    template_name = 'attend_create.html'
    form_class = AttendForm
    success_url = reverse_lazy('portal:attend_create_complete')

class AttendCreateCompleteView(TemplateView):
    template_name = 'attend_create_complete.html'

class AttendListView(ListView):
    template_name = 'attend_list.html'
    model = Attend

class AttendDetailView(DetailView):
    template_name = 'attend_detail.html'
    model = Attend

def index(request):
    if request.method == 'POST':
            name=request.POST['name']
            password = request.POST['pass']
            print(password)
            context={
                "name":name,
                "age":password
            }
            return render(request, 'index.html',context)
    else:
        context={
            "name":"",
            "age":""
        }
        return render(request, 'index.html',context)
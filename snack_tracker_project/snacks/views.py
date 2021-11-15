from django.shortcuts import render
from django.views.generic import (ListView,DetailView)
from .models import Snack
# Create your views here.






class SnackPageView(ListView):
    template_name='snack_list.html'
    model=Snack

class SnackListDetail(DetailView):
    template_name = "list_detail.html"
    model = Snack
    context_object_name = "snack_object" 
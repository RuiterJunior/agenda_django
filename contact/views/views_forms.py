from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from contact import models
from django.core.paginator import Paginator

# Create your views here.
def create(request):
    context = {
        
    }

    return render(request, 'contact/create.html', context)


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Section, Contact
from .forms import ContactForm
from django.urls import reverse
from django.views.generic.edit import CreateView

# Create your views here.
def mynameView(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})

def successfulMsg(request):
    return render(request, 'sucMsg.html' ) 

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
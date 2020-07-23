from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"YO BROOOOOO"
    }

    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def sercice(request):
    return render(request, "service.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        cell = request.POST.get('cell')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, cell = cell, desc = desc, date = datetime.today() )
        contact.save()
        messages.success(request, "Submitted")


    return render(request, "contact.html")




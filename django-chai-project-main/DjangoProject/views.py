from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, world! This is the home page of the Django project.")
    return render(request, 'index.html');

def about(request):
    return HttpResponse("This is the about page of the Django project.");

def contact(request):
    return HttpResponse("This is the contact page of the Django project."); 

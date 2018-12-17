from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    context = {}
    return render (request, 'index.html' , context)

def signup(request):
    context = {}
    return render (request, 'signup.html' , context)
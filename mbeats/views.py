from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def base(request):
    return render(request, 'base.html')

def base_user(request):
    return render(request, 'base_user.html')

def about(request):
    return HttpResponse("<h1>About !!!</h1>")

def contact(request):
    return HttpResponse("<h1>Contact !!!</h1>")

def login(request):
    return render(request, 'login.html')

def logout(request):
    return HttpResponse("<h1>LogOut !!!</h1>")

def index(request):
    return HttpResponse("<h1>Index !!!</h1>")

def register(request):
    return HttpResponse("<h1>Register !!!</h1>")

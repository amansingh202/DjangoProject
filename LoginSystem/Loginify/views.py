from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import UserDetails
from django.contrib import messages

def hello_world(request):
    return HttpRequest("Hello World!")

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if UserDetails.objects.filter(email = email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')
        
        user = UserDetails(username = username, email = email, password = password)
        user.save()
        messages.success(request,'Sugnup Successful!')
        return redirect('login')
    
    return render(request, 'signup.html')
        
    

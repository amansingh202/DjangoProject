from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import UserDetails
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json

def hello_world(request):
    return HttpResponse("Hello World! and page also contains /signup and /login")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')
        
        user = UserDetails(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Signup Successful!')
        return redirect('login')
    
    return render(request, 'signup.html')
        
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserDetails.objects.get(email=email, password=password)
            return render(request, 'success.html', {'user': user})
        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
        
    return render(request, 'login.html')


## Task 5
@csrf_exempt
def get_all_users(request):
    if request.method == 'GET':
        users = UserDetails.objects.all().values()
        return JsonResponse(list(users), safe=False)
    
@csrf_exempt
def get_user_by_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        try:
            user = UserDetails.objects.get(email=email)
            return JsonResponse({
                'username': user.username,
                'email': user.email,
                'password': user.password
            })
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        

@csrf_exempt
def update_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            updated = UserDetails.objects.filter(email=email).update(
                username=data.get('username'),
                password=data.get('password')
            )

            if updated == 0:
                return JsonResponse({'error': 'User not found'}, status=404)
            return JsonResponse({'message': 'User updated successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)






@csrf_exempt
def delete_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        try:
            user = UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

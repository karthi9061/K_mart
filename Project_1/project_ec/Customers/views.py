from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Customer

def show_account(request):
    context={}
    if request.method == 'POST' and 'register' in request.POST:
        context['register']=True
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Validate required fields
        if not all([username, email, password, address, phone]):
            messages.error(request, "All fields are required.")
            return redirect('account')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('account')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('account')

        # Create user with hashed password
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create customer account
        customer = Customer.objects.create(user=user, phone=phone, address=address)

        messages.success(request, "Account created successfully!")
        return redirect('account')
    
    if request.method == 'POST' and 'login' in request.POST:
        context['register']=False

        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('account')

        
    return render(request, 'account.html',context)

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('account')

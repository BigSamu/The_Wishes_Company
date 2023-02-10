from django.shortcuts import render, redirect
from .models import *
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    if 'name' in request.session:
        return redirect('/wishes')
    return render(request,'index.html')

# Register new user
def register(request):
    
    errors = User.objects.validatorSignUp(request.POST)
    
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_password
    )
    
    request.session['name'] = newUser.first_name
    request.session['id'] = newUser.id
    return redirect('/wishes')

# Login for current user
def login(request):
    
    if request.method == 'POST':
        errors = User.objects.validatorSignIn(request.POST)
        
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        loggedUser = User.objects.get(email=request.POST['email'])
        request.session['name'] = loggedUser.first_name
        request.session['id'] = loggedUser.id
        return redirect('/wishes')

    return redirect('/')
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

import time

# @login_required(login_url='/login')
def homePage(request):
    print(request.user.is_authenticated);
    print(request.user)
    return render(request,"index.html")


def loginPage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == '' or password == '':
            messages.info(request, "Enter valid details")
            return redirect('/login')
        
        user = authenticate(request, email=email, password=password)
        print("userauth",user);
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to home page (adjust the URL name as per your project)
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/login')
    
    return render(request, 'login.html')

def signUpPage(request):
    context = {
        'username': "",
        'password': "",
        'email': ""
    }
   
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if username == '' or email == '' or password == '':
            messages.info(request, "Enter valid details")
            
            return redirect('/sign-up');
            
        user_exists_username = User.objects.filter(username=username).exists()
        if user_exists_username:
            context['email'] = email;
            context['password']=password
            context['username'] = username
            messages.error(request, "Username is already taken.")
            return render(request, "signup.html",{'context':context})
        
        user_exists_email = User.objects.filter(email=email).exists()
        if user_exists_email:
            context['email'] = email;
            context['password']=password
            context['username'] = username
            messages.error(request, "Email already exists.")
            return render(request, "signup.html",{'context':context})
        
        # Create user with hashed password
        user = User.objects.create_user(username=username, email=email, password=password)
        # Optionally, you can also set other user fields
        print("user",user);
        # Redirect to login page or any other page
        messages.success(request,"User registered successfull.")
        time.sleep(2) # Sleep for 2 second
        return redirect('/login',{'context': context})
        
    
    return render(request, "signup.html",{'context':context})

def reminderlist(request):

    return render(request,"reminderlist.html")

def createReminder(request):
    return render(request, 'create_reminder.html')
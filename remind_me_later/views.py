import time
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib.auth.decorators import login_required
from reminder.models import Reminder

from reminder.utils import send_email_to_client

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
        
        authenticated_user = authenticate(request, email=email, password=password)
        if authenticated_user is not None:
            print("User authenticated:", authenticated_user)  # Debug statement
            login(request,user=authenticated_user)
            return redirect('/')  # Redirect to home page (adjust the URL name as per your project)
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/login')
    
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    HttpResponse("logging out user.")
    return redirect('/login')
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
    if request.method == "POST":
        user_message = request.POST.get("message")
        user_date = request.POST.get('date')
        user_time = request.POST.get('time')
        user_email = request.POST.get('email')

        if user_message == '' or user_date == '' or user_time == '' or user_email == '':
            messages.info(request, "Enter valid details")
            return redirect('/create-reminder')

        user = User.objects.filter(email=user_email).first()

        if user is not None:
            user_time_date_str = f"{user_date} {user_time}"
            print("date_time", user_time_date_str)
            try:
                user_time_date = datetime.strptime(user_time_date_str, "%Y-%m-%d %H:%M")
                # Adjust timezone if needed
                # user_time_date = timezone.make_aware(user_time_date)
            except ValueError:
                messages.error(request, "Invalid date or time format")
                return redirect('/create-reminder')
            
            # Create reminder for the authenticated user
            created_reminder = Reminder.objects.create(
                message=user_message,
                schedule_time=user_time_date,
                status='pending',
                user=user
            )
            print(created_reminder)
            messages.success(request, "Reminder created successfully")
            return redirect('/create-reminder')
        else:
            messages.error(request, 'User not found!')
            return redirect('/create-reminder')

    return render(request, 'create_reminder.html')



# testing email 
def sendEmail(request):
    send_email_to_client()
    return redirect('/')

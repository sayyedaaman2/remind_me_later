from datetime import datetime,time
import pytz
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from reminder.models import Reminder

from reminder.utils import schedule_email

# @login_required(login_url='/login')
def homePage(request):
    print(request.user.is_authenticated);
    print(request.user)

    return render(request,"index.html")


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or password == '':
            messages.info(request, "Enter valid details")
            return redirect('/login')
        
        authenticated_user = authenticate(request, username=username, password=password)
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
    reminder_list = None # Initialize as an empty list
    user_id = request.user

    try:
        reminder_list = Reminder.objects.filter(user_id=user_id)
    except Reminder.DoesNotExist:
        print("No reminders found for the user")
        reminder_list = None
        return render(request,'reminderlist.html',{'reminder_list': reminder_list})
    
    return render(request, "reminderlist.html", {'reminder_list': reminder_list})


def createReminder(request):
    if request.method == "POST":
        user_message = request.POST.get("message")
        scheduletime = request.POST.get('scheduletime')

        if user_message == '' or scheduletime == '':
            messages.info(request, "Enter valid details")
            return redirect('/create-reminder')
        
        user = request.user
        if user is not None:
            try:
                user_time_date = datetime.strptime(scheduletime, "%Y-%m-%dT%H:%M")
                ist_timezone = pytz.timezone('Asia/Kolkata')
                user_time_date_utc = ist_timezone.localize(user_time_date).astimezone(pytz.utc)

            except ValueError:
                messages.error(request, "Invalid date or time format")
                return redirect('/create-reminder')
            
            # Create reminder for the authenticated user
        
            created_reminder = Reminder.objects.create(
                message=user_message,
                schedule_time=user_time_date_utc,
                status='pending',
                user=user
            )
            print(created_reminder)
            messages.success(request, "Reminder created successfully")

            schedule_email(created_reminder)
            messages.success(request, "Email schedule successfully")

            return redirect('/reminder-list')
        else:
            messages.error(request, 'User not found!')
            return redirect('/create-reminder')

    return render(request, 'create_reminder.html')

def editReminder(request,id):
    # Fetch the reminder object based on the provided id
    try:
        reminder= Reminder.objects.get(id=id)
    except Reminder.DoesNotExist:
        return HttpResponse("Reminder not found", status=404)
        
    # Your edit logic goes here

    return render(request, 'edit_reminder.html',{'reminder':reminder})

def deleteReminder(request,id):
    #Fetch the reminder object based on the provided id
    try:
        reminder= Reminder.objects.get(id=id)

    except Reminder.DoesNotExist:
        return HttpResponse('Reminder not found', status=404)
    
    #Your delete logic goes here
    reminder.delete()

    return redirect('/reminder-list')

# testing email 
def sendEmail(request):
    send_email_to_client()
    return redirect('/')

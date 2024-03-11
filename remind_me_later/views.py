from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login
from users.models import User
from django.utils import timezone

def homePage(request):
    
    return render(request,"index.html")


def loginPage(request):
    errorObject = {"message": "", "error": False}

    try:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")

            print(user.username)
            if user is not None:
                # Log the user in 
                login(request, user)
                print('Login successful.')
                return HttpResponseRedirect('/')
            else:
                errorObject["message"] = "Invalid email or password."
                errorObject["error"] = True
                print(errorObject)
                return render(request, 'login.html', {"error": errorObject})
    except Exception as e:
        print("Error:", str(e))

    return render(request, 'login.html', {"error": errorObject})

def signUpPage(request):
    errorObject = {"message": "", "error": False}

    try:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            username = request.POST.get("username")

            if email is not None and password is not None and username is not None:
                user=User(email=email,password=password, username=username,created_at=timezone.now());
                user.save();
                print('successful created new user.')
                return HttpResponseRedirect('/')

            else:
                errorObject["message"] = "Invalid Data."
                errorObject["error"] = True
                return render(request, 'signup.html', {"error": errorObject})


    except Exception as e:
        print("Error:", str(e))
    return render(request, "signup.html")

def remiderList(request):

    return render(request,"remiderlist.html")

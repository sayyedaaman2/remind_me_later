"""
URL configuration for remind_me_later project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from remind_me_later import views

urlpatterns = [
    path('', views.homePage,name="home"),
    path('admin/', admin.site.urls),
    path('sign-up/', views.signUpPage),
    path('login/', views.loginPage),
    path('logout/',views.logoutPage),
    path('reminder-list/',views.reminderlist),
    path('create-reminder/',views.createReminder),
    path('reminder/edit/<int:id>/', views.editReminder, name='edit_reminder'),
    path('reminder/delete/<int:id>/', views.deleteReminder, name='delete_reminder'),
    path('send-email',views.sendEmail),
]

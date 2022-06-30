from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from datetime import datetime
from .forms import *
import joblib


class HomeView(TemplateView):
    template_name = 'pages/index.html'
    extra_content = {'today': datetime.today()}


def home(request):
    return render(request, 'pages/index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exist! Please try some other username.")
            return redirect('signin')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signin')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signin')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signin')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signin')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()
        return redirect('signin')
    # if request.method == 'POST':

    #     form = Signupform(request.POST, request.FILES)
    #     print(type(type))
    #     if form.is_valid():
    #         form.save()
    #         print("sav")
    #         return redirect('signin')
    # else:
    #     form = Signupform()

    return render(request, "create_account.html")


def signin(request):
    print("hello")
    if request.method == 'POST':
        print("hi")
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print("hi2")
        if user is not None:
            print("notnone")
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "pages/index.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signup')

    return render(request, "sign_in.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')


def Prediction(request):
    cls = joblib.load('finalized_model (1).sav')
    print("hello1")
    lis = []
    lis.append(request.GET['bedrooms'])
    lis.append(request.GET['bathrooms'])
    lis.append(request.GET['SQFT_Living'])
    lis.append(request.GET['SQFT_lot'])
    lis.append(request.GET['floors'])
    lis.append(request.GET['waterfront'])
    lis.append(request.GET['condition'])
    lis.append(request.GET['grade'])
    lis.append(request.GET['SQFT_above'])
    lis.append(request.GET['SQFT_lot15'])
    lis.append(request.GET['yr_built'])
    lis.append(request.GET['SQFT_living15'])
    lis.append(request.GET['lat'])
    lis.append(request.GET['long'])
    print("hello2")

    ans = cls.predict([lis])
    return render(request, "result.html", {'ans': ans})

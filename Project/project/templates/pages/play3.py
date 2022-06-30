from django.shortcuts import render, redirect 
from django.http import
HttpResponse from django.contrib.auth.models import User from django.contrib
import messages from project import settings from django.contrib.auth import
authenticate, login from django.views.generic import TemplateView from
django.views.generic.list import ListView from django.views.generic.detail
import DetailView from datetime import datetime # from . tokens import
generate_token # Create your views here. class UsersDetails(DetailView): model =
User context_object_name = "details" class HomeView(TemplateView): template_name
= 'pages/index.html' extra_content = {'today': datetime.today()} class
AboutUs(TemplateView): template_name = 'aboutUs.html' # def index(request): #
return render(request, 'pages/index.html') class Users(ListView): template_name
= 'settings.html' model = User context_object_name = "users" class
Result(TemplateView): template_name = 'pages/result.html' # def result(request):
# return render(request, 'pages/result.html') def signup(request): if
request.method == "POST": username = request.POST['username'] fname =
request.POST['fname'] lname = request.POST['lname'] # ('lname', "lname") email =
request.POST['email'] pass1 = request.POST['pass1'] pass2 =
request.POST['pass2'] # ('pass2', "pass2") if
User.objects.filter(username=username): messages.error( request, "Username
already exist! Please try some other username.") return redirect('signup') if
User.objects.filter(email=email).exists(): messages.error(request, "Email
Already Registered!!") return redirect('signup') if len(username) > 20:
messages.error(request, "Username must be under 20 charcters!!") return
redirect('signup') if pass1 != pass2: messages.error(request, "Passwords didn't
matched!!") return redirect('signup') if not username.isalnum():
messages.error(request, "Username must be Alpha-Numeric!!") return
redirect('signup') myuser = User.objects.create_user( username, email, pass1)
myuser.first_name = fname myuser.last_name = lname # myuser.is_active = False
myuser.is_active = False myuser.save() return render(request,
"pages/create_account.html") def signin(request): if request.method == 'POST':
username = request.POST['username'] password = request.POST['password'] user =
authenticate(username=username, password=password) if user is not None:
login(request, user) # fname = user.first_name # x = { # 'fname': 'ali'} return
render(request, "pages/index.html") else: messages.error(request, "Bad
Credentials!!") return redirect('signup') return render(request,
"pages/sign_in.html") def setting(request): return render(request,
'settings.html') # def details(request): # return render(request,
'pages/details_page.html') def about(request): x = { 'fname': 'ali'} return
render(request, 'pages/aboutUs.html', x) def sell3(request): return
render(request, 'pages/sell-4.html') def sell2(request): return render(request,
'pages/sell 3.html') def sell(request): return render(request,
'pages/sell1,2.html') def feature(request): return render(request,
'pages/index.html') def filter(request): return render(request, 'pages/onboaded
i.html') def filter2(request): return render(request, 'pages/onboaded ii.html')
def filter3(request): return render(request, 'pages/onboaded iii.html')

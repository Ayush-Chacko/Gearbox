from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from .models import Tools
from .forms import ToolForm

def show(request):
    return HttpResponse("Hello, Welcome to our page!")

def tools(request):
    tool_list = Tools.objects.all()
    return render(request, "tools.html", {"tools": tool_list})

def home(request):
    return render(request,"home.html")

def login_view(request):
    if request.method == "POST":
        # Use parentheses for the get method
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('userhome')  # Redirect to home or any other page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        # Use parentheses for the get method
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Create a new user
        User.objects.create_user(username=username, password=password, email=email)

        return redirect('login')  # Redirect to home or any other page after login
    
    return render(request, 'signup.html')

def user_homepage(request):
    # You can include additional context data as needed.
    context = {
        'user': request.user  # This assumes that you want to access the logged-in user details in the template.
    }
    return render(request, 'user_homepage.html', context)

def shop_home(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workshop_home')  # name of this view in urls.py
    else:
        form = ToolForm()

    tools = Tools.objects.all().order_by('-created_at')  # newest first
    return render(request, 'workshop.html', {
        'form': form,
        'tools': tools,
    })

def shop_login(request):
    if request.method == "POST":
        # Use parentheses for the get method
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('shophome')  # Redirect to home or any other page after login
        else:
            return render(request, 'shop_login.html', {'error': 'Invalid credentials'})

    return render(request, 'shop_login.html')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):

    username = "everson"  # request.POST["username"]
    password = "Ev1629mA@"  # request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        print("Login here!")
        return redirect("/")

    return render(request, "auth/login.html", {})

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import User

# Create your views here.
class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.save()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')

        except:
            user = User.objects.get(username=username)
            if user:
                messages.warning(request, 'Username already taken')
                return redirect('user:register')


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        messages.warning(request, 'Invalid username or password')
        return redirect('user:register')
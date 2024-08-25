from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('user:register')
        return render(request, 'home.html')
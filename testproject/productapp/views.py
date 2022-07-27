from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from productapp.forms import UserCreationForm,UserLoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from productapp.models import Products


# Create your views here.

class UserCreationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


def userloginview(request):
    context = {'form': UserLoginForm}
    template_name = 'login.html'
    if request.user.is_authenticated:
        return redirect('products')
        messages.warning(request, "Yor Are Already Logged in ")
    else:
        if request.method == "POST":
            form = UserLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return redirect('products')
                else:
                    success_message = "Acconty Created Succesfuly"
                    messages.error(request, "Invalid Password or Username")
                    return redirect('login')
        return render(request, template_name, context)

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Succesfully")
    return redirect('login')

def productview(request):
    product = Products.objects.all()
    context = {"product":product}
    return render(request,"product.html",context)

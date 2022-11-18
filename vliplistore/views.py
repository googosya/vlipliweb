from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import SignUp
from .forms import SingUpModelForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt

def main_page(request):
    form = SingUpModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SingUpModelForm()

    context = { 
        "form": form, 
    }
    return render(request, 'main.html', context)

def item_page(request):
    form = SingUpModelForm(request.POST or None)
    if form.is_valid():
         obj = form.save(commit=False)
         form.save()
    form = SingUpModelForm()


    context = { 
        "form": form, 
    }
    return render(request, 'item.html', context)


# def index_page(request):
#     form = SignUpForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password1")
#         form.save()
#         new_user = authenticate(username=username, password=password)
#         if new_user is not None:
#             login(request, new_user)
#             return redirect("main/")


#     context = {
#         "title": "registration", 
#         "form": form, 
#     }
#     return render(request, 'index.html', context)

def shop_page(requset):
    return render(requset, 'shop.html')
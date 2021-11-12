from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

from accounts.models import Account
from . forms import RegistrationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()

            messages.success(request, 'Registration Successful!')

            return redirect('register' )
        
    else:
        form = RegistrationForm()
    
    context={
        'form':form,
    }
    return render(request, "accounts/register.html", context)

def login(request):
    return render(request, "accounts/login.html")

def logout(request):
    return

def confirm_registration(request):
    #return render(request, 'petrol/registration_success.html')
    pass
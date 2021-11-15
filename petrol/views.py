from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from . forms import RegistrationForm
from . models import Users


def index(request):
    # try:
        # registered_users=Users.objects.get()
        # if request.method == 'GET':
        #     registration_form = RegistrationForm()
            
        # else:
        #     registration_form = RegistrationForm(request.POST)
        #     if registration_form.is_valid():
        #         registration_form.save()
        #         return redirect('confirm-registration')

        # return render(request,"petrol/index.html",{
        #     'registered_users':registered_users,
        #     'form': registration_form
        # })
        # if request.method =='POST':
        #     registration_form = RegistrationForm()
        #     if registration_form.is_valid():
        #         username = registration_form.cleaned_data['username']
        #         email= registration_form.cleaned_data['email']
        #         password = registration_form.cleaned_data['password']
        #         user= Users.objects.create_user(
        #             username=username, email=email, password=password
        #         )
        #         user.save()
        # else:
        #     registration_form =  RegistrationForm()
        # context = {
        #     'registration_form': registration_form,
        # }
        return redirect( "petrol/index.html")
       

    # except Exception as exe:
    #     print(exe)
    #     return render(request, "404.html")
    #     # repsonse_data = render_to_string("404.html")
        # return HttpResponseNotFound(repsonse_data)

def confirm_registration(request):
    # return render(request, 'petrol/registration_success.html')
    pass

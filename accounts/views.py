from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from accounts.models import Account
from . forms import RegistrationForm
from django.contrib import messages

#verification
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage



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

            #User Activation
            current_site    = get_current_site(request)
            mail_subject    = "Please activate your account"
            message         = render_to_string('accounts/account_verification_email.html',{
                                'user'   : user,
                                'domain' : current_site,
                                'uid'    : urlsafe_base64_encode(force_bytes(user.pk)),
                                'token'  : default_token_generator.make_token(user), 
                                        })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()


            # messages.success(request, 'Thank you for registering with us. We have sent you a verification email to your email address. Please verify it.')

            return redirect('/accounts/login/?command=verification&email='+ email )
        
    else:
        form = RegistrationForm()
    
    context={
        'form':form,
    }
    return render(request, "accounts/register.html", context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password=request.POST['password']

        user  = auth.authenticate(email=email, password=password)
        print(email, password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request , 'You are now logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Login credentials')
            return redirect('login')

    return render(request, "accounts/login.html")


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('login')

def confirm_registration(request):
    return render(request, 'accounts/registration_success.html')
    

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, "Invalid activation link")
        return redirect('register')


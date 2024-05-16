from django.shortcuts import render, redirect
from app2.forms import UserForm, UserProfileForm

#import for authentication
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index1(request):
    return render(request, 'app2/html/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Hash the password
            user.save()

            profile = profile_form.save(commit=False)  # Delay saving the profile model
            profile.user = user  # Set the user attribute

            if 'profile_pic' in request.FILES:  # Check if a profile picture is uploaded
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()  # Save the profile model
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()  # Initialize an empty UserForm
        profile_form = UserProfileForm()  # Initialize an empty UserProfileForm

    return render(request, 'app2/html/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)  # directly auth user

        if user:
            if user.is_active:
                login(request, user) # if login sredirect to requred page
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return render(request, 'app2/html/login.html', {'not_active': 'Account disable..! contact admin'})
        
        else:
            return render(request, 'app2/html/login.html', {'not_registered': 'Invalid login details.'})
        
    else:
        return render(request, 'app2/html/login.html',{})
    

# only users who log in can logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app2:user_login'))


@login_required
def special(request):
    return HttpResponse("You are logged in")


            
        
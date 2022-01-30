from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from .forms import LoginForm
from .forms import MoviesChoiceForm
from .create_request import create_request

# Create your views here.
# описание функций для каждой страницы

def index(request):
    return render(request, "index.html")

def registration(request):
    return render(request, "account/signin.html")


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'account/successful_auth.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return render(request, 'account/invalid_login.html')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

from .forms import LoginForm, UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'account/signin.html', {'user_form': user_form})


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {'section': 'dashboard'})

def logout_view(request):
    logout(request)
    return render(request, "account/logged_out.html")

def password_change(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

    else:
        user_form = UserRegistrationForm()
        return render(request, 'account/password_change_form.html', {'user_form': user_form})
    return render(request, "account/password_change_form.html")

def password_change_done(request):
    return render(request, "account/password_change_done.html")

def choose_movies(request):
    form = MoviesChoiceForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            temp = form.cleaned_data.get("selected_genres")
            print(temp)
            return render(request, 'movies_results.html', {'temp': create_request(temp)})
    else:
        form = MoviesChoiceForm()
    return render(request, 'movies_choice.html', {'form': form})

# def movies_results(request):


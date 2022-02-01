from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from .forms import LoginForm
from .forms import MoviesChoiceForm
from .create_request import create_request
from .forms import LoginForm, UserRegistrationForm


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
            action = form.cleaned_data.get('action')
            adventure = form.cleaned_data.get('action')
            animation = form.cleaned_data.get('action')
            biography = form.cleaned_data.get('biography')
            comedy = form.cleaned_data.get('comedy')
            crime = form.cleaned_data.get('crime')
            documentary = form.cleaned_data.get('documentary')
            drama = form.cleaned_data.get('drama')
            family = form.cleaned_data.get('family')
            fantasy = form.cleaned_data.get('fantasy')
            film_noir = form.cleaned_data.get('film_noir')
            history = form.cleaned_data.get('history')
            horror = form.cleaned_data.get('horror')
            musical = form.cleaned_data.get('musical')
            mystery = form.cleaned_data.get('mystery')
            romance = form.cleaned_data.get('romance')
            sci_fi = form.cleaned_data.get('sci_fi')
            sport = form.cleaned_data.get('sport')
            thriller = form.cleaned_data.get('thriller')
            western = form.cleaned_data.get('western')

            genres = {biography: 'biography', comedy: 'comedy', crime: 'crime', documentary: 'documentary',
                      drama: 'drama', family: 'family', fantasy: 'fantasy', film_noir: 'film-noir', history: 'history',
                      horror: 'horror', musical: 'musical', mystery: 'mystery', romance: 'romance', sci_fi: 'sci-fi',
                      sport: 'sport', thriller: 'thriller', western: 'western', action: 'action',
                      adventure: 'adventure', animation: 'animation'}

            selected_genres = [genres[item] for item in genres if item]
            return render(request, 'movies_results.html', {'temp': create_request(selected_genres)})
    else:
        form = MoviesChoiceForm()
    return render(request, 'movies_choice.html', {'form': form})


def tests(request):
    form = MoviesChoiceForm()
    return render(request, 'testing.html', {'form': form})
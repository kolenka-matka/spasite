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


def choose_movies(request):  # !!!!!!!!!!!!!!!!!!!!!!! ФИЛЬМЫ
    form = MoviesChoiceForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ЖАНРЫ !!!!!!!!!!!!!
            action = ('action', form.cleaned_data.get('action'))
            adventure = ('adventure', form.cleaned_data.get('action'))
            animation = ('animation', form.cleaned_data.get('action'))
            biography = ('biography', form.cleaned_data.get('biography'))
            comedy = ('comedy', form.cleaned_data.get('comedy'))
            crime = ('crime', form.cleaned_data.get('crime'))
            documentary = ('documentary', form.cleaned_data.get('documentary'))
            drama = ('drama', form.cleaned_data.get('drama'))
            family = ('family', form.cleaned_data.get('family'))
            fantasy = ('fantasy', form.cleaned_data.get('fantasy'))
            film_noir = ('film_noir', form.cleaned_data.get('noir'))
            history = ('history', form.cleaned_data.get('history'))
            horror = ('horror', form.cleaned_data.get('horror'))
            musical = ('musical', form.cleaned_data.get('musical'))
            mystery = ('mystery', form.cleaned_data.get('mystery'))
            romance = ('romance', form.cleaned_data.get('romance'))
            sci_fi = ('sci_fi', form.cleaned_data.get('sci_fi'))
            sport = ('sport', form.cleaned_data.get('sport'))
            thriller = ('thriller', form.cleaned_data.get('thriller'))
            western = ('western', form.cleaned_data.get('western'))

            genres = [adventure, animation, biography, comedy, crime, documentary, drama, family,
                      fantasy, film_noir, history, horror, musical, mystery, romance, sci_fi, sport, thriller, western]
            selection = str()
            selected_genres = [item[0].replace('_', '-') for item in genres if item[1] == True]
            print(selected_genres)
            if selected_genres:
                selection += 'вы выбрали следующие жанры: ' + ', '.join(selected_genres)
            countries = form.cleaned_data.get('country')
            if countries:
                selection += '\nвы выбрали следующие страны: ' + ', '.join(countries)


            return render(request, 'search/movies_results.html', {'temp': create_request(selected_genres, countries), 'selection': selection})
    else:
        form = MoviesChoiceForm()
    return render(request, 'search/movies_choice.html', {'form': form})


def tests(request):
    form = MoviesChoiceForm()
    return render(request, 'testing.html', {'form': form})
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from .create_request import create_request
from .forms import LoginForm, UserRegistrationForm, MoviesChoiceForm
from dal import autocomplete
from .lists import actors_list



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
            adventure = ('adventure', form.cleaned_data.get('adventure'))
            animation = ('animation', form.cleaned_data.get('animation'))
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

            genres = [adventure, animation, biography, comedy, crime, documentary, drama, family, action,
                      fantasy, film_noir, history, horror, musical, mystery, romance, sci_fi, sport, thriller, western]
            selection = list()
            selected_genres = [item[0].replace('_', '-') for item in genres if item[1] == True]
            if selected_genres:
                selection.append('вы выбрали следующие жанры: ' + ', '.join(selected_genres))
            countries = form.cleaned_data.get('country')
            if countries:
                selection.append('вы выбрали следующие страны: ' + ', '.join(countries))

            actors = form.cleaned_data.get('actors')

            ratings = form.cleaned_data.get('ratings')
            if ratings:
                selection.append('вы выбрали рейтинги ' + ', '.join(ratings))

            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ИСКЛЮЧИТЬ ЖАНРЫ !!!!!!!!!!!!!
            exclude_action = ('action', form.cleaned_data.get('exclude_action'))
            exclude_adventure = ('adventure', form.cleaned_data.get('exclude_adventure'))
            exclude_animation = ('animation', form.cleaned_data.get('exclude_animation'))
            exclude_biography = ('biography', form.cleaned_data.get('exclude_biography'))
            exclude_comedy = ('comedy', form.cleaned_data.get('exclude_comedy'))
            exclude_crime = ('crime', form.cleaned_data.get('exclude_crime'))
            exclude_documentary = ('documentary', form.cleaned_data.get('exclude_documentary'))
            exclude_drama = ('drama', form.cleaned_data.get('exclude_drama'))
            exclude_family = ('family', form.cleaned_data.get('exclude_family'))
            exclude_fantasy = ('fantasy', form.cleaned_data.get('exclude_fantasy'))
            exclude_film_noir = ('film_noir', form.cleaned_data.get('exclude_noir'))
            exclude_history = ('history', form.cleaned_data.get('exclude_history'))
            exclude_horror = ('horror', form.cleaned_data.get('exclude_horror'))
            exclude_musical = ('musical', form.cleaned_data.get('exclude_musical'))
            exclude_mystery = ('mystery', form.cleaned_data.get('exclude_mystery'))
            exclude_romance = ('romance', form.cleaned_data.get('exclude_romance'))
            exclude_sci_fi = ('sci_fi', form.cleaned_data.get('exclude_sci_fi'))
            exclude_sport = ('sport', form.cleaned_data.get('exclude_sport'))
            exclude_thriller = ('thriller', form.cleaned_data.get('exclude_thriller'))
            exclude_western = ('western', form.cleaned_data.get('exclude_western'))

            exclude_genres = {exclude_adventure, exclude_animation, exclude_biography, exclude_comedy, exclude_crime, exclude_documentary,
                              exclude_drama, exclude_family, exclude_action, fantasy, exclude_film_noir, exclude_history, exclude_horror, exclude_fantasy,
                              exclude_musical, exclude_mystery, exclude_romance, exclude_sci_fi, exclude_sport, exclude_thriller, exclude_western}
            exclude_genres = {item[0].replace('_', '-') for item in exclude_genres if item[1] == True}
            if exclude_genres:
                selection.append('вы исключили следующие жанры: ' + ', '.join(exclude_genres))

            plot = form.cleaned_data.get('plot')

            # ---------------------------------- КАТЕГОРИЯ ПОИСКА ----------------------------------
            tv_series = ('tv_series', form.cleaned_data.get('tv_series'))
            movies = ('movies', form.cleaned_data.get('movies'))
            games = ('games', form.cleaned_data.get('games'))
            books = ('books', form.cleaned_data.get('books'))
            podcasts = ('podcasts', form.cleaned_data.get('podcasts'))

            categories = [tv_series, movies, games, books, podcasts]
            selected_category = [item[0].replace('_', '-') for item in categories if item[1] == True]

            if selected_category:
                selection.append('вы выбрали следующую категорию: ' + ', '.join(selected_category))
            # ---------------------------------- КАТЕГОРИЯ ПОИСКА ----------------------------------



            return render(request, 'search/movies_results.html',
                          {'temp': create_request(selected_category, selected_genres, countries, exclude_genres, plot, ratings, actors), 'selection': selection})
    else:
        form = MoviesChoiceForm()
    return render(request, 'search/movies_choice.html', {'form': form})


def tests(request):
    form = MoviesChoiceForm()
    return render(request, 'testing.html', {'form': form})
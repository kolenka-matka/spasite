from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from .create_request import create_request, books_help, choose_games, join_results
from .forms import LoginForm, UserRegistrationForm, MoviesChoiceForm
from dal import autocomplete
from .lists import hren_to_tag



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
            selection = list()
            result = list()
            # ---------------------------------- КАТЕГОРИЯ ПОИСКА ----------------------------------
            tv_series = ('tv_series', form.cleaned_data.get('tv_series'))
            movies = ('movies', form.cleaned_data.get('movies'))
            games = ('games', form.cleaned_data.get('games'))
            books = ('books', form.cleaned_data.get('books'))
            podcasts = ('podcasts', form.cleaned_data.get('podcasts'))

            categories = [tv_series, movies, games, books, podcasts]
            selected_category = [item[0] for item in categories if item[1] == True]

            if selected_category:
                selection.append('вы выбрали следующие категории: ' + ', '.join(selected_category))
            # ---------------------------------- КАТЕГОРИЯ ПОИСКА ----------------------------------

            # !!!!!!!!!!!!!!!!!!!!!!! ФИЛЬМЫ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if movies[1] or tv_series[1] or podcasts[1]:
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

                selected_genres = [item[0].replace('_', '-') for item in genres if item[1] == True]
                if selected_genres:
                    selection.append('вы выбрали следующие жанры для фильмов: ' + ', '.join(selected_genres))
                countries = form.cleaned_data.get('country')
                if countries:
                    selection.append('вы выбрали следующие страны-производители для фильмов: ' + ', '.join(countries))

                actors = form.cleaned_data.get('actors')

                ratings = form.cleaned_data.get('ratings')
                if ratings:
                    selection.append('в категории "фильмы" вы выбрали рейтинги ' + ', '.join(ratings))

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

                exclude_genres = {exclude_adventure, exclude_animation, exclude_biography, exclude_comedy, exclude_crime,
                                  exclude_documentary,
                                  exclude_drama, exclude_family, exclude_action, fantasy, exclude_film_noir,
                                  exclude_history, exclude_horror, exclude_fantasy,
                                  exclude_musical, exclude_mystery, exclude_romance, exclude_sci_fi, exclude_sport,
                                  exclude_thriller, exclude_western}
                exclude_genres = {item[0].replace('_', '-') for item in exclude_genres if item[1] == True}
                if exclude_genres:
                    selection.append('для фильмов вы исключили следующие жанры: ' + ', '.join(exclude_genres))

                plot = form.cleaned_data.get('plot')
                result.append(create_request(selected_category, selected_genres, countries,
                                                  exclude_genres, plot, ratings, actors))


            # КНИГИ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if books[1]:
                fantasy_book = ('/knigi-fentezi/', form.cleaned_data.get('fantasy_book'))
                detective_book = ('/knigi-detektivy/', form.cleaned_data.get('detective_book'))
                science_fiction_book = ('/knigi-fantastika/', form.cleaned_data.get('science_fiction_book'))
                romance_book = ('/knigi-lubovnye-romany/', form.cleaned_data.get('romance_book'))
                adventure_book = ('/knigi-priklucheniya/', form.cleaned_data.get('adventure_book'))
                horror_book = ('/knigi-uzhasy-mistika/', form.cleaned_data.get('horror_book'))
                manga_book = ('/komiksy-manga/', form.cleaned_data.get('manga_book'))
                modern_prose_book = ('/knigi-sovremennaya-proza/', form.cleaned_data.get('modern_prose_book'))
                classic_book = ('/klassicheskaya-literatura/', form.cleaned_data.get('classic_book'))
                poetry_book = ('/sereznoe-chtenie/ctihi-poeziya/', form.cleaned_data.get('poetry_book'))
                biography_book = ('/knigi-publicistika/biografii-memuary/', form.cleaned_data.get('biography_book'))
                history_book = ('/istoriya/', form.cleaned_data.get('history_book'))
                war_book = ('/knigi-sovremennaya-proza/knigi_o_voyne/', form.cleaned_data.get('war_book'))
                business_book = ('/biznes-knigi/o-biznese-populyarno/', form.cleaned_data.get('business_book'))
                study_book = ('/znaniya-navyki/uchebnaya-nauchnaya-literatura/', form.cleaned_data.get('study_book'))
                esoteric_book = ('/knigi-ezoterika/', form.cleaned_data.get('esoteric_book'))
                dictionary_book = ('/spravochniki-slovari/', form.cleaned_data.get('dictionary_book'))
                languages_book = (
                '/znaniya-navyki/uchebnaya-nauchnaya-literatura/gumanitarnye-obschestvennye-nauki/izuchenie-yazykov/',
                form.cleaned_data.get('languages_book'))
                art_book = ('/knigi-iskusstvo/', form.cleaned_data.get('art_book'))
                maps_book = ('/spravochniki-slovari/putevoditeli/', form.cleaned_data.get('maps_book'))
                psychology_book = ('/knigi-psihologiya/', form.cleaned_data.get('psychology_book'))
                sport_book = ('/sport-zdorove-krasota/sport/', form.cleaned_data.get('sport_book'))
                cooking_book = ('/knigi-dom-semya/kulinariya/', form.cleaned_data.get('cooking_book'))
                kids_book = ('/detskie-knigi/', form.cleaned_data.get('kids_book'))
                fairytales_book = ('/detskie-knigi/skazki/', form.cleaned_data.get('fairytales_book'))
                student_book = ('/detskie-knigi/uchebnaya-literatura/', form.cleaned_data.get('student_book'))
                school_book = ('/shkolnye-uchebniki/', form.cleaned_data.get('school_book'))

                books = [fantasy_book, detective_book, science_fiction_book, romance_book, adventure_book, horror_book,
                         manga_book,
                         modern_prose_book, classic_book, poetry_book, biography_book, history_book, war_book,
                         business_book,
                         study_book, esoteric_book, dictionary_book, languages_book, psychology_book, maps_book, art_book,
                         sport_book,
                         cooking_book, kids_book, fairytales_book, student_book, school_book]

                selected_books = [item[0].replace('_', '-') for item in books if item[1] == True]
                if selected_books:
                    selection.append('вы выбрали следующие жанры для книг: ' + ', '.join(selected_books))
                    result.append(books_help(selected_books))



            # ------------------------ ИГРЫ --------------------------------
            if games[1]:
                games_indie = ('492', form.cleaned_data.get('games_indie'))
                games_action = ('19', form.cleaned_data.get('games_action'))
                games_adventure = ('21', form.cleaned_data.get('games_adventure'))
                games_casual = ('597', form.cleaned_data.get('games_casual'))
                games_simulation = ('599', form.cleaned_data.get('games_simulation'))
                games_rpg = ('122', form.cleaned_data.get('games_rpg'))
                games_strategy = ('9', form.cleaned_data.get('games_strategy'))
                games_singleplayer = ('4182', form.cleaned_data.get('games_singleplayer'))
                games_early_access = ('493', form.cleaned_data.get('games_early_access'))
                games_free_to_play = ('113', form.cleaned_data.get('games_free_to_play'))
                games_twod = ('3871', form.cleaned_data.get('games_twod'))
                games_atmospheric = ('4166', form.cleaned_data.get('games_atmospheric'))
                games_threed = ('4191', form.cleaned_data.get('games_threed'))
                games_massively_multiplayer = ('128', form.cleaned_data.get('games_massively_multiplayer'))
                games_multiplayer = ('3859', form.cleaned_data.get('games_multiplayer'))
                games_genres = [games_indie, games_action, games_adventure, games_casual, games_simulation, games_rpg, games_strategy, games_singleplayer, games_early_access, games_free_to_play, games_twod, games_atmospheric, games_threed, games_massively_multiplayer, games_multiplayer]
                games_other = form.cleaned_data.get('games_other')
                games_selected_genres = games_other + [item[0].replace('_', '-') for item in games_genres if item[1] == True]
                if games_selected_genres:
                    selection.append('вы выбрали следующие жанры для игр: ' + ', '.join([hren_to_tag[item] for item in games_selected_genres]))

                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ИСКЛЮЧИТЬ ЖАНРЫ !!!!!!!!!!!!!
                exclude_games_indie = ('492', form.cleaned_data.get('exclude_games_indie'))
                exclude_games_action = ('19', form.cleaned_data.get('exclude_games_action'))
                exclude_games_adventure = ('21', form.cleaned_data.get('exclude_games_adventure'))
                exclude_games_casual = ('597', form.cleaned_data.get('exclude_games_casual'))
                exclude_games_simulation = ('599', form.cleaned_data.get('exclude_games_simulation'))
                exclude_games_rpg = ('122', form.cleaned_data.get('exclude_games_rpg'))
                exclude_games_strategy = ('9', form.cleaned_data.get('exclude_games_strategy'))
                exclude_games_singleplayer = ('4182', form.cleaned_data.get('exclude_games_singleplayer'))
                exclude_games_early_access = ('493', form.cleaned_data.get('exclude_games_early_access'))
                exclude_games_free_to_play = ('113', form.cleaned_data.get('exclude_games_free_to_play'))
                exclude_games_twod = ('3871', form.cleaned_data.get('exclude_games_twod'))
                exclude_games_atmospheric = ('4166', form.cleaned_data.get('exclude_games_atmospheric'))
                exclude_games_threed = ('4191', form.cleaned_data.get('exclude_games_threed'))
                exclude_games_massively_multiplayer = ('128', form.cleaned_data.get('exclude_games_massively_multiplayer'))
                exclude_games_multiplayer = ('3859', form.cleaned_data.get('exclude_games_multiplayer'))
                exclude_games_other = form.cleaned_data.get('exclude_games_other')
                exclude_games_genres = [exclude_games_indie, exclude_games_action, exclude_games_adventure, exclude_games_casual, exclude_games_simulation, exclude_games_rpg, exclude_games_strategy, exclude_games_singleplayer, exclude_games_early_access, exclude_games_free_to_play, exclude_games_twod, exclude_games_atmospheric, exclude_games_threed, exclude_games_massively_multiplayer, exclude_games_multiplayer]
                exclude_games_genres = [item[0] for item in exclude_games_genres if item[1] == True]
                exclude_games_genres = exclude_games_other + exclude_games_genres
                if exclude_games_genres:
                    selection.append('вы исключили следующие жанры для игр: ' + ', '.join([hren_to_tag[item] for item in exclude_games_genres]))

                games_players = form.cleaned_data.get('games_players')
                result.append(choose_games(games_selected_genres, exclude_games_genres, games_players))




            return render(request, 'search/movies_results.html',
                          {'temp': join_results(*result), 'selection': selection})
    else:
        form = MoviesChoiceForm()
    return render(request, 'search/movies_choice.html', {'form': form})


def tests(request):
    form = MoviesChoiceForm()
    return render(request, 'testing.html', {'form': form})

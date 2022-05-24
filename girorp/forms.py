from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NonOrdinaryUser
from django.contrib.auth.models import User
from .lists import ratings_help_text, actors_list, countries_list, games_tag_list
# import cchardet

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = NonOrdinaryUser
        # fields = ('username', 'email', 'password', 'password_confirm', 'admin_key')
        fields = ('username', 'email', 'password')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = NonOrdinaryUser
        fields = ('username', 'email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = NonOrdinaryUser
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class MoviesChoiceForm(forms.Form):
    action = forms.BooleanField(label='экшн', required=False)
    adventure = forms.BooleanField(label='приключения', required=False)
    animation = forms.BooleanField(label='мультфильм', required=False)
    biography = forms.BooleanField(label='биография', required=False)
    comedy = forms.BooleanField(label='комедия', required=False)
    crime = forms.BooleanField(label='криминал', required=False)
    documentary = forms.BooleanField(label='документальный фильм', required=False)
    drama = forms.BooleanField(label='драма', required=False)
    family = forms.BooleanField(label='семейное кино', required=False)
    fantasy = forms.BooleanField(label='фэнтези', required=False)
    film_noir = forms.BooleanField(label='нуар', required=False)
    history = forms.BooleanField(label='исторический фильм', required=False)
    horror = forms.BooleanField(label='ужасы', required=False)
    musical = forms.BooleanField(label='мюзикл', required=False)
    mystery = forms.BooleanField(label='детектив', required=False)
    romance = forms.BooleanField(label='романтика', required=False)
    sci_fi = forms.BooleanField(label='научная фантастика', required=False)
    sport = forms.BooleanField(label='о спорте', required=False)
    thriller = forms.BooleanField(label='триллер', required=False)
    western = forms.BooleanField(label='вестерн', required=False)

    country = forms.MultipleChoiceField(choices=countries_list,
                                required=False, label='выберите страну-производителя')

    actors = forms.MultipleChoiceField(choices=actors_list, required=False, label='выберите актера')

    plot = forms.CharField(label='сюжет', required=False, help_text='<i>введите здесь ключевые слова, которые могут встретиться в описании сюжета фильма. слова можно вводить на русском или английском языке. в результаты поиска войдут только фильмы, в описании которых присутствуют все введенные слова.</i>')

    ratings = forms.MultipleChoiceField(choices=[
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC', 'NC')
    ], label='рейтинги', required=False, help_text=ratings_help_text)

    exclude_action = forms.BooleanField(label='исключить: экшн', required=False)
    exclude_adventure = forms.BooleanField(label='исключить: приключения', required=False)
    exclude_animation = forms.BooleanField(label='исключить: мультфильм', required=False)
    exclude_biography = forms.BooleanField(label='исключить: биография', required=False)
    exclude_comedy = forms.BooleanField(label='исключить: комедия', required=False)
    exclude_crime = forms.BooleanField(label='исключить: криминал', required=False)
    exclude_documentary = forms.BooleanField(label='исключить: документальный фильм', required=False)
    exclude_drama = forms.BooleanField(label='исключить: драма', required=False)
    exclude_family = forms.BooleanField(label='исключить: семейное кино', required=False)
    exclude_fantasy = forms.BooleanField(label='исключить: фэнтези', required=False)
    exclude_film_noir = forms.BooleanField(label='исключить: нуар', required=False)
    exclude_history = forms.BooleanField(label='исключить: исторический фильм', required=False)
    exclude_horror = forms.BooleanField(label='исключить: ужасы', required=False)
    exclude_musical = forms.BooleanField(label='исключить: мюзикл', required=False)
    exclude_mystery = forms.BooleanField(label='исключить: детектив', required=False)
    exclude_romance = forms.BooleanField(label='исключить: романтика', required=False)
    exclude_sci_fi = forms.BooleanField(label='исключить: научная фантастика', required=False)
    exclude_sport = forms.BooleanField(label='исключить: о спорте', required=False)
    exclude_thriller = forms.BooleanField(label='исключить: триллер', required=False)
    exclude_western = forms.BooleanField(label='исключить: вестерн', required=False)

    russian = forms.BooleanField(label='книги только на русском языке', required=False)
    keywords = forms.CharField(label='введите здесь ключевые слова', required=False)
    exclude_keywords = forms.CharField(label='убрать из результатов поиска книги со словами', required=False)
    author = forms.CharField(label='отобразить книги, написанные', required=False)
    date_from = forms.DateField(label='c', required=False)
    date_to = forms.DateField(label='до', required=False)


    tv_series = forms.BooleanField(label='сериалы', required=False)
    movies = forms.BooleanField(label='фильмы', required=False)
    games = forms.BooleanField(label='игры', required=False)
    books = forms.BooleanField(label='книги', required=False)
    podcasts = forms.BooleanField(label='подкасты', required=False)

    # test = forms.BooleanField(label='ПОМОГИТЕ', required=False)


    fantasy_book = forms.BooleanField(label='Фэнтези', required=False)
    detective_book = forms.BooleanField(label='Детективы', required=False)
    science_fiction_book = forms.BooleanField(label='Фантастика', required=False)
    romance_book = forms.BooleanField(label='Любовные романы', required=False)
    adventure_book = forms.BooleanField(label='Приключения', required=False)
    horror_book = forms.BooleanField(label='Ужасы/мистика', required=False)
    manga_book = forms.BooleanField(label='Комиксы/манга', required=False)
    modern_prose_book = forms.BooleanField(label='Современная проза', required=False)
    classic_book = forms.BooleanField(label='Классическая литература', required=False)
    poetry_book = forms.BooleanField(label='Поэзия', required=False)
    biography_book = forms.BooleanField(label='Биография и мемуары', required=False)
    history_book = forms.BooleanField(label='История', required=False)
    war_book = forms.BooleanField(label='О войне', required=False)
    business_book = forms.BooleanField(label='Бизнес', required=False)
    study_book = forms.BooleanField(label='Учебная и научная литература', required=False)
    esoteric_book = forms.BooleanField(label='Эзотерика', required=False)
    dictionary_book = forms.BooleanField(label='Словари', required=False)
    languages_book = forms.BooleanField(label='Изучение языков', required=False)
    art_book = forms.BooleanField(label='Культура и искусство', required=False)
    maps_book = forms.BooleanField(label='Путеводители', required=False)
    psychology_book = forms.BooleanField(label='Психология', required=False)
    sport_book = forms.BooleanField(label='Спорт', required=False)
    cooking_book = forms.BooleanField(label='Кулинария', required=False)
    kids_book = forms.BooleanField(label='Детские книги', required=False)
    fairytales_book = forms.BooleanField(label='Сказки', required=False)
    student_book = forms.BooleanField(label='Школьные учебники', required=False)
    school_book = forms.BooleanField(label='Учебная и научная литература', required=False)

    # ИГРЫ -----------------------------------------------
    games_indie = forms.BooleanField(label='Инди', required=False)
    games_action = forms.BooleanField(label='Экшен', required=False)
    games_adventure = forms.BooleanField(label='Приключение', required=False)
    games_casual = forms.BooleanField(label='Казуальная игра', required=False)
    games_simulation = forms.BooleanField(label='Симулятор', required=False)
    games_rpg = forms.BooleanField(label='Ролевая игра', required=False)
    games_strategy = forms.BooleanField(label='Стратегия', required=False)
    games_singleplayer = forms.BooleanField(label='Для одного игрока', required=False)
    games_early_access = forms.BooleanField(label='Ранний доступ', required=False)
    games_free_to_play = forms.BooleanField(label='Бесплатная игра', required=False)
    games_twod = forms.BooleanField(label='2D', required=False)
    games_atmospheric = forms.BooleanField(label='Атмосферная', required=False)
    games_threed = forms.BooleanField(label='3D', required=False)
    games_massively_multiplayer = forms.BooleanField(label='ММО', required=False)
    games_multiplayer = forms.BooleanField(label='Для нескольких игроков', required=False)
    games_story_rich = forms.BooleanField(label='Глубокий сюжет', required=False)
    games_other = forms.MultipleChoiceField(choices=games_tag_list, required=False, label='выберите другие жанры:')

    exclude_games_indie = forms.BooleanField(label='Инди', required=False)
    exclude_games_action = forms.BooleanField(label='Экшен', required=False)
    exclude_games_adventure = forms.BooleanField(label='Приключение', required=False)
    exclude_games_casual = forms.BooleanField(label='Казуальная игра', required=False)
    exclude_games_simulation = forms.BooleanField(label='Симулятор', required=False)
    exclude_games_rpg = forms.BooleanField(label='Ролевая игра', required=False)
    exclude_games_strategy = forms.BooleanField(label='Стратегия', required=False)
    exclude_games_singleplayer = forms.BooleanField(label='Для одного игрока', required=False)
    exclude_games_early_access = forms.BooleanField(label='Ранний доступ', required=False)
    exclude_games_free_to_play = forms.BooleanField(label='Бесплатная игра', required=False)
    exclude_games_twod = forms.BooleanField(label='2D', required=False)
    exclude_games_atmospheric = forms.BooleanField(label='Атмосферная', required=False)
    exclude_games_threed = forms.BooleanField(label='3D', required=False)
    exclude_games_massively_multiplayer = forms.BooleanField(label='ММО', required=False)
    exclude_games_multiplayer = forms.BooleanField(label='Для нескольких игроков', required=False)
    exclude_games_story_rich = forms.BooleanField(label='Глубокий сюжет', required=False)
    exclude_games_other = forms.MultipleChoiceField(choices=games_tag_list, required=False, label='исключить другие жанры:')

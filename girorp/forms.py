from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NonOrdinaryUser
from django.contrib.auth.models import User
from .lists import ratings_help_text, actors_list, countries_list


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
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

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

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NonOrdinaryUser
from django.contrib.auth.models import User


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

    action = forms.BooleanField(label='экшн', help_text='action', required=False)
    adventure = forms.BooleanField(label='приключения', help_text='adventure', required=False)
    animation = forms.BooleanField(label='мультфильм', help_text='animation', required=False)
    biography = forms.BooleanField(label='биография', help_text='biography', required=False)
    comedy = forms.BooleanField(label='комедия', help_text='comedy', required=False)
    crime = forms.BooleanField(label='криминал', help_text='crime', required=False)
    documentary = forms.BooleanField(label='документальный фильм', help_text='documentary', required=False)
    drama = forms.BooleanField(label='драма', help_text='drama', required=False)
    family = forms.BooleanField(label='семейное кино', help_text='family', required=False)
    fantasy = forms.BooleanField(label='фэнтези', help_text='fantasy', required=False)
    film_noir = forms.BooleanField(label='нуар', help_text='film-noir', required=False)
    history = forms.BooleanField(label='исторический фильм', help_text='history', required=False)
    horror = forms.BooleanField(label='ужасы', help_text='horror', required=False)
    musical = forms.BooleanField(label='мюзикл', help_text='musical', required=False)
    mystery = forms.BooleanField(label='детектив', help_text='mystery', required=False)
    romance = forms.BooleanField(label='романтика', help_text='romance', required=False)
    sci_fi = forms.BooleanField(label='научная фантастика', help_text='sci-fi', required=False)
    sport = forms.BooleanField(label='о спорте', help_text='sport', required=False)
    thriller = forms.BooleanField(label='триллер', help_text='thriller', required=False)
    western = forms.BooleanField(label='вестерн', help_text='western', required=False)
    genres = [action, adventure,animation, biography,comedy, crime,documentary,drama,family,fantasy,film_noir,
              history,horror,musical,mystery,romance,sci_fi,sport,thriller,western]

    selected_genres = [item.help_text for item in genres if item is not None]
    print(genres)


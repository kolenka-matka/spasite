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

    country = forms.MultipleChoiceField(choices=[('af', 'Afghanistan'), ('ax', 'Åland Islands'), ('al', 'Albania'), ('dz', 'Algeria'), ('as', 'American Samoa'), ('ad', 'Andorra'), ('ao', 'Angola'), ('ai', 'Anguilla'), ('aq', 'Antarctica'), ('ag', 'Antigua and Barbuda'), ('ar', 'Argentina'), ('am', 'Armenia'), ('aw', 'Aruba'), ('au', 'Australia'), ('at', 'Austria'), ('az', 'Azerbaijan'), ('bs', 'Bahamas'), ('bh', 'Bahrain'), ('bd', 'Bangladesh'), ('bb', 'Barbados'), ('by', 'Belarus'), ('be', 'Belgium'), ('bz', 'Belize'), ('bj', 'Benin'), ('bm', 'Bermuda'), ('bt', 'Bhutan'), ('bo', 'Bolivia'), ('bq', 'Bonaire, Sint Eustatius and Saba'), ('ba', 'Bosnia and Herzegovina'), ('bw', 'Botswana'), ('bv', 'Bouvet Island'), ('br', 'Brazil'), ('io', 'British Indian Ocean Territory'), ('vg', 'British Virgin Islands'), ('bn', 'Brunei Darussalam'), ('bg', 'Bulgaria'), ('bf', 'Burkina Faso'), ('bumm', 'Burma'), ('bi', 'Burundi'), ('kh', 'Cambodia'), ('cm', 'Cameroon'), ('ca', 'Canada'), ('cv', 'Cape Verde'), ('ky', 'Cayman Islands'), ('cf', 'Central African Republic'), ('td', 'Chad'), ('cl', 'Chile'), ('cn', 'China'), ('cx', 'Christmas Island'), ('cc', 'Cocos (Keeling) Islands'), ('co', 'Colombia'), ('km', 'Comoros'), ('cg', 'Congo'), ('ck', 'Cook Islands'), ('cr', 'Costa Rica'), ('ci', "Côte d'Ivoire"), ('hr', 'Croatia'), ('cu', 'Cuba'), ('cy', 'Cyprus'), ('cz', 'Czech Republic'), ('cshh', 'Czechoslovakia'), ('cd', 'Democratic Republic of the Congo'), ('dk', 'Denmark'), ('dj', 'Djibouti'), ('dm', 'Dominica'), ('do', 'Dominican Republic'), ('ddde', 'East Germany'), ('ec', 'Ecuador'), ('eg', 'Egypt'), ('sv', 'El Salvador'), ('gq', 'Equatorial Guinea'), ('er', 'Eritrea'), ('ee', 'Estonia'), ('et', 'Ethiopia'), ('fk', 'Falkland Islands'), ('fo', 'Faroe Islands'), ('yucs', 'Federal Republic of Yugoslavia'), ('fm', 'Federated States of Micronesia'), ('fj', 'Fiji'), ('fi', 'Finland'), ('fr', 'France'), ('gf', 'French Guiana'), ('pf', 'French Polynesia'), ('tf', 'French Southern Territories'), ('ga', 'Gabon'), ('gm', 'Gambia'), ('ge', 'Georgia'), ('de', 'Germany'), ('gh', 'Ghana'), ('gi', 'Gibraltar'), ('gr', 'Greece'), ('gl', 'Greenland'), ('gd', 'Grenada'), ('gp', 'Guadeloupe'), ('gu', 'Guam'), ('gt', 'Guatemala'), ('gg', 'Guernsey'), ('gn', 'Guinea'), ('gw', 'Guinea-Bissau'), ('gy', 'Guyana'), ('ht', 'Haiti'), ('hm', 'Heard Island and McDonald Islands'), ('va', 'Holy See (Vatican City State)'), ('hn', 'Honduras'), ('hk', 'Hong Kong'), ('hu', 'Hungary'), ('is', 'Iceland'), ('in', 'India'), ('id', 'Indonesia'), ('ir', 'Iran'), ('iq', 'Iraq'), ('ie', 'Ireland'), ('im', 'Isle of Man'), ('il', 'Israel'), ('it', 'Italy'), ('jm', 'Jamaica'), ('jp', 'Japan'), ('je', 'Jersey'), ('jo', 'Jordan'), ('kz', 'Kazakhstan'), ('ke', 'Kenya'), ('ki', 'Kiribati'), ('xko', 'Korea'), ('xkv', 'Kosovo'), ('kw', 'Kuwait'), ('kg', 'Kyrgyzstan'), ('la', 'Laos'), ('lv', 'Latvia'), ('lb', 'Lebanon'), ('ls', 'Lesotho'), ('lr', 'Liberia'), ('ly', 'Libya'), ('li', 'Liechtenstein'), ('lt', 'Lithuania'), ('lu', 'Luxembourg'), ('mo', 'Macao'), ('mg', 'Madagascar'), ('mw', 'Malawi'), ('my', 'Malaysia'), ('mv', 'Maldives'), ('ml', 'Mali'), ('mt', 'Malta'), ('mh', 'Marshall Islands'), ('mq', 'Martinique'), ('mr', 'Mauritania'), ('mu', 'Mauritius'), ('yt', 'Mayotte'), ('mx', 'Mexico'), ('md', 'Moldova'), ('mc', 'Monaco'), ('mn', 'Mongolia'), ('me', 'Montenegro'), ('ms', 'Montserrat'), ('ma', 'Morocco'), ('mz', 'Mozambique'), ('mm', 'Myanmar'), ('na', 'Namibia'), ('nr', 'Nauru'), ('np', 'Nepal'), ('nl', 'Netherlands'), ('an', 'Netherlands Antilles'), ('nc', 'New Caledonia'), ('nz', 'New Zealand'), ('ni', 'Nicaragua'), ('ne', 'Niger'), ('ng', 'Nigeria'), ('nu', 'Niue'), ('nf', 'Norfolk Island'), ('kp', 'North Korea'), ('vdvn', 'North Vietnam'), ('mp', 'Northern Mariana Islands'), ('no', 'Norway'), ('om', 'Oman'), ('pk', 'Pakistan'), ('pw', 'Palau'), ('xpi', 'Palestine'), ('ps', 'Palestinian Territory'), ('pa', 'Panama'), ('pg', 'Papua New Guinea'), ('py', 'Paraguay'), ('pe', 'Peru'), ('ph', 'Philippines'), ('pl', 'Poland'), ('pt', 'Portugal'), ('pn', 'Pitcairn'), ('pr', 'Puerto Rico'), ('qa', 'Qatar'), ('mk', 'Republic of Macedonia'), ('re', 'Réunion'), ('ro', 'Romania'), ('ru', 'Russia'), ('rw', 'Rwanda'), ('bl', 'Saint Barthélemy'), ('sh', 'Saint Helena'), ('kn', 'Saint Kitts and Nevis'), ('lc', 'Saint Lucia'), ('mf', 'Saint Martin (French part)'), ('pm', 'Saint Pierre and Miquelon'), ('vc', 'Saint Vincent and the Grenadines'), ('ws', 'Samoa'), ('sm', 'San Marino'), ('st', 'Sao Tome and Principe'), ('sa', 'Saudi Arabia'), ('sn', 'Senegal'), ('rs', 'Serbia'), ('csxx', 'Serbia and Montenegro'), ('sc', 'Seychelles'), ('xsi', 'Siam'), ('sl', 'Sierra Leone'), ('sg', 'Singapore'), ('sk', 'Slovakia'), ('si', 'Slovenia'), ('sb', 'Solomon Islands'), ('so', 'Somalia'), ('za', 'South Africa'), ('gs', 'South Georgia and the South Sandwich Islands'), ('kr', 'South Korea'), ('suhh', 'Soviet Union'), ('es', 'Spain'), ('lk', 'Sri Lanka'), ('sd', 'Sudan'), ('sr', 'Suriname'), ('sj', 'Svalbard and Jan Mayen'), ('sz', 'Swaziland'), ('se', 'Sweden'), ('ch', 'Switzerland'), ('sy', 'Syria'), ('tw', 'Taiwan'), ('tj', 'Tajikistan'), ('tz', 'Tanzania'), ('th', 'Thailand'), ('tl', 'Timor-Leste'), ('tg', 'Togo'), ('tk', 'Tokelau'), ('to', 'Tonga'), ('tt', 'Trinidad and Tobago'), ('tn', 'Tunisia'), ('tr', 'Turkey'), ('tm', 'Turkmenistan'), ('tc', 'Turks and Caicos Islands'), ('tv', 'Tuvalu'), ('vi', 'U.S. Virgin Islands'), ('ug', 'Uganda'), ('ua', 'Ukraine'), ('ae', 'United Arab Emirates'), ('gb', 'United Kingdom'), ('us', 'United States'), ('um', 'United States Minor Outlying Islands'), ('uy', 'Uruguay'), ('uz', 'Uzbekistan'), ('vu', 'Vanuatu'), ('ve', 'Venezuela'), ('vn', 'Vietnam'), ('wf', 'Wallis and Futuna'), ('xwg', 'West Germany'), ('eh', 'Western Sahara'), ('ye', 'Yemen'), ('xyu', 'Yugoslavia'), ('zrcd', 'Zaire'), ('zm', 'Zambia'), ('zw', 'Zimbabwe')],
                                required=False)
    # переделать в checkbox?????????????????



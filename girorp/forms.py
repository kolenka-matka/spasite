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

    country = forms.MultipleChoiceField(choices=[('af', 'Afghanistan'), ('ax', 'Åland Islands'), ('al', 'Albania'), ('dz', 'Algeria'), ('as', 'American Samoa'), ('ad', 'Andorra'), ('ao', 'Angola'), ('ai', 'Anguilla'), ('aq', 'Antarctica'), ('ag', 'Antigua and Barbuda'), ('ar', 'Argentina'), ('am', 'Armenia'), ('aw', 'Aruba'), ('au', 'Australia'), ('at', 'Austria'), ('az', 'Azerbaijan'), ('bs', 'Bahamas'), ('bh', 'Bahrain'), ('bd', 'Bangladesh'), ('bb', 'Barbados'), ('by', 'Belarus'), ('be', 'Belgium'), ('bz', 'Belize'), ('bj', 'Benin'), ('bm', 'Bermuda'), ('bt', 'Bhutan'), ('bo', 'Bolivia'), ('bq', 'Bonaire, Sint Eustatius and Saba'), ('ba', 'Bosnia and Herzegovina'), ('bw', 'Botswana'), ('bv', 'Bouvet Island'), ('br', 'Brazil'), ('io', 'British Indian Ocean Territory'), ('vg', 'British Virgin Islands'), ('bn', 'Brunei Darussalam'), ('bg', 'Bulgaria'), ('bf', 'Burkina Faso'), ('bumm', 'Burma'), ('bi', 'Burundi'), ('kh', 'Cambodia'), ('cm', 'Cameroon'), ('ca', 'Canada'), ('cv', 'Cape Verde'), ('ky', 'Cayman Islands'), ('cf', 'Central African Republic'), ('td', 'Chad'), ('cl', 'Chile'), ('cn', 'China'), ('cx', 'Christmas Island'), ('cc', 'Cocos (Keeling) Islands'), ('co', 'Colombia'), ('km', 'Comoros'), ('cg', 'Congo'), ('ck', 'Cook Islands'), ('cr', 'Costa Rica'), ('ci', "Côte d'Ivoire"), ('hr', 'Croatia'), ('cu', 'Cuba'), ('cy', 'Cyprus'), ('cz', 'Czech Republic'), ('cshh', 'Czechoslovakia'), ('cd', 'Democratic Republic of the Congo'), ('dk', 'Denmark'), ('dj', 'Djibouti'), ('dm', 'Dominica'), ('do', 'Dominican Republic'), ('ddde', 'East Germany'), ('ec', 'Ecuador'), ('eg', 'Egypt'), ('sv', 'El Salvador'), ('gq', 'Equatorial Guinea'), ('er', 'Eritrea'), ('ee', 'Estonia'), ('et', 'Ethiopia'), ('fk', 'Falkland Islands'), ('fo', 'Faroe Islands'), ('yucs', 'Federal Republic of Yugoslavia'), ('fm', 'Federated States of Micronesia'), ('fj', 'Fiji'), ('fi', 'Finland'), ('fr', 'France'), ('gf', 'French Guiana'), ('pf', 'French Polynesia'), ('tf', 'French Southern Territories'), ('ga', 'Gabon'), ('gm', 'Gambia'), ('ge', 'Georgia'), ('de', 'Germany'), ('gh', 'Ghana'), ('gi', 'Gibraltar'), ('gr', 'Greece'), ('gl', 'Greenland'), ('gd', 'Grenada'), ('gp', 'Guadeloupe'), ('gu', 'Guam'), ('gt', 'Guatemala'), ('gg', 'Guernsey'), ('gn', 'Guinea'), ('gw', 'Guinea-Bissau'), ('gy', 'Guyana'), ('ht', 'Haiti'), ('hm', 'Heard Island and McDonald Islands'), ('va', 'Holy See (Vatican City State)'), ('hn', 'Honduras'), ('hk', 'Hong Kong'), ('hu', 'Hungary'), ('is', 'Iceland'), ('in', 'India'), ('id', 'Indonesia'), ('ir', 'Iran'), ('iq', 'Iraq'), ('ie', 'Ireland'), ('im', 'Isle of Man'), ('il', 'Israel'), ('it', 'Italy'), ('jm', 'Jamaica'), ('jp', 'Japan'), ('je', 'Jersey'), ('jo', 'Jordan'), ('kz', 'Kazakhstan'), ('ke', 'Kenya'), ('ki', 'Kiribati'), ('xko', 'Korea'), ('xkv', 'Kosovo'), ('kw', 'Kuwait'), ('kg', 'Kyrgyzstan'), ('la', 'Laos'), ('lv', 'Latvia'), ('lb', 'Lebanon'), ('ls', 'Lesotho'), ('lr', 'Liberia'), ('ly', 'Libya'), ('li', 'Liechtenstein'), ('lt', 'Lithuania'), ('lu', 'Luxembourg'), ('mo', 'Macao'), ('mg', 'Madagascar'), ('mw', 'Malawi'), ('my', 'Malaysia'), ('mv', 'Maldives'), ('ml', 'Mali'), ('mt', 'Malta'), ('mh', 'Marshall Islands'), ('mq', 'Martinique'), ('mr', 'Mauritania'), ('mu', 'Mauritius'), ('yt', 'Mayotte'), ('mx', 'Mexico'), ('md', 'Moldova'), ('mc', 'Monaco'), ('mn', 'Mongolia'), ('me', 'Montenegro'), ('ms', 'Montserrat'), ('ma', 'Morocco'), ('mz', 'Mozambique'), ('mm', 'Myanmar'), ('na', 'Namibia'), ('nr', 'Nauru'), ('np', 'Nepal'), ('nl', 'Netherlands'), ('an', 'Netherlands Antilles'), ('nc', 'New Caledonia'), ('nz', 'New Zealand'), ('ni', 'Nicaragua'), ('ne', 'Niger'), ('ng', 'Nigeria'), ('nu', 'Niue'), ('nf', 'Norfolk Island'), ('kp', 'North Korea'), ('vdvn', 'North Vietnam'), ('mp', 'Northern Mariana Islands'), ('no', 'Norway'), ('om', 'Oman'), ('pk', 'Pakistan'), ('pw', 'Palau'), ('xpi', 'Palestine'), ('ps', 'Palestinian Territory'), ('pa', 'Panama'), ('pg', 'Papua New Guinea'), ('py', 'Paraguay'), ('pe', 'Peru'), ('ph', 'Philippines'), ('pl', 'Poland'), ('pt', 'Portugal'), ('pn', 'Pitcairn'), ('pr', 'Puerto Rico'), ('qa', 'Qatar'), ('mk', 'Republic of Macedonia'), ('re', 'Réunion'), ('ro', 'Romania'), ('ru', 'Russia'), ('rw', 'Rwanda'), ('bl', 'Saint Barthélemy'), ('sh', 'Saint Helena'), ('kn', 'Saint Kitts and Nevis'), ('lc', 'Saint Lucia'), ('mf', 'Saint Martin (French part)'), ('pm', 'Saint Pierre and Miquelon'), ('vc', 'Saint Vincent and the Grenadines'), ('ws', 'Samoa'), ('sm', 'San Marino'), ('st', 'Sao Tome and Principe'), ('sa', 'Saudi Arabia'), ('sn', 'Senegal'), ('rs', 'Serbia'), ('csxx', 'Serbia and Montenegro'), ('sc', 'Seychelles'), ('xsi', 'Siam'), ('sl', 'Sierra Leone'), ('sg', 'Singapore'), ('sk', 'Slovakia'), ('si', 'Slovenia'), ('sb', 'Solomon Islands'), ('so', 'Somalia'), ('za', 'South Africa'), ('gs', 'South Georgia and the South Sandwich Islands'), ('kr', 'South Korea'), ('suhh', 'Soviet Union'), ('es', 'Spain'), ('lk', 'Sri Lanka'), ('sd', 'Sudan'), ('sr', 'Suriname'), ('sj', 'Svalbard and Jan Mayen'), ('sz', 'Swaziland'), ('se', 'Sweden'), ('ch', 'Switzerland'), ('sy', 'Syria'), ('tw', 'Taiwan'), ('tj', 'Tajikistan'), ('tz', 'Tanzania'), ('th', 'Thailand'), ('tl', 'Timor-Leste'), ('tg', 'Togo'), ('tk', 'Tokelau'), ('to', 'Tonga'), ('tt', 'Trinidad and Tobago'), ('tn', 'Tunisia'), ('tr', 'Turkey'), ('tm', 'Turkmenistan'), ('tc', 'Turks and Caicos Islands'), ('tv', 'Tuvalu'), ('vi', 'U.S. Virgin Islands'), ('ug', 'Uganda'), ('ua', 'Ukraine'), ('ae', 'United Arab Emirates'), ('gb', 'United Kingdom'), ('us', 'United States'), ('um', 'United States Minor Outlying Islands'), ('uy', 'Uruguay'), ('uz', 'Uzbekistan'), ('vu', 'Vanuatu'), ('ve', 'Venezuela'), ('vn', 'Vietnam'), ('wf', 'Wallis and Futuna'), ('xwg', 'West Germany'), ('eh', 'Western Sahara'), ('ye', 'Yemen'), ('xyu', 'Yugoslavia'), ('zrcd', 'Zaire'), ('zm', 'Zambia'), ('zw', 'Zimbabwe')],
                                required=False, label='выберите страну-производителя')

    plot = forms.CharField(label='сюжет', required=False, help_text='введите здесь ключевые слова, которые могут встретиться в описании сюжета фильма. слова можно вводить на русском или английском языке. в результаты поиска войдут только фильмы, в описании которых присутствуют все введенные слова.')

    ratings = forms.MultipleChoiceField(choices=[
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC', 'NC')
    ], label='рейтинги', required=False, help_text='''Рейтинг G — General audiences:
Фильм демонстрируется без ограничений. Данный рейтинг показывает, что оценённый фильм не содержит ничего, что большинство родителей могло бы посчитать неприемлемым для просмотра или прослушивания даже самыми маленькими детьми. Обнажение, сексуальные сцены и сцены приёма наркотиков отсутствуют; насилие минимально; могут употребляться выражения, выходящие за пределы вежливой беседы, но только те, которые постоянно встречаются в повседневной речи. Более грубая лексика в фильмах с рейтингом G употребляться не может.

Рейтинг PG — Parental guidance suggested:
Детям рекомендуется смотреть фильм с родителями. Некоторые материалы могут не подходить для детей. Этот рейтинг показывает, что родители могут найти некоторые из сцен в фильме неподходящими для детей и что родителям рекомендуется посмотреть фильм, прежде чем показывать его детям. Явные сексуальные сцены и сцены употребления наркотиков отсутствуют; нагота, если присутствует, только в очень ограниченной степени, могут быть использованы лёгкие ругательства и представлены сцены насилия, но только в очень умеренных количествах.

Рейтинг PG-13 — Parents strongly cautioned:
Просмотр не желателен детям до 13 лет. Данный рейтинг показывает, что оценённый фильм может быть неподходящим для детей. Родители должны быть особенно осторожны, разрешая своим маленьким детям просмотр. Может присутствовать умеренное или грубое насилие; могут присутствовать сцены с наготой; возможны ситуации с сексуальным контекстом; могут присутствовать некоторые сцены употребления наркотиков; можно услышать единичные употребления грубых ругательств.

Рейтинг R — Restricted:
Лица, не достигшие 17-летнего возраста, допускаются на фильм только в сопровождении одного из родителей, либо законного представителя. Данный рейтинг показывает, что оценочная комиссия заключила, что некоторый материал оценённого фильма предназначается только для взрослых. Родители должны больше узнать о фильме, прежде чем взять на его просмотр подростков. Рейтинг R может быть назначен из-за частого употребления непристойной лексики, продолжительных сцен насилия, полового акта или употребления наркотиков.

Рейтинг NC-17 — No One 17 & Under Admitted:
Лица 17-летнего возраста и младше на фильм не допускаются. Данный рейтинг показывает, что оценочная комиссия полагает, что по мнению большинства родителей фильм явно для взрослых, и детей до 17 лет нельзя допускать до просмотра. Фильм может содержать явные сексуальные сцены, большое количество непристойной и сексуальной лексики, или сцен чрезмерного насилия. Рейтинг NC-17, однако, ещё не означает, что данный фильм является непристойным или порнографическим, как в повседневном, так и в юридическом смысле этих слов.''')

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




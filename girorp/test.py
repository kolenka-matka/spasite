import requests
from bs4 import BeautifulSoup

# о том как я пыталась достать список меток по играм:
url = 'https://store.steampowered.com/tag/browse/'
text_ = requests.get(url).text
text = '''<div data-panel="{&quot;bFocusRingRoot&quot;:true,&quot;flow-children&quot;:&quot;row&quot;}" class="tag_browse_tags peeking_carousel" id="tag_browse_global">
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag active" data-tagid="492">Инди</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="19">Экшен</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="21">Приключение</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="597">Казуальная игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="599">Симулятор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="122">Ролевая игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9">Стратегия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4182">Для одного игрока</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="493">Ранний доступ</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="113">Бесплатная игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3871">2D</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4166">Атмосферная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4191">3D</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="128">ММО</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3859">Для нескольких игроков</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1742">Глубокий сюжет</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="701">Спортивная игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1684">Фэнтези</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1664">Головоломка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4667">Насилие</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4305">Цветастая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3964">Пиксельная графика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3834">Исследования</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="699">Гонки</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4726">Милая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6650">Нагота</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3839">От первого лица</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="12095">Сексуальный контент</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4085">Аниме</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4345">Мясо</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4136">Смешная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3942">Научная фантастика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1773">Аркада</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1774">Шутер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4106">Приключенческий экшен</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5350">Для всей семьи</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1667">Хоррор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1654">Расслабляющая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3993">Бой</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4004">Ретро</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1695">Открытый мир</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1625">Платформер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1685">Кооператив</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7208">Протагонистка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1697">От третьего лица</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1662">Выживание</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1756">Отличный саундтрек</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4252">Стилизация</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1719">Юмор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4026">Сложная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1775">Игрок против игрока</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7481">Контроллер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="21978">VR</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6426">Решения с последствиями</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3916">Олдскул</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3799">Визуальная новелла</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1663">Шутер от первого лица</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4175">Реализм</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4791">Вид сверху</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3968">Физика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3843">Сетевой кооператив</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4342">Мрачная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4747">Кастомизация персонажа</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5716">Тайна</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4195">Мультипликация</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3810">Песочница</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6971">Несколько концовок</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5379">2D-платформер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6730">Игра против ИИ</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1721">Психологический хоррор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7250">Линейная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1708">Тактика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4094">Минимализм</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4172">Средневековье</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1755">Космос</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4057">Магия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4255">Shoot 'em up</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="84">Дизайн и иллюстрация</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1643">Строительство</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4295">Будущее</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4231">Ролевой экшен</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1698">Point &amp; Click</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="12472">Менеджмент</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7368">Локальный мультиплеер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="87">Утилиты</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6815">Рисованная графика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1702">Крафтинг</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3798">Вид сбоку</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7743">80-е</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1036">Образование</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4562">Мультфильмы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5125">Процедурная генерация</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="8945">Управление ресурсами</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5537">Головоломка-платформер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5611">Для взрослых</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3978">Хоррор на выживание</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6129">Логика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5984">Драма</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1677">Пошаговая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1716">Рогалик</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4711">Реиграбельность</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4325">Пошаговые сражения</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4604">Тёмное фэнтези</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1678">Война</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5395">3D-платформер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1659">Зомби</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1741">Пошаговая стратегия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="17389">Настольная игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4947">Романтика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1646">Слэшер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4486">Выбери себе приключение</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3841">Локальный кооператив</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3959">Упрощённый рогалик</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3835">Постапокалипсис</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4434">Японская ролевая игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="14139">Пошаговая тактика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7332">Строительство базы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="11014">Интерактивная литература</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3987">Историческая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9551">Симулятор свиданий</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="10695">Партийная ролевая игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5608">Эмоциональная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1738">Поиск предметов</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1710">Сюрреалистичная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1687">Стелс</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5900">Симулятор ходьбы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5094">Повествовательная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1720">Подземелья</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9130">Хентай</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="10397">Мемы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="30358">Природа</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6691">90-е</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9204">Иммерсивный симулятор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1038">Веб-публикация</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5154">Набор очков</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4885">Скролл-шутер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4168">Военные действия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3814">Шутер от третьего лица</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1734">Быстрая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5752">Роботы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1693">Классика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5711">Командная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4637">Шутер с видом сверху</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5851">Изометрия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4975">Псевдотрёхмерность</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4115">Киберпанк</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="15172">Беседы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1673">Инопланетяне</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4234">Короткая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="31275">Текстовая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1676">Стратегия в реальном времени</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4145">Кинематографичная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="42804">Экшен-рогалик</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5923">Чёрный юмор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="872">Анимация и моделирование</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="44868">ЛГБТК+</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="8013">Программное обеспечение</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="8369">Расследования</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4700">Фильм</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6869">Нелинейная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1666">Карточная игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6276">Менеджмент инвентаря</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="12057">Обучение</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4695">Экономика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1644">Вождение</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4400">Абстрактная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="24904">NSFW</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7926">Искусственный интеллект</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5411">Красивая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1621">Музыка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5577">RPG Maker</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1759">Одна жизнь</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9541">Демоны</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1770">Настольная с полем</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="17305">Ролевая стратегия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4840">Локальная игра на четверых</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="379975">Кликер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="10235">Симулятор жизни</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3813">Тактика в реальном времени</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3854">Проработанная вселенная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5186">Психологическая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="13782">Экспериментальная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4064">Триллер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5613">Детектив</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="15045">Полёты</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5547">Арена-шутер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5673">Современность</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1743">Файтинг</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7948">Саундтрек</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5030">Антиутопия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1645">Башенная защита</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="16689">Тайм-менеджмент</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4328">Градостроение</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3877">Платформер на точность</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1714">Психоделия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1669">Поддержка модификаций</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4236">Лут</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1027">Работа со звуком</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5363">Разрушения</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="21725">Тактическая ролевая игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="10808">Сверхъестественное</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4158">Beat 'em up</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1628">Метроидвания</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="784">Видеопродакшн</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4598">Альтернативная история</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3878">Соревновательная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4684">Военные конфликты</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="8122">Редактор уровней</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1751">По комиксу</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="29482">Похожа на Dark Souls</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="16094">Мифология</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1754">MMORPG</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6378">Криминал</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="13906">Разработка игр</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4036">Паркур</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="8666">Раннер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7569">Перемещение по сетке</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4736">2D-файтинг</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="19995">Чёрная комедия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4150">Вторая мировая война</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4474">Компьютерная ролевая игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="15277">Философская</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5652">Коллектатон</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4155">Разделение на классы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5794">Наука</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1100687">Автосимулятор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4508">Совместная кампания</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3955">Яркий главный герой</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="615955">Idle-игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4758">Твин-стик шутер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5765">Кастомизация оружия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4364">Глобальная стратегия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1445">Обучение работе с ПО</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1752">Ритм-игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="16598">Космический симулятор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4608">Сражения на мечах</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="32322">Построение колоды</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="17894">Котики</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4046">Драконы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7432">Лавкрафт</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5228">Кровь</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="176981">Королевская битва</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4190">Затягивающая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="11104">Гонки на выживание</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="791774">Карточный баттлер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4835">Свобода движения</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5055">Киберспорт</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="13190">Америка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="29363">3D Vision</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1665">Три в ряд</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="10816">Разделение экрана</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6052">Нуар</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6506">3D-файтинг</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4878">Пародия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4845">Капитализм</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5372">Заговор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7478">Иллюминаты</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1100689">Симулятор выживания в открытом мире</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1651">Сатира</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5796">Замедление времени</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="255534">Автоматика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4202">Обмен</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1732">Воксельная графика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4853">Политическая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="220585">Симулятор колонии</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1777">Стимпанк</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="198631">Загадочные подземелья</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6625">Контроль времени</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3952">Готика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9592">Динамическое повествование</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4559">QTE</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="809">Обработка фото</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4821">Мехи</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="22602">Сельское хозяйство</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="21006">Подземная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="11123">Управление мышью</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="10679">Путешествия во времени</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="87918">Симулятор фермы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4161">В реальном времени</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="620519">Геройский шутер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5981">Шахты</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9564">Охота</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4242">Сериал</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7782">Культовая классика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="24003">Словесные</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3965">Эпичная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6915">Боевые искусства</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1718">MOBA</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="916648">Поиск существ</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="13276">Танки</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="31579">Отомэ</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4777">Зрелищные сражения</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1681">Пираты</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1688">Ниндзя</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1638">Собаки</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4754">Политика</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5502">Хакерство</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="353880">Лутер-шутер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5300">Симулятор бога</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4102">Боевые гонки</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="13070">Пасьянс</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5708">Ремейк</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5179">Холодная война</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="17770">Асинхронный мультиплеер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1717">Шестиугольная карта</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="18594">Видеовставки</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9271">Коллекционная карточная игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1671">Супергерои</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4376">Ассассины</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="15564">Рыбалка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1670">4X</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3920">Кулинария</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9157">Подводный мир</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5432">Программирование</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4018">Вампиры</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5160">Динозавры </div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7702">Повествование</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="180368">Верования</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3934">Иммерсивная игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1680">Ограбления</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1616">Поезда</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1647">Вестерн</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6910">Флот</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7107">Можно приостановить</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1730">Сокобан</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="26921">Политический симулятор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7108">Вечеринка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="8093">Мини-игры</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1084988">Автобаттлер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7178">Командная игра</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="13382">Стрельба из лука</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5153">Kickstarter</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6310">Дипломатия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="51306">Зарубежная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1723">Экшен-RTS</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="10383">Транспорт</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9803">Снег</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1649">GameMaker</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4994">Морской бой</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="25085">Сенсорное управление</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5348">Модификации</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="14153">Dungeons &amp; Dragons</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="9994">Переживание</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5230">Сиквел</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="8253">Генерация на основе музыки</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7423">Снайперство</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="16250">Азартная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4137">Трансгуманизм</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="13577">Мореплавание</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6702">Марс</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1674">Печатание</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="11333">Злодей-протагонист</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5390">Игра на время</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="56690">Рельсовый шутер</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7622">Бездорожье</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1679">Футбол</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5382">Первая мировая война</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="15339">Документальный фильм</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5310">Games Workshop</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6041">Лошади</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7226">Американский футбол</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="17015">Оборотни</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="10437">Викторина</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="150626">Об играх</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="454187">Традиционный рогалик</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="15954">Молчаливый главный герой</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="776177">Панорамное видео</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="12190">Бокс</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1091588">Карточный рогалик</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4520">Фермерство</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="14720">Ностальгия</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4184">Шахматы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7113">Создана на пожертвования</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1733">Суровая</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="92092">Авиасимулятор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1100686">Симулятор эпидемии</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1736">LEGO</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="4291">Космические корабли</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="856791">Асимметричная VR</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6948">Рим</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="769306">Квест</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="8075">TrackIR</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="198913">Мотоциклы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="71389">Правописание</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1100688">Медицинский симулятор</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7038">Гольф</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="6621">Пинбол</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="61357">Электронная музыка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="29855">Эмбиент</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="19780">Подводная лодка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="123332">Байки</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="922563">Рогалик-метроидвания</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="12286">Warhammer 40K</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1746">Баскетбол</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="745697">Социальная дедукция</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="3796">По мотивам книги</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="1753">Скейтбординг</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="22955">Мини-гольф</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="47827">Реслинг</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="14906">Нарочито неудобное управление</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="189941">Инструментальная музыка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="17927">Бильярд</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="11634">Викинги</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5914">Теннис</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5727">Бейсбол</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5407">Бенчмарк</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="17337">Лемминги</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="96359">Коньки</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="15868">Мотокросс</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="19568">Велосипеды</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="324176">Хоккей</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="603297">Устройства</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="348922">Steam Machine</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7328">Боулинг</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="337964">Рок-музыка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="117648">8-битная музыка</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="143739">Электроника</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="129761">Квадроциклы</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="27758">Управление голосом</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="252854">Веломотокросс</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="11095">Boss Rush</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="8461">Хорошо написанная</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="233824">Полнометражный фильм</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="28444">Сноубординг</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="7309">Лыжи</div>
									<div data-panel="{&quot;autoFocus&quot;:true,&quot;focusable&quot;:true,&quot;clickOnActivate&quot;:true}" class="tag_browse_tag" data-tagid="5941">Перезапуск</div>
							</div>'''
soup = BeautifulSoup(text, 'lxml')
tags = soup.find('div', class_='tag_browse_tags peeking_carousel')
tags = tags.find_all('div')
tags = [(item.text, item.get('data-tagid')) for item in tags]

soup_ = BeautifulSoup(text_, 'lxml')
tags_ = soup_.find('div', class_='tag_browse_tags peeking_carousel')
tags_ = tags_.find_all('div')
tags_ = ['games_' + item.text.lower().replace(' ', '_').replace('-', '_').replace('2', 'two').replace('3', 'three') for item in tags_]
print(tags)
print(tags_)

# games_tag_list = [(tags_[i], tags[i][0]) for i in range(15, 426)]
# print(games_tag_list)
# print([item[::-1] for item in tags[15::]])
# for i in range(15):
#     print(f"exclude_{tags_[i]} = ('{tags[i][1]}', form.cleaned_data.get('exclude_{tags_[i]}'))")
# print(*(tags_[i] for i in range(15)), sep=', ')
# print(*('exclude_' + tags_[i] for i in range(15)), sep=', ')

players = [item.strip() for item in ''' Для одного игрока
 Для нескольких игроков
 Против игроков
 Против игроков (по сети)
 Против игроков (LAN)
 Против игроков (общий экран)
 Кооперативная игра
 Кооператив (по сети)
 Кооператив (LAN)
 Кооператив (общий экран)
 Общий экран
 Кроссплатформенная игра'''.split('\n')]
# a = '2%2C1%2C49%2C36%2C47%2C37%2C9%2C38%2C48%2C39%2C24%2C27'.split('%2C')
# players = [(a[i], players[i]) for i in range(len(a))]
# print(players)

dic = {tags[i][1]: tags[i][0] for i in range(426)}
print(dic)

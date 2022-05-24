import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from .lists import ratings_help_text, actors_list, countries_list, new_book_genres_list
import re


def from_hren_to_genre(name):
    genre = [i[1] for i in new_book_genres_list if i[0] == name][0]
    return genre


def create_request(selected_category=None, selected_genres=None, countries=None,
                   exclude_genres=set(), plot=None, ratings=None, actors=None):
    print('exclude: ', exclude_genres, ', include:', selected_genres)
    print(selected_category)

    # !!!!!!!!!!!!! -- вот отсюда начинается код из-за который не работает -- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """
    url = ""
    
    if selected_category == 'movies' or selected_category == 'tv_series':
        url = "https://www.imdb.com/search/title/?title_type=feature,tv_movie,short,documentary"
    elif selected_category == 'book':
        url = "https://www.litres.ru"

    """
    # !!!!!!!!!!!!!!!!!!-- вот отсюда начинается код из-за которого ничего не работает -- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    url = "https://www.imdb.com/search/title/?title_type=feature,tv_movie,short,documentary"
    if selected_genres:
        if exclude_genres:
            selected_genres = [item for item in selected_genres if item not in exclude_genres]
        genres = ','.join(selected_genres)
        url = url + "&genres=" + genres

    if countries:
        countries = ','.join(countries)
        url = url + "&countries=" + countries

    if actors:
        actors = ','.join((actor.split('/')[-1] for actor in actors))
        url = url + "&role=" + actors.split('/')[-1]

    if plot:
        translator = Translator()
        plot = translator.translate(plot, dest='en').text.lower().replace(',', '').replace('.', '').split()

        plot = '+'.join(plot)
        url = url + "&plot=" + plot

    if ratings:
        ratings = ','.join((item + 'US%3A' for item in ratings))
        url = url + '&certificates' + ratings
    '''
    if selected_books:
        book_genres = ','.join(selected_books)
        url = url + book_genres + "elektronnie-knigi/"
        '''

    text_ = requests.get(url).text
    # print(url)

    soup = BeautifulSoup(text_, 'lxml')
    found = soup.find_all("div", class_="lister-item mode-advanced")
    output = list()

    for i in found:
        item = i.find('div', class_='lister-item-content')
        name = item.find("a").text
        link = "https://www.imdb.com" + item.find('h3', class_="lister-item-header").find('a').get('href')
        year = item.find('span', class_="lister-item-year text-muted unbold").text
        length_in_min = item.find('span', class_="runtime")
        genre = str()
        if item.find('span', class_="genre") is not None:
            genre = item.find('span', class_="genre").text[1:]
            if any(item in genre.lower() for item in exclude_genres):
                continue
        # ratings = item.find('div', class_="ratings-bar").text

        summary = item.find_all("p", class_="text-muted")[-1].text[1:]
        people = item.find("p", class_='').text
        # pic = i.find('div', class_="lister-item-image float-left").find('img', class_='loadlate').get('src')

        link = 'https://www.imdb.com' + item.find('h3', class_="lister-item-header").find('a').get('href')
        # pic = BeautifulSoup(requests.get(link).text, 'lxml').find("img", class_="ipc-image").get('src')
        pic = re.search(r'class="ipc-image" loading="eager" src=".*?"', requests.get(link).text).group(0)
        pic = pic[pic.find('src') + 5:-1:]
        dic = {'name': name, 'year': year, 'genre': genre, "summary": summary, 'pic': pic, 'link': link}
        output.append(dic)
    return output


def books_help(selected_books=None):
    if selected_books:
        url = "https://www.litres.ru"
        text_ = requests.get(url).text
        url = url + selected_books[0] + "elektronnie-knigi/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        names = []
        authors = []
        hrefs = []
        imgs = []

        for link in soup.findAll(class_="cover_img"):
            href = link.get('src')
            imgs.append(href)

        for link in soup.findAll(class_='art-item__name__href'):
            href = link.get('href')
            name = link.get('title')
            names.append(name)
            hrefs.append(href)

        for link in soup.findAll(class_='art-item__author'):
            auth = link.text
            authors.append(auth)

        result = []
        genre = [i[1] for i in new_book_genres_list if i[0] == selected_books[0]][0]
        for i in range(len(names)):
            dic = {'name': names[i], 'author': authors[i], 'href': hrefs[i], 'genre': genre, 'image': imgs[i]}
            # dic = {'name': names[i], 'author': authors[i], 'href': hrefs[i], 'genre': genre}
            # print(dic)
            result.append(dic)

        return result
    return []


def choose_games(games_selected_genres=None, exclude_games_genres=None):
    pass
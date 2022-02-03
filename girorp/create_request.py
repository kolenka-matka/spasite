import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def create_request(selected_genres=None, countries=None, exclude_genres=set(), plot=None, ratings=None):
    print('exclude: ', exclude_genres, ', include:', selected_genres)
    url = "https://www.imdb.com/search/title/?title_type=feature,tv_movie,short,documentary"
    if selected_genres:
        if exclude_genres:
            selected_genres = [item for item in selected_genres if item not in exclude_genres]
        genres = ','.join(selected_genres)
        url = url + "&genres=" + genres

    if countries:
        countries = ','.join(countries)
        url = url + "&countries=" + countries

    if plot:
        translator = Translator()
        plot = translator.translate(plot, dest='en').text.lower().replace(',', '').replace('.', '').split()

        plot = '+'.join(plot)
        url = url + "&plot=" + plot

    # ?certificates=US%3AG,US%3APG,US%3APG-13,US%3AR
    if ratings:
        ratings = ','.join((item + 'US%3A' for item in ratings))
        url = url + '&certificates' + ratings

    text_ = requests.get(url).text
    print(url)

    soup = BeautifulSoup(text_, 'lxml')
    found = soup.find_all("div", class_="lister-item-content")
    output = list()

    for item in found:
        name = item.find("a").text
        src = item.find
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

        dic = {'name': name, 'year': year, 'genre': genre, "summary": summary}
        output.append(dic)
    return output

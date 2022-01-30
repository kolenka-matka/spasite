import requests
from bs4 import BeautifulSoup

def create_request(selected_genres):
    if selected_genres == ['f']:
        text_ = requests.get("https://www.imdb.com/search/title/?genres=fantasy").text
    else:
        text_ = requests.get("https://www.imdb.com/search/title/?genres=horror").text

    soup = BeautifulSoup(text_, 'lxml')
    found = soup.find_all("div", class_="lister-item-content")
    results = list()
    for item in found:
        src = item.find("a").text
        year = item.find('span', class_="lister-item-year text-muted unbold").text
        length_in_min = item.find('span', class_="runtime")
        genre = item.find('span', class_="genre").text
        # ratings = item.find('div', class_="ratings-bar").text
        summary = item.find_all("p", class_="text-muted")[-1].text
        people = item.find("p", class_='').text
        film = '\n'.join((
        src,
        year,
        # print(length_in_min)
        genre,
        # print(ratings)
        summary,
        # print(people)
        '\nконец фильма) приколы\n'))
        results.append(film)

    return '\n'.join(results)
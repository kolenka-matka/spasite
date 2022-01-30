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

    """
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # help = soup.find_all("", attrs={property: "imdb:pageConst"})
    text_ = requests.get("https://www.imdb.com/title/tt9032400/").text
    soup = BeautifulSoup(text_, 'lxml')
    help = soup.find_all("meta", class_="imdb:pageConst")
    return help
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """

    output = []

    for item in found:
        src = item.find("a").text
        year = item.find('span', class_="lister-item-year text-muted unbold").text
        length_in_min = item.find('span', class_="runtime")
        genre = item.find('span', class_="genre").text[1:]
        # ratings = item.find('div', class_="ratings-bar").text
        summary = item.find_all("p", class_="text-muted")[-1].text[1:]
        people = item.find("p", class_='').text

        dic = {'name': src, 'year': year, 'genre': genre, "summary": summary}

        """
        film = '\n'.join((
        src,
        year,
        # print(length_in_min)
        genre,
        # print(ratings)
        summary,
        # print(people)
        '\nконец фильма) приколы\n'))
        film += '\n'
        results.append(film)
        results.append("\n")
        """

        output.append(dic)

    return output

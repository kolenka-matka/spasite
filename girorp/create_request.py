import requests
from bs4 import BeautifulSoup

def create_request(selected_genres):
    url = "https://www.imdb.com/search/title/"
    if selected_genres:
        genres = ','.join(selected_genres)
        url = url + "?genres=" + genres
    text_ = requests.get(url).text

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
        name = item.find("a").text
        src = item.find
        year = item.find('span', class_="lister-item-year text-muted unbold").text
        length_in_min = item.find('span', class_="runtime")
        genre = item.find('span', class_="genre").text[1:]
        # ratings = item.find('div', class_="ratings-bar").text
        summary = item.find_all("p", class_="text-muted")[-1].text[1:]
        people = item.find("p", class_='').text

        dic = {'name': name, 'year': year, 'genre': genre, "summary": summary}

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

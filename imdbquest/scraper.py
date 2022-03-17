from bs4 import BeautifulSoup
import requests
from imdbquest.movie import Movie


def scraper(n_movie: int):
    return_list = []

    # Collect data from the movies #
    url = 'https://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
    votes = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=nv]')]

    for index in range(0, n_movie):

        # Title of the current movie #
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index)) + 1:-7]

        # Determine the number of the Oscars #
        current_award_url = 'https://www.imdb.com' + links[index] + 'awards/?ref_=tt_awd'
        current_url_resp = requests.get(current_award_url)
        current_movie_soup = BeautifulSoup(current_url_resp.text, 'lxml')
        current_awards = current_movie_soup.find_all('table', {'class': 'awards'})

        # Check if the current movie has won an Oscar or not #
        if current_awards[0].tr.b.get_text() == 'Winner' and current_awards[0].tr.span.get_text() == 'Oscar':
            n_oscar_won = int(current_awards[0].td['rowspan'])
        else:
            n_oscar_won = 0

        # Store the collected data in a Film class #
        return_list.append(Movie(ratings[index], votes[index], n_oscar_won, movie_title))

    return return_list

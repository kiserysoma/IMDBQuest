import argparse
from imdbquest.scraper import scraper
from imdbquest.rating_adjustment import oscar_calculator, review_penalizer
import operator
import json
import unidecode
import os


def main():
    ap = argparse.ArgumentParser(description='First N movies from the IMDB TOP250')
    ap.add_argument("-n_movies", type=int, default=20, help="Enter the number of the movies to get data")
    ar = vars(ap.parse_args())
    args = list(ar.values())

    movie_list = scraper(args[0])
    oscar_calculator(movie_list)
    review_penalizer(movie_list)
    movie_list.sort(key=operator.attrgetter('adjusted_rating'), reverse=True)

    result_list = []
    for movie in movie_list:
        result_list.append([unidecode.unidecode(movie.title), movie.adjusted_rating, movie.rating])

    if not os.path.exists('imdbquest/results'):
        os.makedirs('imdbquest/results')

    with open('imdbquest/results/imdb_top' + str(args[0]) + '_movies.txt', 'w') as file_handle:
        json.dump(result_list, file_handle)


if __name__ == "__main__":
    main()

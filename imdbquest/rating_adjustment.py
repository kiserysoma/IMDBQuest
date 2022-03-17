from imdbquest.movie import Movie


def oscar_calculator(movie_list: Movie):
    return_list = []
    for movie in movie_list:
        if 0 < movie.n_oscars:
            if 2 >= movie.n_oscars:
                movie.set_adjusted_rating((float(movie.get_adjusted_rating()) + 0.3))
            elif 5 >= movie.n_oscars:
                movie.set_adjusted_rating((float(movie.get_adjusted_rating()) + 0.5))
            elif 10 >= movie.n_oscars:
                movie.set_adjusted_rating((float(movie.get_adjusted_rating()) + 1.0))
            else:
                movie.set_adjusted_rating((float(movie.get_adjusted_rating()) + 1.5))
        return_list.append(movie)

    return return_list


def review_penalizer(movie_list: Movie):
    return_list = []
    max_reviewers = 0
    for movie in movie_list:
        temp_n_ratings = int(movie.get_n_ratings())
        if temp_n_ratings > max_reviewers:
            max_reviewers = temp_n_ratings

    for movie in movie_list:
        temp_n_ratings = int(movie.get_n_ratings())
        if max_reviewers > temp_n_ratings:
            deduction = float(int(((max_reviewers - temp_n_ratings) / 1e5)) * 0.1)
            movie.set_adjusted_rating(float(movie.get_adjusted_rating() - deduction))
        return_list.append(movie)

    return return_list

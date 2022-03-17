class Movie:
    def __init__(self, rating: float, n_ratings: int, n_oscars: int, title: str):
        self.rating = float(rating)
        self.adjusted_rating = float(rating)
        self.n_ratings = int(n_ratings)
        self.n_oscars = int(n_oscars)
        self.title = str(title)

    def get_rating(self):
        return self.rating

    def get_n_ratings(self):
        return self.n_ratings

    def get_n_oscars(self):
        return self.n_oscars

    def get_title(self):
        return self.title

    def get_adjusted_rating(self):
        return self.adjusted_rating

    def set_adjusted_rating(self, calculated_rating):
        self.adjusted_rating = float(calculated_rating)

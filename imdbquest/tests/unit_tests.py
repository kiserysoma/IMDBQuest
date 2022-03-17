import unittest
from imdbquest.scraper import scraper
from imdbquest.movie import Movie
from imdbquest.rating_adjustment import oscar_calculator, review_penalizer


class TestScraper(unittest.TestCase):

    def test_returned_list(self):
        result = scraper(20)

        self.assertEqual(len(result), 20)
        for i in range(20):
            self.assertIs(type(result[i]), Movie)
            self.assertIs(type(result[i].n_oscars), int)
            self.assertIs(type(result[i].title), str)
            self.assertIs(type(result[i].n_ratings), int)
            self.assertIs(type(result[i].adjusted_rating), float)
            self.assertIs(type(result[i].rating), float)

            self.assertEqual(result[i].adjusted_rating, result[i].rating)

    def test_collected_data(self):
        expected_data = [Movie(9.2,  2559956, 0, "A remény rabjai"), Movie(9.2, 1762187, 3, "A keresztapa"), Movie(9, 2519994, 2, "A sötét lovag")]

        result = scraper(3)

        for i in range(3):
            self.assertEqual(result[i].title, expected_data[i].title)
            self.assertEqual(result[i].n_oscars, expected_data[i].n_oscars)


class TestOscarCalculator(unittest.TestCase):

    def test_oscar_calculator(self):
        input_data = [Movie(9.2,  2559956, 0, "A remény rabjai"), Movie(9.2, 1762187, 2, "A keresztapa"), Movie(9, 2519994, 4, "A sötét lovag"),
                      Movie(9.0, 1220256, 6, "A keresztapa II"), Movie(8.95, 756295, 11, "Tizenkét dühös ember")]

        result = oscar_calculator(input_data)

        for i in range(5):
            self.assertEqual(result[i].title, input_data[i].title)
            self.assertEqual(result[i].n_oscars, input_data[i].n_oscars)
            self.assertEqual(result[i].rating, input_data[i].rating)
            self.assertEqual(result[i].n_ratings, input_data[i].n_ratings)

        self.assertEqual(result[0].adjusted_rating, 9.2)
        self.assertEqual(result[1].adjusted_rating, 9.5)
        self.assertEqual(result[2].adjusted_rating, 9.5)
        self.assertEqual(result[3].adjusted_rating, 10)
        self.assertEqual(result[4].adjusted_rating, 10.45)

    def test_review_penalizer(self):
        input_data = [Movie(9.2,  2456123, 0, "A remény rabjai"), Movie(9.4, 1258369, 2, "A keresztapa")]
        
        result = review_penalizer(input_data)
        
        for i in range(2):
            self.assertEqual(result[i].title, input_data[i].title)
            self.assertEqual(result[i].n_oscars, input_data[i].n_oscars)
            self.assertEqual(result[i].rating, input_data[i].rating)
            self.assertEqual(result[i].n_ratings, input_data[i].n_ratings)
            
        self.assertEqual(result[0].adjusted_rating, input_data[0].adjusted_rating)
        self.assertEqual(result[1].adjusted_rating, 8.3)


if __name__ == '__main__':
    unittest.main()

IMDBQuest application scrapes data from IMDB and adjusts IMDB ratings based on
the won Oscars and the number of the reviews. 

Used third-party libraries:
- BeautifulSoup
- lxml
- requests
- unidecode
- argparse

The application stores the collected data from every movie in a list that elements are a custom class (Movie).

**Implemented functions**
- scraper: It gets a number as input describing the first N movies (default: N=20) to scrape data of. 
It collects the title, its rating, number of the reviews and the number of the won Oscars. The function scraper
provides the collected data in a list.

- oscar_calculator: The function gets a list containing movies as a parameter and sets the adjusted_rating field 
of its elements based on the won Oscars according to the next rule:
    - 1 or 2 oscars → 0.3 point
    - 3 or 5 oscars → 0.5 point
    - 6 - 10 oscars → 1 point
    - 10+ oscars → 1.5 point

- review_penalizer: The function gets a list containing movies as a parameter and sets the adjusted_rating field 
of its elements based on the number of the reviews. First, the function calculates the maximal number of the reviews in the input list.
The function sets the adjusted_rating filed according to the following rule: 
    - Every 100k deviation from the calculated maximum translates to a point deduction of 0.1.  
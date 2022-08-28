import requests

from classes.moviemon import Moviemon
from classes.map import Map
from Rush00.settings.game_data import *


def get_info() -> dict:
    URL = "http://www.omdbapi.com/?apikey=d550cc9c&"

    moviemon = dict()
    for identifer in IMDB_LIST:
        params = {"i": identifer}
        try:
            res = requests.get(URL, params=params).json()
            moviemon[identifer] = str(Moviemon(
                    res["Title"],
                    res["Year"],
                    res["Director"],
                    res["Poster"],
                    float(res["imdbRating"]),
                    res["Type"],
                    res["Plot"],
                    res["Actors"]
            ))
        except Exception as exc:
            assert exc
    return moviemon


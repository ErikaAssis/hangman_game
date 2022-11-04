from models.api.movie_api import MovieApi
from models.hangman.hangman import Hangman

url = "https://api.themoviedb.org/3/movie/popular?api_key=6f7cad428d6255687d23f8a8907d2d53&language=pt-BR"
random_movie = MovieApi(url).random_movie()

hangman_game = Hangman(random_movie.title, random_movie.overview)
hangman_game.start()

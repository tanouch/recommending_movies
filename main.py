from flask import escape
from reco_movies.movie_recommendations import get_movie_recommendations

def recommending_movies(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    movie_name = request_json["movie_name"]
    movie_year = request_json["movie_year"]
    movie_reco_string = get_movie_recommendations(movie_name, movie_year)
    return '{}'.format(escape(movie_reco_string))

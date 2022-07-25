from flask import escape
from reco_movies.movie_recommendations import get_movie_recommendations

def recommending_movies(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json()
    request_args = request.args

    if request_json:
        movie_name = request_json["movie_name"]
        movie_year = request_json["movie_year"]
    elif request_args:
        movie_name = request_args["movie_name"]
        movie_year = request_args["movie_year"]
    else:
        movie_name = "The Godfather"
        movie_year = 1972
    movie_reco_string = get_movie_recommendations(movie_name, movie_year)
    return '{}'.format(escape(movie_reco_string))

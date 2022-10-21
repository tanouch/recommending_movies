import numpy as np
import wikipedia
from transformers import DistilBertTokenizer, DistilBertModel
import json
import fire
from scipy.spatial import distance
from pkg_resources import resource_stream
import transformers
transformers.logging.set_verbosity_error()

def get_text(movie, year):
    try:
        text = wikipedia.WikipediaPage(title = movie).summary
    except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError) as e:
        try:
            new_movie = movie + " (film)"
            text = wikipedia.WikipediaPage(title = new_movie).summary
        except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError) as e:
            try:
                new_movie = movie + " (" + str(year) + " " + "film)"
                text = wikipedia.WikipediaPage(title = new_movie).summary
            except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError) as e:
                text = ""
    text = text.replace('\n','').replace("\'","")
    if text=="":
        print("Could not find the summary, are you sure this is the right title on Wikipedia ?")
    return text


def get_movie_recommendations(
    movie_name="The Godfather Part III",
    movie_year=1990
    ):
    json_string = resource_stream(__name__, 'data/movie_summaries.json').read().decode()
    movie_summaries = json.loads(json_string)
    json_string = resource_stream(__name__, 'data/movie_vectors.json').read().decode()
    movie_vectors = json.loads(json_string)

    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertModel.from_pretrained('distilbert-base-uncased')
    new_text = get_text(movie_name, movie_year)
    inputs = tokenizer(new_text, return_tensors="pt", max_length=300, truncation=True)
    new_vector = model(**inputs).last_hidden_state[0][-1].detach().numpy()

    all_scores = np.round(np.array([distance.cosine(new_vector, movie_vectors[movie]) \
                           for movie in movie_vectors]), 3)

    num_scores = 10
    top_scores = np.argsort(all_scores)[:num_scores]
    movie_reco_list = list(["Your movie recommendations are: \n"])
    for movie, score in zip([list(movie_vectors.keys())[elem] for elem in top_scores], list(1-all_scores[top_scores])):
        movie_reco_list.append(movie + ": " + str(np.round(score, 3)) + "\n")
    movie_reco_string = ''.join(movie_reco_list)
    return movie_reco_string

def main():
    fire.Fire(get_movie_recommendations)

if __name__ == "__main__":
    fire.Fire(get_movie_recommendations)

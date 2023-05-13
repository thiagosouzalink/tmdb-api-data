from typing import Dict, List, Union

import requests
import pandas as pd

import config
import url


def get_genres() -> Dict[int, str]:
    """Get genres related to movies.

    Raises:
        Exception: if return status is different from 200.

    Returns:
        dict: dictionary of genres identified by id.
    """
    url_genre = url.url_genre()

    request_genre = requests.get(url_genre)
    if request_genre.status_code != 200:
        raise Exception(f"Erro: status code {request_genre.status_code}")
    
    # Get list of genres.
    response_genre = request_genre.json()
    list_genres = response_genre["genres"]
    genres = {}
    for genre in list_genres:
        genres[genre["id"]] = genre["name"]
    
    return genres 


def get_movies(genres: Dict[int, str], page: int
               ) -> Dict[str, List[Union[str, int, float]]]:
    """Get movie information.

    Args:
        genres (Dict[int, str]): genres.
        page (int): requisition page.

    Raises:
        Exception: if return status is different from 200.

    Returns:
        Dict[str, List[Union[str, int, float]]]: information of the 
        films obtained.
    """
    # print(f"Page: {page}")
    url_movie = url.url_movie(page)
    request_movie = requests.get(url_movie)

    if request_movie.status_code != 200:
        raise Exception(f"Erro: status code {request_movie.status_code}")

    # Get top rated movies on TMDB
    response_movie = request_movie.json()
    movies = response_movie["results"]

    id_movie = []
    original_title = []
    original_language = []
    overview = []
    popularity = []
    release_date = []
    title = []
    vote_average = []
    vote_count = []
    genre = []
    for movie in movies:
        id_movie.append(movie["id"])
        original_title.append(movie["original_title"])
        original_language.append(movie["original_language"])
        overview.append(movie["overview"])
        popularity.append(movie["popularity"])
        release_date.append(movie["release_date"])
        title.append(movie["title"])
        vote_average.append(movie["vote_average"])
        vote_count.append(movie["vote_count"])
        list_genres = []
        for id_genre in movie["genre_ids"]:
            list_genres.append(genres[id_genre])
        genre.append(", ".join(list_genres))

    dict_movie = {
        "id_movie": id_movie,
        "original_title": original_title,
        "original_language": original_language,
        "overview": overview,
        "popularity": popularity,
        "release_date": release_date,
        "title": title,
        "vote_average": vote_average,
        "vote_count": vote_count,
        "genre": genre
    }
    
    return dict_movie


def api_to_csv():
    try:
        genres = get_genres()
        for page in range(1, 101):
            movies = get_movies(genres, page)

            df = pd.DataFrame(movies)
            if page == 1:
                df.to_csv(config.filename, mode="a", 
                        sep=";", index=False)
            else:
                df.to_csv(config.filename, mode="a", sep=";", 
                        index=False, header=False)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    api_to_csv()

    

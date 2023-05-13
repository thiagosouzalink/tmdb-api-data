import config 


def url_genre() -> str:
    """Gets url API relates to genres.

    Returns:
        str: url API to genres
    """
    url_base_genre = "https://api.themoviedb.org/3/genre/movie/list?"
    params = f"api_key={config.api_key}&language={config.language}"
    return url_base_genre + params


def url_movie(page: int) -> str:
    """Gets url API relates to movie.

    Args:
        page (int): currently page

    Returns:
        str: url API to movie.
    """
    url_base_movie = "https://api.themoviedb.org/3/movie/top_rated?"
    params= f"api_key={config.api_key}&language={config.language}&page={page}"
    return url_base_movie + params



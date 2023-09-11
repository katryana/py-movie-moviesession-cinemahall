from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> QuerySet:
    if genres_ids is None:
        if actors_ids is None:
            return Movie.objects.all()
        return Movie.objects.filter(actors__id__in=actors_ids)
    if actors_ids is None:
        return Movie.objects.filter(genres__id__in=genres_ids)
    return Movie.objects.filter(
        actors__id__in=actors_ids,
        genres__id__in=genres_ids
    )


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids is not None:
        movie.genres.set(genres_ids)
    if actors_ids is not None:
        movie.actors.set(actors_ids)

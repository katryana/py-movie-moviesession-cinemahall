import datetime
from django.db.models import QuerySet

from db.models import MovieSession


def get_movies_sessions(
        session_date: str = None
) -> QuerySet:
    if session_date is None:
        return MovieSession.objects.all()
    year, month, day = map(int, session_date.split("-"))
    return MovieSession.objects.filter(
        show_time__date=datetime.date(year, month, day)
    )


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def delete_movie_session_by_id(movie_session_id: int) -> None:
    MovieSession.objects.get(id=movie_session_id).delete()


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)
    if show_time is not None:
        movie_session.update(show_time=show_time)
    if movie_id is not None:
        movie_session.update(movie_id=movie_id)
    if cinema_hall_id is not None:
        movie_session.update(cinema_hall_id=cinema_hall_id)

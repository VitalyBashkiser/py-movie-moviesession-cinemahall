from typing import List

from django.db.models.query import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__in=genres_ids,
            actors__in=actors_ids
        ).distinct()
    elif genres_ids:
        queryset = queryset.filter(
            genres__in=genres_ids
        ).distinct()
    elif actors_ids:
        queryset = queryset.filter(
            actors__in=actors_ids
        ).distinct()
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)
    return movie

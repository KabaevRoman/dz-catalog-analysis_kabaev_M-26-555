from math import ceil

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies: list[dict]) -> float:
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)


def catalog_age_stats(
    movies: list[dict],
    current_year: int = 2026,
) -> tuple[int, int, int]:
    min_age = current_year - movies[0]["year"]
    max_age = min_age
    total_age = 0

    for movie in movies:
        age = current_year - movie["year"]
        total_age += age
        min_age = min(min_age, age)
        max_age = max(max_age, age)

    return (max_age, min_age, ceil(total_age / len(movies)))


def duration_in_hours(minutes: int) -> str:
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


def rating_tier(rating: float) -> str:
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year: int) -> str:
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


def print_non_comedy_movies(movies: list[dict]) -> None:
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def print_first_masterpiece(movies: list[dict]) -> None:
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > 9.0:
            print(movie["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title: str) -> str:
    normalized_words = []
    for word in title.split():
        normalized_words.append(word[0].upper() + word[1:])
    return " ".join(normalized_words)


def make_slug(title: str) -> str:
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie: dict) -> str:
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def titles_sorted_by_rating(movies: list[dict]) -> list[str]:
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies: list[dict], n: int = 3) -> list[tuple[str, float]]:
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies: list[dict]) -> dict[str, int]:
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies: list[dict]) -> dict[str, list[str]]:
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            titles = filmography.get(actor, [])
            titles.append(movie["title"])
            filmography[actor] = titles
    return filmography


def ratings_above_average(movies: list[dict]) -> dict[str, float]:
    if not movies:
        return {}
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average
    }


def all_genres(movies: list[dict]) -> set[str]:
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1: dict, movie2: dict) -> set[str]:
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]) -> set[str]:
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies: list[dict], min_rating: float = 8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def demonstrate_generators(movies: list[dict]) -> None:
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    total_duration = sum(
        movie["duration_min"] for movie in movies if movie["rating"] > 7
    )
    print(total_duration)


def build_report(movies: list[dict]) -> None:
    print("ОТЧЕТ ПО КАТАЛОГУ")
    if movies:
        print(f"Средний рейтинг: {average_rating(movies):.1f}")
        average_age = catalog_age_stats(movies)[2]
        print(f"Средний возраст фильмов: {average_age} лет")
    else:
        print("Средний рейтинг: нет данных")
        print("Средний возраст фильмов: нет данных")

    print("\nТоп-3 фильма:")
    top_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)[:3]
    for movie in top_movies:
        print(f"  {format_report_line(movie)}")

    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    for genre, count in sorted(
        genre_counts.items(), key=lambda item: (-item[1], item[0])
    ):
        print(f"  {genre} — {count}")

    genres = ", ".join(sorted(all_genres(movies)))
    print(f"\nВсе жанры каталога: {genres}")


if __name__ == "__main__":
    build_report(movies)

import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies: list) -> float:
    sum_rate = 0
    for movie in movies:
        sum_rate += movie.get('rating', 0)
    return round(sum_rate / len(movies), 1)

def catalog_age_stats(movies: list, current_year=2026) -> tuple:
    old = 0
    new = 1000
    sum_age = 0
    for movie in movies:
            mov_year = movie.get('year')
            age = current_year - mov_year
            sum_age += age
            if age > old:
                old = age
            if age < new:
                new = age
    return (old, new, math.ceil(sum_age / len(movies)))

def duration_in_hours(minutes: int) -> str:
    hour = minutes // 60
    minute = minutes % 60
    return f'{hour}ч {minute}мин'

def rating_tier(rating: float) -> str:
    if rating >= 9.0:
        return "шедевр"
    elif rating >= 7 & rating <= 8.9:
        return "хорошо"
    else:
        return "слабо" if rating < 5.0 else "средне"

def decade_label(year: int) -> str:
    match year:
        case y if y > 2020:
            return "новые"
        case y if 2015 <= y <= 2020:
            return "недавние"
        case _:
            return "старые"

def all_movies_for(movies: list) -> None:
    for movie in movies:
        genres = movie.get('genres')
        if 'comedy' in genres:
            continue
        else:
            print(movie.get('title'))

def good_movie(movies: list) -> None:
    i = 0
    while i < len(movies):
        movie = movies[i]
        if movie.get('rating') > 9.0:
            print(movie.get('title'))
            break
        i += 1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies: list, threshold=120) -> int:
    count = 0
    for movie in movies:
        if movie.get('duration_min') > threshold:
            count += 1
    return count    

def normalize_title(title: str) -> str:
    tcase_title = []
    for word in title.split():
        new_word = word[0].upper() + word[1:]
        tcase_title.append(new_word)
    return ' '.join(tcase_title)

def make_slug(title: str) -> str:
    return title.replace(' ', '-').lower()

def format_report_line(movie: dict) -> str:
    title = normalize_title(movie.get('title'))
    year = movie.get('year')
    rating = movie.get('rating')
    dur = duration_in_hours(movie.get('duration_min'))
    genres = ", ".join(sorted(movie.get('genres')))
    return f'\"{title}\" ({year}) - {rating}/10, {dur}, жанры: {genres}'

def titles_sorted_by_rating(movies: list) -> list:
    return sorted(movies, key=lambda x: x['rating'], reverse=True)

def top_n_by_rating(movies: list, n=3) -> list:
    sorted_titles = titles_sorted_by_rating(movies)
    res = []
    for i in range(0, n):
        res.append((sorted_titles[i].get('title'), sorted_titles[i].get('rating')))
    return res

def main():
    print(average_rating(movies))
    print(duration_in_hours(200))
    print(catalog_age_stats(movies))
    all_movies_for(movies)
    good_movie(movies)
    print(count_long_movies(movies))
    print(normalize_title(movies[5].get('title')))
    print(make_slug(normalize_title(movies[5].get('title'))))
    print(format_report_line(movies[0]))
    print(titles_sorted_by_rating(movies))
    print(top_n_by_rating(movies))
    print(movies)

if __name__ == "__main__":
    main()

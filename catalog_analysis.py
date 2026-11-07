import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": [
         "T. Chalamet", "R. Ferguson", "O. Isaac"]},
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
    '''Возвращает среднюю оценку по каталогу, округленную до одного знака'''
    sum_rate = 0
    for movie in movies:
        sum_rate += movie.get('rating', 0)
    return round(sum_rate / len(movies), 1)

def catalog_age_stats(movies: list, current_year=2026) -> tuple:
    '''
    Возвращает кортеж 
    (самый старый фильм в годах, самый новый фильм в годах, среднее)
    '''
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
    '''Переводит минуты в формат "2ч 35м"'''
    hour = minutes // 60
    minute = minutes % 60
    return f'{hour}ч {minute}м'

def rating_tier(rating: float) -> str:
    '''
    По оценке возвращает категорию: "шедевр" (≥9), 
    "хорошо" (7–8.9), "средне" (5–6.9), "слабо" (<5)
    '''
    if rating >= 9.0:
        return "шедевр"
    elif rating >= 7 & rating <= 8.9:
        return "хорошо"
    else:
        return "слабо" if rating < 5.0 else "средне"

def decade_label(year: int) -> str:
    '''
    Возвращает метку "новые" (после 2020), 
    "недавние" (2015–2020) или "старые" (раньше 2015)
    '''
    match year:
        case y if y > 2020:
            return "новые"
        case y if 2015 <= y <= 2020:
            return "недавние"
        case _:
            return "старые"

def all_movies_for(movies: list) -> None:
    '''Выводит на экран названия всех фильмов, которые НЕ относятся к жанру "comedy"'''
    for movie in movies:
        genres = movie.get('genres')
        if 'comedy' in genres:
            continue
        else:
            print(movie.get('title'))

def good_movie(movies: list) -> None:
    '''Выводит первый по порядку в списке фильм с рейтингом выше 9.0'''
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
    '''Считает количество фильмов длиннее threshold минут'''
    count = 0
    for movie in movies:
        if movie.get('duration_min') > threshold:
            count += 1
    return count    

def normalize_title(title: str) -> str:
    '''Приводит строку к формату Title Case (каждое слово с заглавной буквы)'''
    tcase_title = []
    for word in title.split():
        new_word = word[0].upper() + word[1:]
        tcase_title.append(new_word)
    return ' '.join(tcase_title)

def make_slug(title: str) -> str:
    '''Превращает нормализованное название в «слаг»'''
    return title.replace(' ', '-').lower()

def format_report_line(movie: dict) -> str:
    '''Возвращает единую строку с описанием фильма'''
    title = normalize_title(movie.get('title'))
    year = movie.get('year')
    rating = movie.get('rating')
    dur = duration_in_hours(movie.get('duration_min'))
    genres = ", ".join(sorted(movie.get('genres')))
    return f'\"{title}\" ({year}) - {rating}/10, {dur}, жанры: {genres}'

def titles_sorted_by_rating(movies: list) -> list:
    '''Возвращает список названий фильмов, отсортированных по убыванию рейтинга'''
    return sorted(movies, key=lambda x: x['rating'], reverse=True)

def top_n_by_rating(movies: list, n=3) -> list:
    '''Возвращает список из n кортежей (title, rating) — топ по рейтингу'''
    sorted_titles = titles_sorted_by_rating(movies)
    res = []
    for i in range(0, n):
        res.append((sorted_titles[i].get('title'), sorted_titles[i].get('rating')))
    return res

def count_by_genre(movies: list) -> dict:
    '''Возвращает словарь {жанр: количество фильмов}'''
    genres_count = {}
    for movie in movies:
        for genre in movie.get('genres'):
            genres_count[genre] = genres_count.get(genre, 0) + 1
    return genres_count

def actor_filmography(movies: list) -> dict:
    '''Возвращает словарь {актер: [список названий фильмов]}.'''
    actor_films = {}
    for movie in movies:
        for actor in movie.get('actors'):
            actor_films.setdefault(actor, list()).append(movie.get('title'))
    return actor_films

def title_over_rating(movies: list) -> dict:
    '''Строит словарь {title: rating} только для фильмов с рейтингом выше среднего'''
    return {movie['title']: movie['rating'] 
            for movie in movies if movie['rating'] > average_rating(movies)}

def all_genres(movies: list) -> set:
    '''Возвращает множество всех уникальных жанров каталога'''
    genres = set()
    for movie in movies:
        genres.update(movie.get('genres'))
    return genres

def common_actors(movie1: dict, movie2: dict) -> set:
    '''Возвращает множество актеров, снимавшихся в обоих фильмах'''
    return set(movie1.get('actors')) & set(movie2.get('actors'))

def genres_only_in_one(movies_a: list, movies_b: list) -> set:
    '''Возвращает жанры, встречающиеся в movies_a, но не встречающиеся в movies_b'''
    return all_genres(movies_a) - all_genres(movies_b)

def iter_high_rated(movies: list, min_rating=8.0):
    '''Лениво отдает фильмы с рейтингом не ниже min_rating'''
    for movie in movies:
        if movie.get('rating') > min_rating:
            yield movie

def duration_sum(movies: list) -> None:
    '''
    Генераторное выражение, которое считает 
    суммарную длительность всех фильмов с рейтингом выше 7 в минутах
    '''
    print(sum(m["duration_min"] for m in movies if m["rating"] > 7))

def build_report(movies: list) -> None:
    '''Объединяет результаты всех предыдущих этапов в единый консольный отчет'''
    print('ОТЧЁТ ПО КАТАЛОГУ')
    print(f'Средний рейтинг: {average_rating(movies)}')
    print(f'Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет')
    print()
    print('Топ-3 фильма:')
    for movie in iter_high_rated(movies):
        print(f' {format_report_line(movie)}')
    print()
    print('Фильмов по жанрам:')
    genre_c = sorted(count_by_genre(movies).items(), key=lambda x: x[1], reverse=True)
    for genre in genre_c:
        print(f' {genre[0]} - {genre[1]}')
    print()
    print(f'Все жанры каталога: {', '.join(all_genres(movies))}')

if __name__ == "__main__":
    build_report(movies)

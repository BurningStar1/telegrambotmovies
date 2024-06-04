from LxmlSoup import LxmlSoup
import requests
from random import random, randint
import json
import requests
import pandas as pd
import bs4

headers = {
    # ИСТОЩЁН'X-API-KEY': '72a1abb3-7936-411f-a164-e43fcf62388f',
    # ИСТОЩЁН'X-API-KEY': '67dae962-f2d9-4a97-bc0d-77d9d981f2b2',
    # ИСТОЩЁН'X-API-KEY': '3fd25d96-2c5c-41d1-b28b-d6ba9345c39b',
    #'X-API-KEY': '096e8092-9c8a-45f4-9a8f-a90339f0472d',
    #  'X-API-KEY': 'f8a29f29-f4d3-473b-802a-423ae43174e7',
    # ИСТОЩЁН'X-API-KEY': 'adb76fb4-b6f2-4723-9c5f-522f73172207',
    #  'X-API-KEY': '2d7197af-4e12-490c-9b53-9b6a86973b39',
    #  'X-API-KEY': 'b104bb3b-b04b-49c4-a7ca-8ba3e2c2d45b', ОСТАНОВКА 2597
    'X-API-KEY': 'ab6012c7-ec2d-4d19-949c-1c2d30f31d1f'#, ещё начало с 258687 и плюс начало с Дюны часть вторая и ещё начало там с мстители война бесконечности
    # Api кей свой сделай по ссылке https://kinopoiskapiunofficial.tech/
    'Content-Type': 'application/json'
}

KPid = []  # ID КИНОПОИСК
NameFilm = []  # Название на русскому
NameFilmEn = []  # Название на английском
PosterUrl = []  # Фулл картинка
Description = []  # Описание
Countries = []  # Страна
ratingMpaa = []  # Возрастное ограничение
ratingAgeLimits = []  # Возрастное ограничение
Type = []  # Фильм или сериал
Year = []  # Год выпуска
Genres = []  # Жанры
ratingImdb = []  # Рейтинг Imdb
ratingKP = []  # Рейтинг Кинопоиска
filmLength = []  # Длительность в минутах
WebUrl = []  # https://w2.kpfr.wiki/film/ ссылка на просмотр
Genres1 = []
WebUrl2 = []

for j in range(1989, 1978, -1):
    for i in range(1, 100):
        ListMovies = requests.get(
            'https://kinopoiskapiunofficial.tech/api/v2.2/films?order=RATING&type=FILM&ratingFrom=0&ratingTo=10&yearFrom=' + str(
                j) + '&yearTo=' + str(j) + '&page=' + str(i),
            headers=headers)

        if ListMovies.status_code == 200:
            Str = ListMovies.json()

            for item in Str.get('items', []):
                print(item)
                KPid.append(item.get("kinopoiskId", ""))
                NameFilm.append(item.get("nameRu", ""))
                NameFilmEn.append(item.get("nameEn", ""))
                PosterUrl.append(item.get("posterUrl", ""))
                ratingKP.append(item.get("ratingKinopoisk", ""))
                ratingImdb.append(item.get("ratingImdb", ""))
                Year.append(item.get("year", ""))
                filmLength.append(item.get("filmLength", ""))
                Description.append(item.get("description", ""))
                ratingMpaa.append(item.get("ratingMpaa", ""))
                ratingAgeLimits.append(item.get("ratingAgeLimits", ""))
                WebUrl.append("https://w4.kpfr.wiki/film/" + str(item.get("kinopoiskId", "")) + "/")
                WebUrl2.append(item.get("webUrl", ""))

                countries = item.get("countries", [])
                country_names = [country.get("country", "") for country in countries]
                Countries.append(", ".join(country_names))

                genres = item.get("genres", [])
                genre_names = [genre.get("genre", "") for genre in genres]
                Genres.append(", ".join(genre_names))

                Type.append(item.get("type", ""))

data = {'KPid': KPid,
        'Type': Type,
        'NameFilm': NameFilm,
        'Year': Year,
        'Countries': Countries,
        'Genres': Genres,
        'ratingKP': ratingKP,
        'ratingImdb': ratingImdb,
        'ratingMpaa': ratingMpaa,
        'ratingAgeLimits': ratingAgeLimits,
        'Description': Description,
        'WebUrl': WebUrl,
        'WebUrl2': WebUrl2,
        'PosterUrl': PosterUrl
        }
df = pd.DataFrame(data)
# df.to_csv('MovieData.csv', index=False)

df.to_csv('MovieData_cleaned.csv', mode='a', header=False, index=False)

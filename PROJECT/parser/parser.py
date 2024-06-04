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
    'X-API-KEY': '096e8092-9c8a-45f4-9a8f-a90339f0472d',
    #  'X-API-KEY': 'f8a29f29-f4d3-473b-802a-423ae43174e7',
    # ИСТОЩЁН'X-API-KEY': 'adb76fb4-b6f2-4723-9c5f-522f73172207',
    #  'X-API-KEY': '2d7197af-4e12-490c-9b53-9b6a86973b39',
    #  'X-API-KEY': 'b104bb3b-b04b-49c4-a7ca-8ba3e2c2d45b', ОСТАНОВКА 2597
    #  'X-API-KEY': 'ab6012c7-ec2d-4d19-949c-1c2d30f31d1f', ещё начало с 258687 и плюс начало с Дюны часть вторая и ещё начало там с мстители война бесконечности
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

for i in range(843149, 842649, -1):

    response = requests.get('https://kinopoiskapiunofficial.tech/api/v2.2/films/' + str(i), headers=headers)
    #actors = requests.get('https://kinopoiskapiunofficial.tech/api/v1/staff?filmId=' + str(i), headers=headers)
    ListMovies = requests.get(
        'https://kinopoiskapiunofficial.tech/api/v2.2/films?order=RATING&type=FILM&ratingFrom=0&ratingTo=10&yearFrom=2024&yearTo=2024&page=1' + str(
            i), headers=headers)

    if response.status_code == 200:

        Str = response.json()
        WebUrl.append("https://w4.kpfr.wiki/film/" + str(i) + "/")
        for section, command in Str.items():
            if section == "kinopoiskId":
                KPid.append(command)
            if section == "nameRu":
                NameFilm.append(command)
            if section == "nameEn":
                NameFilmEn.append(command)
            if section == "posterUrl":
                PosterUrl.append(command)
            if section == "ratingKinopoisk":
                ratingKP.append(command)
            if section == "ratingImdb":
                ratingImdb.append(command)
            if section == "year":
                Year.append(command)
            if section == "filmLength":
                filmLength.append(command)
            if section == "description":
                Description.append(command)
            if section == "ratingMpaa":
                ratingMpaa.append(command)
            if section == "ratingAgeLimits":
                ratingAgeLimits.append(command)
            if section == "countries":
                Genres1 = ((str(command).replace("country", "").
                            replace(" ", "").replace("'", "").
                            replace("{", "").replace(":", "")).
                           replace("[", "").replace("}", "")).replace("]", "").split(",")
                Countries.append(Genres1)
            if section == "genres":
                Genres1 = ((str(command).replace("genre", "").
                            replace(" ", "").replace("'", "").
                            replace("{", "").replace(":", "")).
                           replace("[", "").replace("}", "")).replace("]", "").split(",")
                Genres.append(Genres1)
            if section == "type":
                Type.append(command)
            if section == "webUrl":
                WebUrl2.append(command)

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

# print(KPid, Type, NameFilm, NameFilmEn, Year, Countries, Genres,
# ratingKP, ratingImdb, AverageRating, ratingMpaa, ratingAgeLimits, Description, WebUrl)


# my_file = open("data.txt", "a+")
#
# # 341 строка баг выдаёт. Надо проверить с какого фильмы начинаются (c 0 до 301 пройтись, мб там раньше что-то было)
# # Также я создал заранее файл data.txt Не уверен что он в режиме a+ сразу норм заработает
# # Файл data.txt заполнен с 301 по 340
# for movie_id in range(298, 1001):
#     response = requests.get('https://kinopoiskapiunofficial.tech/api/v2.2/films/' + str(movie_id), headers=headers)
#     if response.status_code == 200:
#         print(response.json())
#         my_file.write(str(response.json()) + '\n')
#     else:
#         print(f'Ошибка {response.status_code}: {response.text}')
# my_file.close()

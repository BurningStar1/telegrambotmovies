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
    #ИСТОЩЁН'X-API-KEY': '096e8092-9c8a-45f4-9a8f-a90339f0472d',
      #ИСТОЩЁН'X-API-KEY': 'f8a29f29-f4d3-473b-802a-423ae43174e7',
    # ИСТОЩЁН'X-API-KEY': 'adb76fb4-b6f2-4723-9c5f-522f73172207',
     #ИСТОЩЁН'X-API-KEY': '2d7197af-4e12-490c-9b53-9b6a86973b39',
    #ИСТОЩЁН 'X-API-KEY': 'b104bb3b-b04b-49c4-a7ca-8ba3e2c2d45b',
    #ИСТОЩЁН'X-API-KEY': 'ab6012c7-ec2d-4d19-949c-1c2d30f31d1f', #ещё начало с 258687 и плюс начало с Дюны часть вторая и ещё начало там с мстители война бесконечности ОСТАНОВКА 2597
    #ИСТОЩЁН'X-API-KEY': '0edb28f6-f148-4625-9c57-2672c6cfdcdc',
    #ИСТОЩЁН'X-API-KEY': 'b0065b7d-c169-457a-8714-a28b9d8ea046',
    #ИСТОЩЁН'X-API-KEY': 'd3227578-f951-4d2a-81be-e5c02826987e',
    #ИСТОЩЁН'X-API-KEY': '1c50cc62-298d-4bfc-81e7-4fbcabc1ff3a',
    #ИСТОЩЁН'X-API-KEY': '559ebb5e-e93c-4c33-aab0-3e61b9e41af6',
    #ИСТОЩЁН'X-API-KEY': '23f3ce81-1106-47d1-92c6-4550710cfded',
    'X-API-KEY': 'fc750daa-02e9-40ab-a426-ca16141f7157',
    # 'X-API-KEY': '574641dd-9801-4bc8-b8a9-6b7841de4151',
    # 'X-API-KEY': '7ec5ffb4-5226-452e-9a22-0ac3d5484d3e',
    # 'X-API-KEY': 'd646b928-3d54-4ba3-b4ce-fdc335fe1b2a',

    'Content-Type': 'application/json'
}

# Загрузите данные из CSV файла
df = pd.read_csv('MovieData_cleaned_with_staff.csv')

# Укажите индекс строки, с которой нужно начать заполнение
start_index = 4119  # замените 2246 на нужный индекс

# Обработка каждой строки DataFrame, начиная с указанного индекса
for index in range(start_index, len(df)):
    film_id = df.at[index, df.columns[0]]
    response = requests.get(f'https://kinopoiskapiunofficial.tech/api/v1/staff?filmId={film_id}', headers=headers)

    if response.status_code == 200:
        staff_data = response.json()

        directors = []
        actors = []

        for staff_member in staff_data:
            profession = staff_member.get('professionKey')
            name = staff_member.get('nameRu') or staff_member.get('nameEn')

            if profession == 'DIRECTOR':
                directors.append(name)
            elif profession == 'ACTOR':
                actors.append(name)

        # Обновите соответствующие столбцы
        df.at[index, 'Directors'] = ', '.join(directors)
        df.at[index, 'Actors'] = ', '.join(actors)

# Сохраните обновленные данные обратно в CSV файл
df.to_csv('MovieData_cleaned_with_staff.csv', index=False)

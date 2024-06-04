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
    #  'X-API-KEY': 'ab6012c7-ec2d-4d19-949c-1c2d30f31d1f', ещё начало с 258687 и плюс начало с Дюны часть вторая и ещё начало там с мстители война бесконечности ОСТАНОВКА 2597
    'Content-Type': 'application/json'
}

# Загрузите данные из CSV файла
df = pd.read_csv('MovieData_cleaned.csv')

# Выберите столбец, из которого нужно выводить значения
first_column = df.columns[0]

# Укажите индекс строки, с которой нужно начать вывод
start_index = 3882  # замените 2246 на нужный индекс

# Убедитесь, что индекс находится в допустимом диапазоне
if 0 <= start_index < len(df):
    for index in range(start_index, len(df)):
        film_id = df.at[index, df.columns[0]]
        response = requests.get('https://kinopoiskapiunofficial.tech/api/v2.2/films/' + str(film_id), headers=headers)

        if response.status_code == 200:
            film_data = response.json()
            print(film_data)
            df.at[index, 'Description'] = film_data.get('description', '')

            df.at[index, 'ratingMpaa'] = film_data.get('ratingMpaa', '')

            df.at[index, 'ratingAgeLimits'] = film_data.get('ratingAgeLimits', '')

            df.at[index, 'WebUrl2'] = film_data.get('webUrl', '')

    # Сохраните обновленные данные обратно в CSV файл
    df.to_csv('MovieData_cleaned.csv', index=False)
    print("Данные обновлены и сохранены в 'MovieData_cleaned_updated.csv'.")
else:
    print("Указанный индекс строки находится вне диапазона")

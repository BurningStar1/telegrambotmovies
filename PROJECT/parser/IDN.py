# import pandas as pd
#
# # Загрузите данные из CSV файла
# df = pd.read_csv('MovieData_cleaned.csv')
#
# # Подсчитайте количество строк в DataFrame
# num_rows = df.shape[0]
#
# # Получите значение ячейки в первом столбце и последней строке
# if num_rows > 0:
#     first_column_last_row_value = df.iloc[-1, 0]
# else:
#     first_column_last_row_value = None
#
# print(f"Количество строк в CSV файле: {num_rows}")
# print(f"Значение ячейки в первом столбце и последней строке: {first_column_last_row_value}")
#
# import pandas as pd
#
# # Загрузите данные из CSV файла
# df = pd.read_csv('MovieData_cle.csv')
#
# # Укажите название столбца, по которому нужно проверять наличие значений
# column_name = 'NameFilm'  # замените 'NameFilm' на название нужного столбца
#
# # Удалите строки, в которых отсутствует значение в указанном столбце
# df_cleaned = df.dropna(subset=[column_name])
#
# # Сохраните очищенные данные обратно в CSV файл
# df_cleaned.to_csv('MovieData_cleaned.csv', index=False)
#
# print(f"Строки с отсутствующими значениями в столбце '{column_name}' удалены и сохранены в 'output_cleaned.csv'.")

# import pandas as pd
#
# # Загрузите данные из CSV файла
# df = pd.read_csv('MovieData_cleaned_with_staff.csv')
#
# # Функция для удаления квадратных скобок и кавычек, а также преобразования в строку
# def format_column_values(value):
#     if isinstance(value, str) and value.startswith("[") and value.endswith("]"):
#         # Удалите квадратные скобки и кавычки, затем разделите и соедините элементы через запятую
#         formatted_value = value[1:-1].replace("'", "").split(", ")
#         return ", ".join(formatted_value)
#     return value
#
# # Примените функцию к столбцам 'Genres' и 'Countries'
# df['Genres'] = df['Genres'].apply(format_column_values)
# df['Countries'] = df['Countries'].apply(format_column_values)
#
# # Сохраните обновленные данные обратно в CSV файл
# df.to_csv('MovieData_cleaned_formatted.csv', index=False)
#
# print("Данные обновлены и сохранены в 'MovieData_cleaned_formatted.csv'.")


# import pandas as pd
#
# # Открываем CSV-файл
# df = pd.read_csv('MovieData_cleaned_formatted.csv')
#
# # Преобразуем столбцы Countries и Genres в формат списка
# df['Countries'] = df['Countries'].str.split(', ')
# df['Genres'] = df['Genres'].str.split(', ')
#
# # Сохраняем изменения в CSV-файле
# df.to_csv('MovieData.csv', index=False)


import pandas as pd

# Открываем CSV-файл
df = pd.read_csv('MovieData.csv')

# Удаляем строки, в которых столбец Genres пустой
df = df.dropna(subset=['Genres'])

# Сохраняем изменения в CSV-файле
df.to_csv('output.csv', index=False)

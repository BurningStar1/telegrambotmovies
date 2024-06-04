import pandas as pd

# Загрузите данные из CSV файла
df = pd.read_csv('MovieData_cleaned_with_staff.csv')

# Удалите дубликаты по первому столбцу
df_cleaned = df.drop_duplicates(subset=df.columns[0], keep='first')

# Сохраните очищенные данные обратно в CSV файл
df_cleaned.to_csv('MovieData_cleaned_with_staff.csv', index=False)

print("Дубликаты по первому столбцу удалены и данные сохранены в 'MovieData_cleaned_no_duplicates.csv'.")

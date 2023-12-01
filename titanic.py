# titanic.py

import pandas as pd
from catboost.datasets import titanic

# Загрузка данных о пассажирах "Титаника"
train_df, _ = titanic()
titanic_dataset = train_df.copy()

# Заполнение пропущенных значений в поле "Age" средним значением
titanic_dataset['Age'].fillna(titanic_dataset['Age'].mean(), inplace=True)

# Создание нового признака с использованием one-hot-encoding для поля "Sex"
titanic_dataset = pd.get_dummies(titanic_dataset, columns=['Sex'], drop_first=True)

# Сохранение датасета в CSV файл
titanic_dataset.to_csv("titanic_dataset_updated.csv", index=False)


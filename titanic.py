try:
    import pandas as pd
    from catboost.datasets import titanic
except ModuleNotFoundError:
    print("Some required modules are not installed. Installing them now...")
    # Установка pandas и catboost
    try:
        import subprocess
        subprocess.check_call(['pip', 'install', 'pandas', 'catboost'])
    except Exception as e:
        print(f"Failed to install required modules: {e}")
        exit(1)

# Загрузка данных о пассажирах "Титаника"
train_df, _ = titanic()
titanic_dataset = train_df.copy()

# Создание нового датасета с информацией о классе, поле и возрасте
additional_info = pd.DataFrame({
    'Pclass': [1, 2, 3],
    'Sex': ['male', 'female', 'male'],
    'Age': [30, 25, 22]
})

# Объединение датасетов
titanic_dataset_extended = pd.concat([titanic_dataset, additional_info], axis=1)

# Сохранение расширенного датасета в CSV файл
titanic_dataset_extended.to_csv("titanic_dataset_extended.csv", index=False)


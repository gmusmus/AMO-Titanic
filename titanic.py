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

    # Попробуйте импортировать снова после установки
    import pandas as pd
    from catboost.datasets import titanic

# Остальной код вашего скрипта
# ...

# Загрузка данных о пассажирах "Титаника"
train_df, _ = titanic()
titanic_dataset = train_df.copy()

# Сохранение датасета в CSV файл
titanic_dataset.to_csv("titanic_dataset.csv", index=False)


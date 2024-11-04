import pandas as pd

def load_and_process_data(filepath):
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл '{filepath}' пуст.")
        return None
    except pd.errors.ParserError:
        print(f"Ошибка: Не удалось прочитать файл '{filepath}'.")
        return None

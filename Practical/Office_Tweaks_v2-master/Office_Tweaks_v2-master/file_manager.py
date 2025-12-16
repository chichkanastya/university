import os
from tqdm import tqdm


def find_files_for_deletion(directory, mode, pattern):
    all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    to_delete = []

    for f in all_files:
        if mode == 'startswith' and f.startswith(pattern):
            to_delete.append(f)
        elif mode == 'endswith' and f.endswith(pattern):
            to_delete.append(f)
        elif mode == 'contains' and pattern in f:
            to_delete.append(f)
        elif mode == 'extension':
            clean_pattern = pattern.strip('.')
            if f.endswith('.' + clean_pattern):
                to_delete.append(f)

    return to_delete


def delete_files(directory, file_list):
    if not file_list:
        print("Нет файлов для удаления.")
        return

    deleted_count = 0
    for filename in tqdm(file_list, desc="Удаление файлов"):
        try:
            os.remove(os.path.join(directory, filename))
            print(f"Файл: \"{filename}\" успешно удалён!")
            deleted_count += 1
        except OSError as e:
            print(f"Не удалось удалить {filename}: {e}")

    print(f"\nОперация завершена. Удалено файлов: {deleted_count}")

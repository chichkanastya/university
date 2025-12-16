import os

def print_separator():
    print("-" * 40)

def get_valid_int_input(prompt, min_val, max_val):
    while True:
        try:
            val = input(prompt)
            if not val:
                continue
            num = int(val)
            if min_val <= num <= max_val:
                return num
            else:
                print(f"Ошибка: введите число от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: это не число. Попробуйте снова.")

def confirm_action(message):
    response = input(f"{message} (y/n): ").lower()
    return response == 'y'

def get_files_by_ext(directory, extensions):
    files = []
    try:
        for f in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, f)):
                if f.lower().endswith(tuple(extensions)):
                    files.append(f)
    except OSError as e:
        print(f"Ошибка чтения каталога: {e}")
    return files

import os
import file_manager
import converter
import image_processor
import utils


def change_directory_interactive():
    current = os.getcwd()
    print(f"Текущий каталог: {current}")
    new_path = input("Укажите новый путь: ")
    if os.path.isdir(new_path):
        try:
            os.chdir(new_path)
            print(f"Каталог изменен на: {os.getcwd()}")
        except Exception as e:
            print(f"Ошибка: {e}")
    else:
        print("Ошибка: путь не существует или это не папка.")


def convert_pdf_interactive():
    files = utils.get_files_by_ext(os.getcwd(), ['.pdf'])
    if not files:
        print("PDF файлы не найдены.")
        return

    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    choice = utils.get_valid_int_input("Введите номер файла (0 для всех): ", 0, len(files))

    if choice == 0:
        targets = files
    else:
        targets = [files[choice - 1]]

    for f in targets:
        converter.convert_single_pdf_to_docx(os.path.join(os.getcwd(), f))


def convert_docx_interactive():
    files = utils.get_files_by_ext(os.getcwd(), ['.docx'])
    if not files:
        print("DOCX файлы не найдены.")
        return

    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    choice = utils.get_valid_int_input("Введите номер файла (0 для всех): ", 0, len(files))

    if choice == 0:
        targets = files
    else:
        targets = [files[choice - 1]]

    for f in targets:
        converter.convert_single_docx_to_pdf(os.path.join(os.getcwd(), f))


def compress_images_interactive():
    exts = ['.jpg', '.jpeg', '.png', '.gif']
    files = utils.get_files_by_ext(os.getcwd(), exts)
    if not files:
        print("Изображения не найдены.")
        return

    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    choice = utils.get_valid_int_input("Введите номер файла (0 для всех): ", 0, len(files))
    quality = utils.get_valid_int_input("Введите качество сжатия (1-100): ", 1, 100)

    if choice == 0:
        targets = files
    else:
        targets = [files[choice - 1]]

    for f in targets:
        image_processor.compress_single_image(os.path.join(os.getcwd(), f), quality)


def delete_files_interactive():
    print("\nВыберите критерий удаления:")
    print("1. Начинающиеся на подстроку")
    print("2. Заканчивающиеся на подстроку")
    print("3. Содержащие подстроку")
    print("4. По расширению")

    choice = utils.get_valid_int_input("Введите номер действия: ", 1, 4)
    pattern = input("Введите подстроку/расширение: ")

    modes = {1: 'startswith', 2: 'endswith', 3: 'contains', 4: 'extension'}
    mode = modes[choice]

    to_delete = file_manager.find_files_for_deletion(os.getcwd(), mode, pattern)

    if not to_delete:
        print("Файлы не найдены.")
        return

    print("\nБудут удалены:")
    for f in to_delete:
        print(f"- {f}")

    if utils.confirm_action("Вы уверены?"):
        file_manager.delete_files(os.getcwd(), to_delete)
    else:
        print("Операция отменена.")


def start_interactive_mode():
    while True:
        utils.print_separator()
        print("=== Office Tweaks v1.0 (Интерактивный режим) ===")
        print(f"Текущий каталог: {os.getcwd()}")
        print("\nВыберите действие:")
        print("0. Сменить рабочий каталог")
        print("1. Преобразовать PDF в Docx")
        print("2. Преобразовать Docx в PDF")
        print("3. Произвести сжатие изображений")
        print("4. Удалить группу файлов")
        print("5. Выход")

        choice = utils.get_valid_int_input("\nВаш выбор: ", 0, 5)

        if choice == 0:
            change_directory_interactive()
        elif choice == 1:
            convert_pdf_interactive()
        elif choice == 2:
            convert_docx_interactive()
        elif choice == 3:
            compress_images_interactive()
        elif choice == 4:
            delete_files_interactive()
        elif choice == 5:
            print("Выход.")
            break
            
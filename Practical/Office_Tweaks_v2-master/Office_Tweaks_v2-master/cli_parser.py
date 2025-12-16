import argparse
import os
import sys
from tqdm import tqdm
import utils
import converter
import image_processor
import file_manager


def check_quality(value):
    ivalue = int(value)
    if not 1 <= ivalue <= 100:
        raise argparse.ArgumentTypeError(f"{value} не является корректным значением качества (1-100)")
    return ivalue


def create_parser():
    parser = argparse.ArgumentParser(description="Office Tweaks - утилита для работы с документами и изображениями.")

    parser.add_argument('-i', '--interactive', action='store_true', help="Запустить в интерактивном режиме.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--pdf2docx',
                       help="Конвертировать PDF в DOCX. Укажите путь к файлу или 'all' для всех в --workdir.")
    group.add_argument('--docx2pdf',
                       help="Конвертировать DOCX в PDF. Укажите путь к файлу или 'all' для всех в --workdir.")
    group.add_argument('--compress-images',
                       help="Сжать изображения. Укажите путь к файлу или 'all' для всех в --workdir.")
    group.add_argument('--delete', action='store_true', help="Удалить файлы по критерию.")

    parser.add_argument('--workdir', help="Рабочий каталог для пакетной обработки ('all').")
    parser.add_argument('--quality', type=check_quality, help="Качество сжатия изображений (1-100).")

    parser.add_argument('--delete-mode', choices=['startswith', 'endswith', 'contains', 'extension'],
                        help="Режим удаления файлов.")
    parser.add_argument('--delete-pattern', help="Шаблон для удаления.")
    parser.add_argument('--delete-dir', help="Каталог, в котором производится удаление.")

    return parser


def handle_cli_args(args):
    print("Office Tweaks v1.0 - Пакетный режим")
    utils.print_separator()

    if args.pdf2docx:
        if args.pdf2docx == 'all':
            if not args.workdir or not os.path.isdir(args.workdir):
                print("Ошибка: для 'all' нужно указать корректный --workdir.")
                sys.exit(1)
            files = utils.get_files_by_ext(args.workdir, ['.pdf'])
            for f in tqdm(files, desc="Конвертация PDF->DOCX"):
                converter.convert_single_pdf_to_docx(os.path.join(args.workdir, f))
        else:
            converter.convert_single_pdf_to_docx(args.pdf2docx)

    elif args.docx2pdf:
        if args.docx2pdf == 'all':
            if not args.workdir or not os.path.isdir(args.workdir):
                print("Ошибка: для 'all' нужно указать корректный --workdir.")
                sys.exit(1)
            files = utils.get_files_by_ext(args.workdir, ['.docx'])
            for f in tqdm(files, desc="Конвертация DOCX->PDF"):
                converter.convert_single_docx_to_pdf(os.path.join(args.workdir, f))
        else:
            converter.convert_single_docx_to_pdf(args.docx2pdf)

    elif args.compress_images:
        if not args.quality:
            print("Ошибка: для сжатия необходимо указать --quality.")
            sys.exit(1)
        if args.compress_images == 'all':
            if not args.workdir or not os.path.isdir(args.workdir):
                print("Ошибка: для 'all' нужно указать корректный --workdir.")
                sys.exit(1)
            exts = ['.jpg', '.jpeg', '.png', '.gif']
            files = utils.get_files_by_ext(args.workdir, exts)
            for f in tqdm(files, desc="Сжатие изображений"):
                image_processor.compress_single_image(os.path.join(args.workdir, f), args.quality)
        else:
            image_processor.compress_single_image(args.compress_images, args.quality)

    elif args.delete:
        if not all([args.delete_mode, args.delete_pattern, args.delete_dir]):
            print("Ошибка: для удаления нужны --delete-mode, --delete-pattern и --delete-dir.")
            sys.exit(1)
        if not os.path.isdir(args.delete_dir):
            print(f"Ошибка: каталог для удаления не найден - {args.delete_dir}")
            sys.exit(1)

        files_to_delete = file_manager.find_files_for_deletion(args.delete_dir, args.delete_mode, args.delete_pattern)
        if not files_to_delete:
            print("Файлы по заданному критерию не найдены.")
            return

        print("Следующие файлы будут удалены:")
        for f in files_to_delete:
            print(f"- {f}")

        if utils.confirm_action("Подтвердите удаление"):
            file_manager.delete_files(args.delete_dir, files_to_delete)
        else:
            print("Операция отменена пользователем.")

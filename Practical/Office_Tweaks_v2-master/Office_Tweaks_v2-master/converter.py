import os
import sys
from tqdm import tqdm

try:
    from pdf2docx import Converter
except ImportError:
    Converter = None

try:
    from docx2pdf import convert as docx_to_pdf_convert
except ImportError:
    docx_to_pdf_convert = None


def convert_single_pdf_to_docx(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"Ошибка: файл не найден - {pdf_path}")
        return False

    docx_file = pdf_path.rsplit('.', 1)[0] + ".docx"

    counter = 1
    while os.path.exists(docx_file):
        docx_file = pdf_path.rsplit('.', 1)[0] + f"_{counter}.docx"
        counter += 1

    try:
        cv = Converter(pdf_path)
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        print(f"Успешно: {pdf_path} -> {docx_file}")
        return True
    except Exception as e:
        print(f"Ошибка при конвертации {pdf_path}: {e}")
        return False


def convert_single_docx_to_pdf(docx_path):
    if not os.path.exists(docx_path):
        print(f"Ошибка: файл не найден - {docx_path}")
        return False

    try:
        docx_to_pdf_convert(docx_path)
        print(f"Успешно сконвертирован: {docx_path}")
        return True
    except Exception as e:
        print(f"Ошибка при конвертации {docx_path}: {e}")
        print("Убедитесь, что MS Word установлен и закрыт.")
        return False

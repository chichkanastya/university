# Office Tweaks



## Что умеет?
- Смена рабочего каталога (в интерактивном режиме)
- Конвертация PDF <-> DOCX
- Сжатие изображений (JPEG, PNG, GIF)
- Массовое удаление файлов по критериям

## Установка
1. Склонировать репозиторий: ``
2. Python 3.10+
3. Создайте и активируйте виртуальное окружение:
   `python -m venv venv`
   `venv\Scripts\activate` (для Windows)
4. Установите зависимости:
   `pip install -r requirements.txt`

## Запуск

### Интерактивный режим
Запустите без аргументов или с флагом `-i`:
```bash
python office_tweaks.py
# или
python office_tweaks.py --interactive
```

### Режим командной строки (CLI)

#### Конвертация
```bash
# Один файл PDF в DOCX
python office_tweaks.py --pdf2docx "C:\docs\report.pdf"

# Все DOCX файлы в папке в PDF
python office_tweaks.py --docx2pdf all --workdir "C:\docs"
```

#### Сжатие изображений
```bash
# Одно изображение с качеством 75
python office_tweaks.py --compress-images "photo.jpg" --quality 75

# Все изображения в папке
python office_tweaks.py --compress-images all --workdir "C:\images" --quality 85
```

#### Удаление файлов
```bash
# Удалить все файлы с расширением docx в папке Temp
python office_tweaks.py --delete --delete-mode extension --delete-pattern docx --delete-dir "C:\Temp"

# Удалить все файлы, начинающиеся с "backup_"
python office_tweaks.py --delete --delete-mode startswith --delete-pattern "backup_" --delete-dir "C:\archive"
```

## Сборка EXE
Для сборки исполняемого файла используйте PyInstaller:
```bash
pyinstaller --onefile --console --name Office_Tweaks office_tweaks.py
```

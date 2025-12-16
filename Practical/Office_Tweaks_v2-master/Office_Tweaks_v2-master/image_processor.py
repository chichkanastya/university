import os
from tqdm import tqdm

try:
    from PIL import Image
except ImportError:
    Image = None


def compress_single_image(image_path, quality):
    if not os.path.exists(image_path):
        print(f"Ошибка: файл не найден - {image_path}")
        return False

    try:
        img = Image.open(image_path)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        dir_name = os.path.dirname(image_path)
        base_name = os.path.basename(image_path)
        new_name = os.path.join(dir_name, "compressed_" + base_name)

        img.save(new_name, quality=quality, optimize=True)

        old_size = os.path.getsize(image_path)
        new_size = os.path.getsize(new_name)
        saving = (1 - new_size / old_size) * 100

        print(f"Сжато: {base_name} ({old_size / 1024:.1f} KB -> {new_size / 1024:.1f} KB, экономия {saving:.1f}%)")
        return True
    except Exception as e:
        print(f"Ошибка обработки {image_path}: {e}")
        return False

#!/usr/bin/env python3
import subprocess
from pathlib import Path


def generate_qrc_file(icons_dir: Path, qrc_file: Path) -> None:
    """Генерирует QRC файл для всех SVG иконок в указанной директории."""
    qrc_content = ['<!DOCTYPE RCC><RCC version="1.0">', "<qresource>"]

    for icon in icons_dir.glob("*.svg"):
        if not icon.is_file():
            continue
        # Убираем префикс пути для чистоты
        relative_path = icon.relative_to(icons_dir.parent).as_posix()
        qrc_content.append(f"    <file>{relative_path}</file>")

    qrc_content.append("</qresource>")
    qrc_content.append("</RCC>")

    with qrc_file.open("w", encoding="utf-8") as f:
        f.write("\n".join(qrc_content))
    print(f"Сгенерирован {qrc_file}")


def compile_qrc(qrc_file: Path, output_file: Path) -> None:
    """Компилирует QRC файл в Python модуль с помощью pyside6-rcc."""
    cmd = ["pyside6-rcc", str(qrc_file), "-o", str(output_file)]
    try:
        subprocess.run(cmd, check=True)
        print(f"Скомпилирован {output_file}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ошибка компиляции QRC: {e}")


def main():
    # Путь к папке с иконками
    project_root = Path(__file__).parent.parent
    icons_dir = project_root / "src" / "ArboKit" / "resources" / "icons"
    qrc_file = project_root / "src" / "ArboKit" / "resources" / "icons.qrc"
    output_file = project_root / "src" / "ArboKit" / "resources" / "icons_rc.py"

    if not icons_dir.exists():
        raise FileNotFoundError(f"Директория иконок {icons_dir} не найдена")

    generate_qrc_file(icons_dir, qrc_file)
    compile_qrc(qrc_file, output_file)


if __name__ == "__main__":
    main()

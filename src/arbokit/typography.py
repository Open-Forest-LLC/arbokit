from pathlib import Path
from typing import Optional

from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QApplication


class Typography:
    """Управление шрифтами для ArboKit UI Kit."""

    BRAND: Optional[QFont] = None
    BASE: Optional[QFont] = None
    H1: Optional[QFont] = None
    H2: Optional[QFont] = None

    @staticmethod
    def create_font(family: str, size: int, weight: QFont.Weight = QFont.Weight.Normal) -> QFont:
        font = QFont(family, size)
        font.setWeight(weight)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        return font

    @classmethod
    def initialize(cls, font_file: Optional[Path] = None) -> None:
        """Инициализация шрифтов."""
        font_family = "Inter"

        if font_file is None:
            font_file = Path(__file__).parent / "resources" / "fonts" / "Inter-V.ttf"

        print(f"Загрузка шрифта: {font_file}")
        if font_file.exists():
            font_id = QFontDatabase.addApplicationFont(str(font_file))
            if font_id == -1:
                raise RuntimeError(f"Не удалось загрузить шрифт из {font_file}")
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        else:
            raise FileNotFoundError(f"Шрифт не найден: {font_file}")

        dpi_scale = QApplication.primaryScreen().logicalDotsPerInch() / 96.0

        cls.BRAND = cls.create_font(font_family, int(24 * dpi_scale), QFont.Weight.ExtraBold)
        cls.BASE = cls.create_font(font_family, int(10 * dpi_scale), QFont.Weight.Normal)
        cls.H1 = cls.create_font(font_family, int(14 * dpi_scale), QFont.Weight.Bold)
        cls.H2 = cls.create_font(font_family, int(12 * dpi_scale), QFont.Weight.Medium)

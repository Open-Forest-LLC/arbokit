import logging
from pathlib import Path
from typing import Optional

from PySide6.QtGui import QFont, QFontDatabase

logger = logging.getLogger(__name__)


class Typography:
    """Управление шрифтами для ArboKit UI Kit."""

    BRAND: Optional[QFont] = None
    BASE: Optional[QFont] = None
    H1: Optional[QFont] = None

    @staticmethod
    def create_font(family: str, size: int, weight: QFont.Weight = QFont.Weight.Normal) -> QFont:
        font = QFont(family, size)
        font.setWeight(weight)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        return font

    @classmethod
    def initialize(cls) -> None:
        """Инициализация шрифтов."""
        logger.debug("Инициализация шрифтов...")
        font_family = "Arial"
        font_file = Path(__file__).parent / "resources" / "fonts" / "Inter-V.ttf"

        if font_file.exists():
            font_id = QFontDatabase.addApplicationFont(str(font_file))
            if font_id != -1:
                font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
                logger.info(f"Шрифт '{font_family}' загружен.")
            else:
                logger.error(f"Не удалось загрузить шрифт из {font_file}.")
        else:
            logger.error(f"Шрифт не найден: {font_file}.")

        cls.BRAND = cls.create_font(font_family, 24, QFont.Weight.ExtraBold)
        cls.BASE = cls.create_font(font_family, 10, QFont.Weight.Normal)
        cls.H1 = cls.create_font(font_family, 14, QFont.Weight.Bold)

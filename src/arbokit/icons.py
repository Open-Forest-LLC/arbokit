from pathlib import Path
from typing import Dict

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPainter, QColor


class Icons:
    """Динамическая генерация иконок."""
    _ICONS: Dict[str, str] = {}

    @classmethod
    def load_icons(cls) -> None:
        """Загружает пути к SVG-иконкам из resources/icons."""
        icon_dir = Path(__file__).parent / "resources" / "icons"
        for svg in icon_dir.glob("*.svg"):
            cls._ICONS[svg.stem] = str(svg)

    @classmethod
    def get_icon(cls, name: str) -> QIcon:
        """Возвращает иконку по имени."""
        if not cls._ICONS:
            cls.load_icons()
        if name not in cls._ICONS:
            raise ValueError(f"Иконка '{name}' не найдена")
        return QIcon(cls._ICONS[name])

    @classmethod
    def create_colored_icon(cls, name: str, color: str, size: QSize = QSize(16, 16)) -> QIcon:
        """Создает иконку с заданным цветом."""
        icon = cls.get_icon(name)
        pixmap = icon.pixmap(size)
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.SourceIn)  # type: ignore[attr-defined]
        painter.fillRect(pixmap.rect(), QColor(color))
        painter.end()
        return QIcon(pixmap)

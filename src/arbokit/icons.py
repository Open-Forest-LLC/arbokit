from typing import Optional, ClassVar
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QColor, QPixmap, QPainter, Qt
from PySide6.QtSvg import QSvgRenderer


class IconProvider:
    """Управление иконками из QRC ресурсов."""

    _renderer_cache: ClassVar[dict[str, QSvgRenderer]] = {}
    DEFAULT_ICON_SIZE = QSize(16, 16)

    @classmethod
    def get_icon(cls, name: str, size: Optional[QSize] = None) -> QIcon:
        """Возвращает иконку по имени (без .svg)."""
        resource_path = f":/icons/{name}.svg"
        print(f"Загрузка иконки: {resource_path}")
        if not QSvgRenderer(resource_path).isValid():
            raise ValueError(f"Иконка '{name}' не найдена в ресурсах")

        icon = QIcon(resource_path)
        if size:
            pixmap = icon.pixmap(size)
            icon = QIcon(pixmap)
        return icon

    @classmethod
    def get_colored_icon(cls, name: str, color: str, size: QSize = DEFAULT_ICON_SIZE) -> QIcon:
        """Создаёт иконку с заданным цветом."""
        resource_path = f":/icons/{name}.svg"
        print(f"Загрузка цветной иконки: {resource_path}")

        if resource_path not in cls._renderer_cache:
            renderer = QSvgRenderer(resource_path)
            if not renderer.isValid():
                raise ValueError(f"Иконка '{name}' не найдена")
            cls._renderer_cache[resource_path] = renderer

        renderer = cls._renderer_cache[resource_path]
        pixmap = QPixmap(size)
        pixmap.fill(Qt.transparent)  # type: ignore[attr-defined]
        painter = QPainter(pixmap)
        try:
            renderer.render(painter)
            painter.setCompositionMode(QPainter.CompositionMode_SourceIn)  # type: ignore[attr-defined]
            painter.fillRect(pixmap.rect(), QColor(color))
        finally:
            painter.end()

        return QIcon(pixmap)

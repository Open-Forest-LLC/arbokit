from contextlib import contextmanager
from typing import Iterator

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

from arbokit.colors import Colors


class Palettes:
    """Управление цветовыми палитрами для светлой и темной тем."""

    @staticmethod
    def light_palette() -> QPalette:
        """Создает палитру для светлой темы."""
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(Colors.BACKGROUND_MAIN))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(Colors.PRIMARY))
        palette.setColor(QPalette.ColorRole.Base, QColor(Colors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(Colors.P10))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(Colors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(Colors.PRIMARY))
        palette.setColor(QPalette.ColorRole.Text, QColor(Colors.PRIMARY))
        palette.setColor(QPalette.ColorRole.Button, QColor(Colors.P20))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(Colors.PRIMARY))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(Colors.SUCCESS))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(Colors.BACKGROUND))
        return palette

    @staticmethod
    def dark_palette() -> QPalette:
        """Создает палитру для темной темы."""
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(Colors.PRIMARY))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(Colors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.Base, QColor("#2B2B2B"))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#3C3C3C"))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(Colors.PRIMARY))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(Colors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.Text, QColor(Colors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.Button, QColor(Colors.PRIMARY))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(Colors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(Colors.BRAND))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(Colors.BACKGROUND))
        return palette

    @classmethod
    @contextmanager
    def apply_theme(cls, app: QApplication, palette: QPalette) -> Iterator[None]:
        """Применяет палитру к приложению с возможностью отката."""
        old_palette = app.palette()
        app.setPalette(palette)
        try:
            yield
        finally:
            app.setPalette(old_palette)

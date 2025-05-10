from typing import Iterator

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication
from contextlib import contextmanager
from arbokit.colors import ThemeColors


class Palettes:
    """Управление цветовыми палитрами для светлой и темной тем."""

    @staticmethod
    def light_palette() -> QPalette:
        """Создает палитру для светлой темы."""
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(ThemeColors.BACKGROUND_MAIN))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.ColorRole.Base, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(ThemeColors.P10))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.ColorRole.Text, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.ColorRole.Button, QColor(ThemeColors.P20))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(ThemeColors.SUCCESS))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(ThemeColors.BACKGROUND))
        return palette

    @staticmethod
    def dark_palette() -> QPalette:
        """Создает палитру для темной темы."""
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.Base, QColor("#2B2B2B"))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#3C3C3C"))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.Text, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.Button, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(ThemeColors.BRAND))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(ThemeColors.BACKGROUND))
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

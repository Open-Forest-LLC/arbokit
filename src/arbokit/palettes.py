from PySide6.QtGui import QPalette, QColor

from PySide6.QtWidgets import QApplication
from arbokit.colors import ThemeColors
from contextlib import contextmanager


class Palettes:
    """Управление цветовыми палитрами для светлой и темной тем."""

    @staticmethod
    def light_palette() -> QPalette:
        """Создает палитру для светлой темы."""
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(ThemeColors.BACKGROUND_MAIN))
        palette.setColor(QPalette.WindowText, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.Base, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.AlternateBase, QColor(ThemeColors.P10))
        palette.setColor(QPalette.ToolTipBase, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.ToolTipText, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.Text, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.Button, QColor(ThemeColors.P20))
        palette.setColor(QPalette.ButtonText, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.Highlight, QColor(ThemeColors.SUCCESS))
        palette.setColor(QPalette.HighlightedText, QColor(ThemeColors.BACKGROUND))
        return palette

    @staticmethod
    def dark_palette() -> QPalette:
        """Создает палитру для темной темы."""
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.WindowText, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.Base, QColor("#2B2B2B"))
        palette.setColor(QPalette.AlternateBase, QColor("#3C3C3C"))
        palette.setColor(QPalette.ToolTipBase, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.ToolTipText, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.Text, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.Button, QColor(ThemeColors.PRIMARY))
        palette.setColor(QPalette.ButtonText, QColor(ThemeColors.BACKGROUND))
        palette.setColor(QPalette.Highlight, QColor(ThemeColors.BRAND))
        palette.setColor(QPalette.HighlightedText, QColor(ThemeColors.BACKGROUND))
        return palette

    @classmethod
    @contextmanager
    def apply_theme(cls, app: QApplication, palette: QPalette):
        """Применяет палитру к приложению с возможностью отката."""
        old_palette = app.palette()
        app.setPalette(palette)
        try:
            yield
        finally:
            app.setPalette(old_palette)

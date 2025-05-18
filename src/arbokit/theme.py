from contextlib import contextmanager
from typing import Dict, Iterator

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

from .colors import Colors


class Theme:
    """Управление темами приложения."""

    _palette_configs: Dict[str, Dict[QPalette.ColorRole, str]] = {
        "light": {
            QPalette.ColorRole.Window: "BACKGROUND_MAIN",  # #F9FAFB
            QPalette.ColorRole.WindowText: "PRIMARY",  # #353535
            QPalette.ColorRole.Base: "BACKGROUND",  # #FFFFFF
            QPalette.ColorRole.AlternateBase: "P10",
            QPalette.ColorRole.ToolTipBase: "BACKGROUND",
            QPalette.ColorRole.ToolTipText: "PRIMARY",
            QPalette.ColorRole.Text: "PRIMARY",  # #353535
            QPalette.ColorRole.Button: "P20",
            QPalette.ColorRole.ButtonText: "PRIMARY",  # #353535
            QPalette.ColorRole.Highlight: "SUCCESS",
            QPalette.ColorRole.HighlightedText: "BACKGROUND",
        },
        "dark": {
            QPalette.ColorRole.Window: "PRIMARY",  # #353535
            QPalette.ColorRole.WindowText: "BACKGROUND",  # #FFFFFF
            QPalette.ColorRole.Base: "#2B2B2B",
            QPalette.ColorRole.AlternateBase: "#3C3C3C",
            QPalette.ColorRole.ToolTipBase: "PRIMARY",
            QPalette.ColorRole.ToolTipText: "BACKGROUND",
            QPalette.ColorRole.Text: "BACKGROUND",  # #FFFFFF
            QPalette.ColorRole.Button: "PRIMARY",
            QPalette.ColorRole.ButtonText: "BACKGROUND",  # #FFFFFF
            QPalette.ColorRole.Highlight: "BRAND",
            QPalette.ColorRole.HighlightedText: "BACKGROUND",
        },
    }

    @classmethod
    def create_palette(cls, theme_name: str) -> QPalette:
        """Создаёт палитру для указанной темы."""
        if theme_name not in cls._palette_configs:
            raise ValueError(f"Тема '{theme_name}' не найдена")

        colors = Colors.load()
        print(f"Создание палитры для темы: {theme_name}")
        palette = QPalette()
        for role, color_key in cls._palette_configs[theme_name].items():
            if hasattr(colors, color_key):
                color_value = getattr(colors, color_key)
            else:
                color_value = color_key
            palette.setColor(role, QColor(color_value))
            print(f"Установка {role}: {color_value}")
        return palette

    @classmethod
    @contextmanager
    def apply_theme(cls, app: QApplication, theme_name: str) -> Iterator[None]:
        """Применяет тему с возможностью отката."""
        old_palette = app.palette()
        new_palette = cls.create_palette(theme_name)
        print(f"Применение палитры: {theme_name}")
        app.setPalette(new_palette)
        try:
            yield
        finally:
            print("Восстановление старой палитры")
            app.setPalette(old_palette)

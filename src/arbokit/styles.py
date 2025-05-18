from ArboKit.colors import Colors
from ArboKit.spacing import Spacing


class Styles:
    """Генерация QSS-стилей для UI компонентов."""

    @staticmethod
    def button_base_style(
        bg_color: str, hover_color: str, pressed_color: str, text_color: str, spacing: Spacing
    ) -> str:
        """Базовый стиль для кнопок."""
        return f"""
            QPushButton {{
                background-color: {bg_color};
                color: {text_color};
                border: none;
                padding: 4px 8px;
                border-radius: 4px;
                qproperty-iconSize: {spacing.L}px {spacing.L}px;
            }}
            QPushButton > QIcon {{
                color: {text_color};
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
            QPushButton:pressed {{
                background-color: {pressed_color};
            }}
        """

    @classmethod
    def styled_line_edit(
        cls, colors: Colors, spacing: Spacing, border_color: str = None, theme: str = "light"
    ) -> str:
        """Стиль для QLineEdit."""
        border_color = border_color or colors.P20
        text_color = colors.PRIMARY if theme == "light" else colors.BACKGROUND
        return f"""
            QLineEdit {{
                border: 1px solid {border_color};
                border-radius: {spacing.S}px;
                padding: {spacing.S}px;
                background-color: {colors.BACKGROUND};
                color: {text_color};
            }}
            QLineEdit:hover {{
                border: 1px solid {colors.P70};
                background-color: {colors.BACKGROUND_MAIN};
            }}
            QLineEdit:focus {{
                border: 1px solid {colors.BRAND};
                background-color: {colors.BACKGROUND};
            }}
            QLineEdit:disabled {{
                background-color: {colors.P10};
                color: {colors.P40};
                border: 1px solid {colors.P40};
            }}
        """

    @classmethod
    def success_button_style(cls, colors: Colors, spacing: Spacing, theme: str = "light") -> str:
        """Стиль для кнопок успеха."""
        text_color = colors.BACKGROUND if theme == "light" else colors.PRIMARY
        return cls.button_base_style(
            colors.SUCCESS,
            colors.SUCCESS_HOVER,
            colors.SUCCESS_PRESSED,
            text_color,
            spacing,
        )

    @classmethod
    def error_button_style(cls, colors: Colors, spacing: Spacing, theme: str = "light") -> str:
        """Стиль для кнопок ошибки."""
        text_color = colors.BACKGROUND if theme == "light" else colors.PRIMARY
        return cls.button_base_style(
            colors.ERROR,
            colors.ERROR_HOVER,
            colors.ERROR_PRESSED,
            text_color,
            spacing,
        )

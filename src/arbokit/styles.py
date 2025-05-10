from arbokit.colors import Colors
from arbokit.spacing import Spacing


class Styles:
    """Генерация QSS-стилей для UI компонентов."""

    Colors = Colors()
    Spacing = Spacing()

    @staticmethod
    def button_base_style(
        bg_color: str, hover_color: str, pressed_color: str, text_color: str
    ) -> str:
        """Базовый стиль для кнопок."""
        return f"""
            QPushButton {{
                background-color: {bg_color};
                color: {text_color};
                border: none;
                padding: 4px 8px;
                border-radius: 4px;
                qproperty-iconSize: {Styles.Spacing.DOUBLE_GRID}px {Styles.Spacing.DOUBLE_GRID}px;
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
    def styled_line_edit(cls, border_color: str = Colors.P20) -> str:
        """Стиль для QLineEdit."""
        return f"""
            QLineEdit {{
                border: 1px solid {border_color};
                border-radius: {cls.Spacing.HALF_GRID}px;
                padding: {cls.Spacing.HALF_GRID}px;
                background-color: {cls.Colors.BACKGROUND};
                color: {cls.Colors.PRIMARY};
            }}
            QLineEdit:hover {{
                border: 1px solid {cls.Colors.P70};
                background-color: {cls.Colors.BACKGROUND_MAIN};
            }}
            QLineEdit:focus {{
                border: 1px solid {cls.Colors.BRAND};
                background-color: {cls.Colors.BACKGROUND};
            }}
            QLineEdit:disabled {{
                background-color: {cls.Colors.P10};
                color: {cls.Colors.P40};
                border: 1px solid {cls.Colors.P40};
            }}
        """

    @classmethod
    def success_button_style(cls) -> str:
        """Стиль для кнопок успеха."""
        return cls.button_base_style(
            cls.Colors.SUCCESS,
            cls.Colors.SUCCESS_HOVER,
            cls.Colors.SUCCESS_PRESSED,
            cls.Colors.BACKGROUND,
        )

    @classmethod
    def error_button_style(cls) -> str:
        """Стиль для кнопок ошибки."""
        return cls.button_base_style(
            cls.Colors.ERROR,
            cls.Colors.ERROR_HOVER,
            cls.Colors.ERROR_PRESSED,
            cls.Colors.BACKGROUND,
        )

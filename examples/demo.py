from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ArboKit.colors import Colors
from ArboKit.icons import IconProvider
from ArboKit.spacing import Spacing
from ArboKit.styles import Styles
from ArboKit.theme import Theme
from ArboKit.typography import Typography


class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Инициализация DemoWindow")
        self.setWindowTitle("ArboKit UI Kit Demo")
        self.current_theme = "light"

        # Инициализация классов
        print("Загрузка Colors")
        self.colors = Colors.load()
        print("Инициализация Typography")
        Typography.initialize()
        print("Создание Spacing")
        self.spacing = Spacing()

        # Настройка центрального виджета и макета
        print("Настройка макета")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(self.spacing.S)
        layout.setContentsMargins(self.spacing.M, self.spacing.M, self.spacing.M, self.spacing.M)

        # Заголовок (H1)
        print("Создание заголовка")
        self.title = QLabel("ArboKit UI Kit")
        self.title.setFont(Typography.H1)
        self.title.setStyleSheet(f"color: {self.colors.PRIMARY};")
        layout.addWidget(self.title)

        # Поле ввода
        print("Создание поля ввода")
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите текст...")
        self.input_field.setFont(Typography.BASE)
        self.input_field.setStyleSheet(Styles.styled_line_edit(self.colors, self.spacing))
        layout.addWidget(self.input_field)

        # Кнопка с иконкой для переключения темы
        print("Создание кнопки переключения темы")
        self.theme_button = QPushButton("Переключить на тёмную тему")
        self.theme_button.setFont(Typography.BASE)
        self.theme_button.setIcon(IconProvider.get_colored_icon("settings", self.colors.SUCCESS, QSize(16, 16)))
        self.theme_button.setStyleSheet(Styles.success_button_style(self.colors, self.spacing))
        self.theme_button.clicked.connect(self.toggle_theme)
        layout.addWidget(self.theme_button)

        # Дополнительная кнопка с обычной иконкой
        print("Создание кнопки действия")
        self.action_button = QPushButton("Действие")
        self.action_button.setFont(Typography.BASE)
        self.action_button.setIcon(IconProvider.get_icon("add"))
        self.action_button.setStyleSheet(Styles.error_button_style(self.colors, self.spacing))
        layout.addWidget(self.action_button)

        # Растяжка для выравнивания
        layout.addStretch()

        # Применяем начальную тему
        print("Применение начальной темы")
        self.apply_theme()

    def toggle_theme(self):
        """Переключает между светлой и тёмной темой."""
        print("Переключение темы")
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.theme_button.setText(f"Переключить на {'тёмную' if self.current_theme == 'light' else 'светлую'} тему")
        self.apply_theme()

    def apply_theme(self):
        """Применяет текущую тему."""
        print("Применение темы:", self.current_theme)
        app = QApplication.instance()
        palette = Theme.create_palette(self.current_theme)
        app.setPalette(palette)
        app.processEvents()  # Принудительная обработка событий
        bg_color = self.colors.BACKGROUND_MAIN if self.current_theme == "light" else self.colors.PRIMARY
        self.centralWidget().setStyleSheet(f"QWidget {{ background-color: {bg_color}; }}")
        self.update_styles()

    def update_styles(self):
        """Обновляет стили для динамической смены темы."""
        print("Обновление стилей")
        text_color = self.colors.PRIMARY if self.current_theme == "light" else self.colors.BACKGROUND
        self.title.setStyleSheet(f"QLabel {{ color: {text_color}; }}")
        self.input_field.setStyleSheet(Styles.styled_line_edit(self.colors, self.spacing))
        self.theme_button.setStyleSheet(Styles.success_button_style(self.colors, self.spacing))
        self.action_button.setStyleSheet(Styles.error_button_style(self.colors, self.spacing))
        for widget in self.findChildren(QWidget):
            widget.update()
        self.centralWidget().update()

def main():
    print("Запуск приложения")
    app = QApplication([])
    window = DemoWindow()
    window.resize(400, 300)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()

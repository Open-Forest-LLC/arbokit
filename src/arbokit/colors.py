import json
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Colors:
    PRIMARY: str
    BRAND: str
    BACKGROUND_MAIN: str
    BACKGROUND: str
    P70: str
    P40: str
    P20: str
    P10: str
    SUCCESS: str
    SUCCESS_HOVER: str
    SUCCESS_PRESSED: str
    ERROR: str
    ERROR_HOVER: str
    ERROR_PRESSED: str
    WARNING: str
    WARNING_HOVER: str
    WARNING_PRESSED: str

    @staticmethod
    def _validate_hex(color: str) -> str:
        """Проверяет, что строка является валидным HEX-цветом."""
        if not re.match(r"^#[0-9A-Fa-f]{6}$", color):
            raise ValueError(f"Невалидный HEX-цвет: {color}")
        return color

    @classmethod
    def load(cls) -> "Colors":
        """Загружает цвета из JSON."""
        color_file = Path(__file__).parent / "resources" / "themes" / "colors.json"
        print(f"Попытка загрузки: {color_file}")
        if not color_file.exists():
            raise FileNotFoundError(f"Файл цветов {color_file} не найден")

        with color_file.open(encoding="utf-8") as f:
            colors = json.load(f)
        print(f"Загружены цвета: {colors}")

        # Проверяем, что все поля dataclass присутствуют
        required_fields = {f.name for f in cls.__dataclass_fields__.values()}
        missing_fields = required_fields - set(colors.keys())
        if missing_fields:
            raise ValueError(f"В {color_file} отсутствуют поля: {missing_fields}")

        # Валидация
        for color in colors.values():
            cls._validate_hex(color)

        return cls(**colors)

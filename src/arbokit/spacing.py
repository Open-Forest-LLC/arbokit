from dataclasses import dataclass


@dataclass(frozen=True)
class Spacing:
    """Константы отступов и размеров для UI компонентов."""

    BASE_GRID: int = 8

    XS: int = BASE_GRID // 2  # 4
    S: int = BASE_GRID  # 8
    M: int = BASE_GRID * 2  # 16
    L: int = BASE_GRID * 3  # 24
    XL: int = BASE_GRID * 4  # 32

    @classmethod
    def from_config(cls, base_grid: int = 8) -> "Spacing":
        """Создаёт Spacing с кастомной базовой сеткой."""
        return cls(BASE_GRID=base_grid)

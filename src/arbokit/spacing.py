from dataclasses import dataclass


@dataclass(frozen=True)
class Spacing:
    """Константы отступов и размеров для UI компонентов."""

    GRID: int = 8
    HALF_GRID: int = GRID // 2
    DOUBLE_GRID: int = GRID * 2
    TRIPLE_GRID: int = GRID * 3

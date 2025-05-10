import pytest
from PySide6.QtGui import QPalette, QColor
from arbokit.palettes import Palettes
from arbokit.colors import Colors


@pytest.mark.qt
def test_light_palette(qtbot):
    palette = Palettes.light_palette()
    assert palette.color(QPalette.Window) == QColor(Colors.BACKGROUND_MAIN)
    assert palette.color(QPalette.Highlight) == QColor(Colors.SUCCESS)


@pytest.mark.qt
def test_dark_palette(qtbot):
    palette = Palettes.dark_palette()
    assert palette.color(QPalette.Window) == QColor(
        Colors.PRIMARY)
    assert palette.color(QPalette.Base) == QColor("#2B2B2B")

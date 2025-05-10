import pytest
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication
from arbokit.palettes import Palettes
from arbokit.colors import Colors


@pytest.mark.qt
def test_light_palette(qtbot):
    try:
        palette = Palettes.light_palette()
        assert palette.color(QPalette.ColorRole.Window) == QColor(Colors.BACKGROUND_MAIN)
        assert palette.color(QPalette.ColorRole.Highlight) == QColor(Colors.SUCCESS)
    except Exception as e:
        pytest.fail(f"Test failed with exception: {str(e)}")


@pytest.mark.qt
def test_apply_theme(qtbot):
    app = QApplication.instance() or QApplication([])
    original_palette = app.palette()
    new_palette = Palettes.dark_palette()
    with Palettes.apply_theme(app, new_palette):
        assert app.palette().color(QPalette.ColorRole.Window) == QColor(Colors.PRIMARY)
    assert app.palette().color(QPalette.ColorRole.Window) == original_palette.color(QPalette.ColorRole.Window)

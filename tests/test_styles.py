from arbokit.styles import Styles
from arbokit.colors import Colors


def test_button_base_style():
    style = Styles.button_base_style(
        Colors.SUCCESS,
        Colors.SUCCESS_HOVER,
        Colors.SUCCESS_PRESSED,
        Colors.BACKGROUND
    )
    assert "background-color: #009345" in style
    assert "border-radius: 4px" in style


def test_styled_line_edit():
    style = Styles.styled_line_edit()
    assert f"border-radius: {Styles.Spacing.HALF_GRID}px" in style
    assert "background-color: #FFFFFF" in style

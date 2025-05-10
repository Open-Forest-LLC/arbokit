from arbokit.spacing import Spacing


def test_spacing():
    assert Spacing.GRID == 8
    assert Spacing.HALF_GRID == 4
    assert Spacing.DOUBLE_GRID == 16
    assert Spacing.TRIPLE_GRID == 24

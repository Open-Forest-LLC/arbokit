import pytest
from arbokit.typography import Typography


@pytest.mark.qt
def test_typography_initialization(qtbot):
    Typography.initialize()
    assert Typography.BRAND.pointSize() == 24

from PyQt5.QtCore import QRect
from wallpaste.monitors import *


def test_dual_widescreen():
    mon_a = QRect(0, 0, 1920, 1080)
    mon_b = QRect(1920, 0, 1920, 1080)
    result = scale_monitors([mon_a, mon_b], 600, 600)
    expected = [(0, 0, 300, 168), (300, 0, 300, 168)]
    assert result == expected


def test_single_widescreen():
    mon_a = QRect(0, 0, 1920, 1080)
    result = scale_monitors([mon_a], 600, 600)
    expected = [(0, 0, 600, 337)]
    assert result == expected


def test_dual_with_vertical():
    mon_a = QRect(0, 444, 1920, 1080)
    mon_b = QRect(1920, 0, 1080, 1920)
    result = scale_monitors([mon_a, mon_b], 700, 400)
    expected = [(0, 103, 447, 251), (447, 0, 251, 447)]
    assert result == expected

"""
Tests the Pixel module.
"""

from unittest.mock import Mock
from app.components.pixel import Pixel


def test_pixel_construction():
    """Tests construction of Pixel with valid and invalid arguments"""
    # Default construction args
    pixel = Pixel()
    assert pixel.position == (0, 0)
    assert pixel.color is Pixel.default_color

    # Valid construction args
    pixel = Pixel(pixel_x_idx=5, pixel_y_idx=5, color=None)
    assert pixel.position == (5, 5)
    assert pixel.color is Pixel.default_color

    # Negative x/y
    pixel = Pixel(pixel_x_idx=-5, pixel_y_idx=-5, color=None)
    assert pixel.position == (0, 0)
    assert pixel.color is Pixel.default_color


def test_render():
    """Tests the renderer object double dispatch call"""
    pixel = Pixel()
    renderer = Mock()
    pixel.render(renderer)
    renderer.render_pixel.assert_called_once_with(pixel=pixel)

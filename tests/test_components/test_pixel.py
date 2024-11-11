from app.components.pixel import Pixel
from unittest.mock import Mock
from app.renderers.color import Color


def test_pixel_construction():
    """Tests construction of Pixel with valid and invalid arguments"""
    # Default construction args
    pixel = Pixel()
    assert pixel.position == (0, 0)
    assert pixel.color is None

    # Valid construction args
    pixel = Pixel(x_pos=5, y_pos=5, color=None)
    assert pixel.position == (5, 5)
    assert pixel.color is None

    # Negative x/y
    pixel = Pixel(x_pos=-5, y_pos=-5, color=None)
    assert pixel.position == (0, 0)
    assert pixel.color is None


# def test_set_color():
#     pixel = Pixel()
#     color = Color(255, 0, 0)  # Assuming Color takes RGB values
#     pixel.set_color(color)
#     assert pixel.color == color


def test_render():
    """Tests the renderer object double dispatch call"""
    pixel = Pixel()
    renderer = Mock()
    pixel.render(renderer)
    renderer.render_pixel.assert_called_once_with(pixel=pixel)

"""
Terminal Renderer Test Module
"""

from app.renderers.terminal.terminal_renderer import TerminalRenderer
from app.components.pixel import Pixel


def test_initial_terminal_x_scale():
    """Tests construction Renderer object with valid and invalid arguments"""
    term_renderer = TerminalRenderer()
    assert term_renderer.get_terminal_x_scale == 3

    term_renderer = TerminalRenderer(terminal_x_scale=5)
    assert term_renderer.get_terminal_x_scale == 5

    term_renderer = TerminalRenderer(terminal_x_scale=0)
    assert term_renderer.get_terminal_x_scale == 1

    term_renderer = TerminalRenderer(terminal_x_scale=-5)
    assert term_renderer.get_terminal_x_scale == 1


def test_render_pixel(capsys):
    """Test the rendered output for a pixel"""
    pixel = Pixel(x_pos=2, y_pos=3)
    term_renderer = TerminalRenderer()
    term_renderer.render_pixel(pixel)
    captured = capsys.readouterr()
    assert captured.out == "\033[3;6H███\n"

import pytest
from app.renderers.terminal_renderer import TerminalRenderer
from app.components.pixel import Pixel


@pytest.fixture
def terminal_renderer():
    """Generate a default TerminalRenderer fixture for tests to use"""
    return TerminalRenderer()


def test_initial_terminal_x_scale(terminal_renderer):
    """Tests construction Renderer object with valid and invalid arguments"""
    terminal_renderer.set_terminal_x_scale(5)
    assert terminal_renderer.get_terminal_x_scale() == 5

    terminal_renderer.set_terminal_x_scale(0)
    assert terminal_renderer.get_terminal_x_scale() == 1

    terminal_renderer.set_terminal_x_scale(-5)
    assert terminal_renderer.get_terminal_x_scale() == 1


def test_cursor_locator(capsys, terminal_renderer):
    terminal_renderer._cursor_locator((2, 3))
    captured = capsys.readouterr()
    assert captured.out == "\033[3;6H"


def test_render_pixel(capsys, terminal_renderer):
    pixel = Pixel(x_pos=2, y_pos=3)
    terminal_renderer.render_pixel(pixel)
    captured = capsys.readouterr()
    assert captured.out == "\033[3;6H███\n"

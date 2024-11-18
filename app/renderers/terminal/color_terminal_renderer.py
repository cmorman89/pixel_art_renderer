"""
Color Terminal Renderer Module
"""

from typing import Optional

from app.components.pixel import Pixel
from app.renderers.utils.color import Color
from app.renderers.terminal.terminal_renderer import TerminalRenderer
from app.renderers.utils.run_buffer import RunBuffer


class ColorTerminalRenderer(TerminalRenderer):
    """
    Renders colored pixels to the terminal, respecting each pixel's color and position attributes.

    Inherits from `TerminalRenderer`

    Attributes:
        __color_buffer (Optional[Color]): Tracks the last Color used to act as a simple buffer to
            prevent repeated ANSI color calls and ANSI terminal resets when not needed.

    Methods:
        render_pixel: Triggers applying an ANSI color code to terminal (if needed) before calling
            `TerminalRenderer` to render the actual pixel.

    Inherits:
        Inherits from and delegates pixel rendering to the `Renderer` object `TerminalRenderer`.
    """

    def __init__(self, terminal_x_scale: int = 3):
        """
        Initializes the renderer by calling the parent `TerminalRenderer` constructor and
        setting up the color history buffer.

        Args:
            terminal_x_size (int): The scaling factor of horizontal terminal output. Defaults to 3.
        """
        super().__init__(terminal_x_scale)
        self._last_rendered_color: Optional[Color] = None

    def render_pixel(self, pixel: Pixel):
        """
        Renders a single pixel to the terminal at the correct position with the correct color.

        Steps:
            1. Sets the ANSI code based on the Pixel's color.
            2. Updates the color buffer
            3. Delegates rendering of the pixel to superclass `TerminalRenderer`

        Args:
            pixel (Pixel): The pixel to render to the terminal.
        """
        self._set_ansi_color_code(color=pixel.get_color())
        self._cache_last_used_color(color=pixel.get_color())
        super().render_pixel(pixel)

    def _set_ansi_color_code(self, color: Optional[Color] = None):
        """
        Uses the color buffer to check if a new color is needed, and applies the color to the
        terminal if so.

        Args:
            color (Optional[Color]): The color expected by the current pixel. Defaults to None.
        """
        if self._last_rendered_color is not color:
            ansi_code = color.value if color else Pixel.default_color
            super()._renderer_print(ansi_code)

    def _cache_last_used_color(self, color: Optional[Color] = None):
        """
        Caches the last used ANSI code to prevent reissue of duplicate codes.

        Args:
            color (Optional[Color]): The color expected by the current pixel. Defaults to None.
        """
        self._last_rendered_color = color

    def _render_run_buffer(self, run_buffer: RunBuffer):
        """
        Renders a completed RunBuffer to the terminal in color. Responsible for setting the color
        before delegating to Super to handle the rest of the rendering.

        Args:
            run_buffer (RunBuffer): The run buffer to render to the terminal.
        """
        self._set_ansi_color_code(run_buffer.color)
        super()._render_run_buffer(run_buffer)

    @staticmethod
    def reset_terminal_format():
        """
        Unsets any formatting applied to the terminal for future printed characters.
        """
        print(Color.RESET.value, end="")

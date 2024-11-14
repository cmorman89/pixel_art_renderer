"""
Terminal Renderer Module.

This module contains the TerminalRenderer class, which is responsible for rendering pixels to the
terminal. The TerminalRenderer class inherits from the Renderer base class and provides methods
to render individual pixels at specified locations in the terminal.

Classes:
    TerminalRenderer: Outputs the character representation of a single pixel to the terminal at the
        correct location.
"""

from typing import Tuple
from app.components.pixel import Pixel
from app.data.pixel_matrix import PixelMatrix
from app.renderers.renderer import Renderer


class TerminalRenderer(Renderer):
    """Outputs the character representation of a single pixel to the terminal at the correct
    location.

    Attributes:
        terminal_x_scale (int): The factor to scale the width-related calculations to compensate
            for differences in column and row size in the terminal. Defaults to 3.
        render_char (str): The character to use when printing the terminal output. Defaults to "█"
    """

    def __init__(self, terminal_x_scale: int = 3):
        """
        Constructs the renderer object, setting the x scale factor and the character to render
        for each pixel.

        Args:
            terminal_x_scale (int): The factor to scale the width-related calculations to compensate
                for differences in column and row size in the terminal. Defaults to 3.
        """
        self._set_terminal_x_scale(terminal_x_scale)
        self._render_char = "█"

    @property
    def get_terminal_x_scale(self) -> int:
        """
        Get the terminal x scale

        Returns:
            int: The x-scaling factor used by the renderer.
        """
        return self.__terminal_x_scale

    def _set_terminal_x_scale(self, scale: int):
        """
        Safely sets the terminal x_scale. Ensures a min of 1 character to prevent blank output.

        Args:
            scale (int): The scale to
        """
        self.__terminal_x_scale = max(1, scale)

    def render_pixel(self, pixel: Pixel):
        """
        Renders a single pixel to the terminal at a given location by printing the render
        character

        Args:
            pixel: The Pixel object to render to the terminal.
        """
        self._cursor_locator(position=pixel.position)
        print(self._render_char * self.__terminal_x_scale)

    def render_pixelmatrix(self, pixel_matrix: PixelMatrix):
        """
        Renders a PixelMatrix to the terminal

        Args:
            pixel: The Pixel object to render to the terminal.
        """

    def _cursor_locator(self, position: Tuple[int, int]):
        """
        Places the cursor in the correct position in the terminal to render the pixel in another
         step.

        Args:
            Position (Tuple[int, int]): The new (x, y) position to place the terminal cursor.

        Note:
            Move to own class if takes on any more responsibilities.
        """
        col = position[0] * self.__terminal_x_scale
        row = position[1]

        # ANSI escape sequence to reposition the cursor in the terminal
        print(f"\033[{row};{col}H", end="")

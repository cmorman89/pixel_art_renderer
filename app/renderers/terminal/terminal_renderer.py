"""
Terminal Renderer Module.

This module contains the TerminalRenderer class, which is responsible for rendering pixels to the
terminal. The TerminalRenderer class inherits from the Renderer base class and provides methods
to render individual pixels at specified locations in the terminal.

Classes:
    TerminalRenderer: Outputs the character representation of a single pixel to the terminal at the
        correct location.
"""

import sys
from typing import Tuple, Optional

from app.components.pixel import Pixel
from app.data.pixel_matrix import PixelMatrix
from app.renderers.renderer import Renderer
from app.renderers.utils.run_buffer import RunBuffer
from app.renderers.utils.run_buffer_builder import RunBufferBuilder


class TerminalRenderer(Renderer):
    """Outputs the character representation of a single pixel to the terminal at the correct
    location.

    Attributes:
        terminal_x_scale (int): The factor to scale the width-related calculations to compensate
            for differences in column and row size in the terminal. Defaults to 3.
        render_char (str): The character to use when printing the terminal output. Defaults to "█"
    """

    def __init__(self, terminal_x_scale: int = 3):
        """Constructs the renderer object, setting the x scale factor and the character to render
        for each pixel.

        Args:
            terminal_x_scale (int): The factor to scale the width-related calculations to compensate
                for differences in column and row size in the terminal. Defaults to 3.
        """
        self._set_terminal_x_scale(terminal_x_scale)
        self._render_char = "█"
        self._none_char = " "

    @property
    def get_terminal_x_scale(self) -> int:
        """Get the terminal x scale.

        Returns:
            int: The x-scaling factor used by the renderer.
        """
        return self._terminal_x_scale

    def _set_terminal_x_scale(self, scale: int):
        """Safely sets the terminal x_scale. Ensures a min of 1 character to prevent blank output.

        Args:
            scale (int): The scale to
        """
        self._terminal_x_scale = max(1, scale)

    def set_render_char(self, render_char: Optional[str] = "█"):
        """
        Set the character to use when rendering a pixel to the terminal.

        Args:
            render_char (Optional[str]): The basic character to use when rendering a pixel.
                Defaults to "█".

        Notes:
                Only the first character of the passed `render_char` string is used. The rest is
                discarded.
        """
        self._render_char = render_char[:1] if render_char else "█"

    def render_pixel(self, pixel: Pixel):
        """Renders a single pixel to the terminal at a given location by printing the render
        character.

        Args:
            pixel: The Pixel object to render to the terminal.
        """
        self._cursor_locator(position=pixel.position)
        print(self._render_char * self._terminal_x_scale)

    def render_pixelmatrix(self, pixel_matrix: PixelMatrix):
        """Renders a PixelMatrix to the terminal by rendering the RunBuffers returned from passing
        Pixels to a RunBufferBuilder object.

        Args:
            pixel_matrix (PixelMatrix): The PixelMatrix object to render to the terminal.
        """
        self._cursor_locator(position=(0, 0))
        # Step 1: Create the RunBufferBuilder
        buffer_builder = RunBufferBuilder()

        # Step 2:  Pre-expand rendered character strings
        pixel_rendered_chars = self._render_char * self.get_terminal_x_scale
        pixel_none_chars = self._none_char * self.get_terminal_x_scale

        # Step 3: Iterate pixels and pass into buffer builder
        for matrix_y_idx, row in enumerate(pixel_matrix.matrix):
            for matrix_x_idx, pixel in enumerate(row):
                # Handle 'None' cells in the PixelMatrix
                if pixel is None:
                    pixel = Pixel(pixel_x_idx=matrix_x_idx, pixel_y_idx=matrix_y_idx)
                    rendered_chars = pixel_none_chars
                else:
                    rendered_chars = pixel_rendered_chars
                # Check if  a completed RunBuffer has been returned
                pixel_run_buffer = buffer_builder.buffer_pixel(
                    pixel=pixel, rendered_chars=rendered_chars
                )
                if pixel_run_buffer:
                    # Render the RunBuffer immediately upon completion
                    self._render_run_buffer(run_buffer=pixel_run_buffer)

            # Add a newline between row transitions in the PixelMatrix data.
            if matrix_y_idx < pixel_matrix.height - 1:
                buffer_builder.buffer_string("\n")

    def _render_run_buffer(self, run_buffer: RunBuffer):
        """Print the run-length buffer to the terminal at the correct location.

        Args:
            run_buffer (RunBuffer): The RunBuffer obj to print.
            debug (bool): Flag for rendering in debug mode or not. Defaults to `False`.
        """
        self._cursor_locator(run_buffer.origin)
        self._renderer_print(f"{run_buffer}")

    def _cursor_locator(self, position: Tuple[int, int]):
        """Places the cursor in the correct position in the terminal to render the pixel in another
        step.

        Args:
            Position (Tuple[int, int]): The new (x, y) position to place the terminal cursor.

        Note:
            Move to own class if takes on any more responsibilities.
        """
        ansi_col = 1 + position[0] * self._terminal_x_scale
        ansi_row = 1 + position[1]

        # ANSI escape sequence to reposition the cursor in the terminal
        self._renderer_print(f"\033[{ansi_row};{ansi_col}H")

    def _renderer_print(self, data: str):
        sys.stdout.write(data)
        sys.stdout.flush()

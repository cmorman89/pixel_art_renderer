"""
Run-Length Buffer Builder Module

This module processes incoming data from the renderer to generate run-length buffers (`RunBuffers`)
by grouping pixels with similar formatting. This results in substantially improved efficiency as
ANSI codes can be issued once for a group of contiguous pixels, instead of once for every pixel.

Classes:
    RunBufferBuilder:  Builds the RunBuffer objects at render time by processing incoming data.
"""

from typing import Optional
from app.components.pixel import Pixel
from app.renderers.utils.color import Color
from app.renderers.utils.run_buffer import RunBuffer


class RunBufferBuilder:
    """Builds the RunBuffer objects at render time by processing incoming `Pixel` objects and `str`
    objects.
    """

    def __init__(self):
        """Initialize the run buffer builder to track the current Color in a buffer and holds the
        current RunBuffer.
        """
        self._buffered_color: Optional[Color] = None
        self._new_run_length_buffer: Optional[Color] = None
        self._old_run_length_buffer: Optional[RunBuffer] = None

    def buffer_pixel(self, pixel: Pixel, rendered_chars: str):
        """Orchestrate adding a pixel to a new buffer or an existing buffer.

        Args:
            pixel (Pixel): The Pixel object to buffer.
            rendered_chars (str): The characters that represent a pixel once rendered.

        Returns:
            RunBuffer: The RunBuffer once complete.
        """
        if pixel.get_color() is self._buffered_color:
            return self._add_to_existing_buffer(rendered_chars=rendered_chars)
        else:
            self._start_new_run_buffer(pixel=pixel)
            self._add_to_existing_buffer(rendered_chars=rendered_chars)
            return self._old_run_length_buffer

    def _add_to_existing_buffer(self, rendered_chars: str):
        """Add rendered characters to the current run-length buffer.

        Args:
            rendered_chars (str): The characters to add to the buffer.
        """
        self._new_run_length_buffer.add_to_buffer(data=rendered_chars)

    def _start_new_run_buffer(self, pixel: Pixel):
        """Orchestrate starting a new run-length buffer after storing the old buffer in
        `_old_run_length_buffer` attribute.

        Args:
            pixel (Pixel): The pixel to get format information from.
            rendered_chars (str): _description_
        """
        self._update_buffered_color(pixel_color := pixel.get_color())
        self._old_run_length_buffer = self._new_run_length_buffer
        self._new_run_length_buffer = RunBuffer(
            origin=pixel.position, color=pixel_color
        )

    def _update_buffered_color(self, color: Color):
        """Update the buffered color with the given color.

        Args:
            color (Color): The new color to set as the buffered color.
        """
        self._buffered_color = color

    def buffer_string(self, string_to_buffer: str):
        """Insert a string into the RunBuffer with minimal processing.

        Args:
            string (str): The string to add to the buffer.
        """
        self._new_run_length_buffer.add_to_buffer(string_to_buffer)

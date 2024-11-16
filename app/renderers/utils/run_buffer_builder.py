from typing import Optional
from app.components.pixel import Pixel
from app.renderers.utils.color import Color
from app.renderers.utils.run_buffer import RunBuffer


class RunBufferBuilder:
    """
    Builds the RunBuffer objects at render time by processing incoming `Pixel` objects and `str`
    objects.
    """

    def __init__(self):
        """
        Initializes the run buffer builder to track the current Color in a backbuffer and holds the
        current RunBuffer.
        """
        self._buffered_color: Optional[Color] = None
        self._new_run_length_buffer: Optional[RunBuffer] = None
        self._old_run_length_buffer: Optional[RunBuffer] = None

    def buffer_pixel(self, pixel: Pixel, rendered_chars: str):
        """
        Processes a pixel by determining if it is the start of a new RunBuffer or part of the old RunBuffer.

        Args:
            pixel (Pixel): _description_
            rendered_chars (str): _description_

        Returns:
            RunBuffer: The completed RunBuffer
        """

        if pixel.get_color is self._buffered_color:
            return self._add_to_existing_buffer(rendered_chars=rendered_chars)
        else:
            self._add_to_new_buffer(pixel=pixel, rendered_chars=rendered_chars)
            return self._old_run_length_buffer

    def _add_to_existing_buffer(self, rendered_chars: str):
        self._new_run_length_buffer.add_to_buffer(data=rendered_chars)

    def _add_to_new_buffer(self, pixel: Pixel, rendered_chars: str):
        self._update_buffered_color(pixel_color := pixel.get_color())
        self._old_run_length_buffer = self._new_run_length_buffer
        self._new_run_length_buffer = RunBuffer(
            origin=pixel.position, color=pixel_color
        )
        self._new_run_length_buffer.add_to_buffer(data=rendered_chars)
        return self._old_run_length_buffer

    def _update_buffered_color(self, color: Color):
        self._buffered_color = color

    def buffer_string(self, string_to_buffer: str):
        """
        Inserts a string into the RunBuffer with minimal processing.

        Args:
            string (str): _description_
        """
        self._new_run_length_buffer.add_to_buffer(string_to_buffer)

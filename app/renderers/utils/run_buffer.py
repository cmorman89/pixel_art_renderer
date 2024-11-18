"""
Run-Length Buffer Module

RunBuffers are used in all TerminalRenderer objects as the final element in the rendering pipeline.
Handles storage of buffered data and related attributes such as color and position. Logic is held
in the `RunBufferBuilder` class.

Classes:
    RunBuffer: Represents the run-length buffer. Handles storage of buffered data and related
    attributes such as color and position.
"""

from dataclasses import dataclass
from typing import Tuple
from app.renderers.utils.color import Color


@dataclass
class RunBuffer:
    """
    Represents the run-length buffer. Handles storage of buffered data and related attributes such
    as color and position.

    Attributes:
        origin (Tuple[int, int]): The (x_idx, y_idx) coordinate where the run-length buffer starts.
        buffer_data (str): The printable characters that make up the run-length buffer.
        color (Color): The color of all characters in the buffer.
    """

    origin: Tuple[int, int] = (0, 0)
    buffer_data: str = ""
    color: Color = None

    def add_to_buffer(self, data: str):
        """
        Adds the string data to the buffer with minimal processing.

        Args:
            data (str): The string to add to the buffer.
        """
        self.buffer_data += data

    def __str__(self):
        """
        Returns the RunBuffer data when called as a `string`.
        """
        return self.buffer_data

    def __repr__(self):
        """
        Generates a representational view of the RunBuffer with spaces as "_", and printed
        characters as "-". RunBuffers are bound within [brackets].

        Returns:
            str: The representational view of the RunBuffer.
        """

        repr_buffer_data = self.buffer_data.replace(" ", "_").replace("█", "-")
        truncate = (repr_buffer_data.count("\n") * 2) + 2
        return f"[{repr_buffer_data[truncate:]}]"

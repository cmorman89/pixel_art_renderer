"""
Pixel Component Module.

This module defines the `Pixel` class, which serves as the concrete leaf node in the object tree.
Each `Pixel` instance represents a single pixel in the output, maintaining its own color and
position data.

Classes:
    Pixel: Represents a single pixel with color and position attributes.
"""

from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Tuple
from app.components.renderable_component import RenderableComponent
from app.renderers.color import Color

# Break circular dependencies caused by type checking.
if TYPE_CHECKING:
    from app.renderers.renderer import Renderer


class Pixel(RenderableComponent):
    """Concrete object at the base of the object tree. Represents a single pixel in the output and
    its color and position data.

    Attributes:
        position (Tuple[int, int]): The relative (x, y) position of the pixel within its parent.
        color (Color): The render color of the pixel, if supported.
    """

    def __init__(self, x_pos: int = 0, y_pos: int = 0, color: Color = None):
        """Initializes the pixel color and position, ensuring a default is set.

        Args:
            x_pos (int): The relative x-coordinate of the pixel within its parent. Defaults to 0.
            y_pos (int): The relative y-coordinate of the pixel within its parent. Defaults to 0,
            color (Color): The color of the pixel. Defaults to None.
        """
        self.position: Tuple[int, int] = (0, 0)
        self.color = None

        # Set valid attributes
        self._set_position(x_pos=x_pos, y_pos=y_pos)
        self.set_color(color=color)

    def get_position(self) -> Tuple[int, int]:
        """Provides the position in (x, y) of the pixel.

        Returns:
            Tuple[int, int]: The relative (x, y) position of the pixel.
        """
        return self.position

    def get_color(self) -> Optional[Color]:
        """Provides the `Color` enum obj of the pixel.

        Returns:
            Optional[Color]: Returns the Color object of the pixel or None if not set.
        """
        return self.color

    def _set_position(self, x_pos: int = 0, y_pos: int = 0):
        """Updates the relative position of the pixel to a non-negative integer.

        Args:
            x_pos (int): The relative x-coordinate of the pixel within its parent.
            y_pos (int): The relative y-coordinate of the pixel within its parent.

        Note:
            Position should only be set during init, for now.
            Future: Consider Observers with PixelMatrixManager so that Pixel alerts
            PixelMatrixManager, which then puts Pixel in updated matrix location?
        """
        x_pos = max(0, x_pos)
        y_pos = max(0, y_pos)
        self.position = (x_pos, y_pos)

    def set_color(self, color: Optional[Color] = None):
        """Sets the color of the pixel.

        Args:
            color (Color): The color to set the pixel to.

        Note:
            Color can be safely changed at any point.
        """
        self.color = color

    def render(self, renderer: Renderer):
        """When visited by the renderer, calls Pixel's specific rendering method

        Args:
            renderer (Renderer): The Renderer object that will visit and render this pixel.
        """
        renderer.render_pixel(pixel=self)

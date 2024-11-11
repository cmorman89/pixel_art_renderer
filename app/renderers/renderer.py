"""
Renderer Abstract Base Class Module

This module defines the abstract base class `Renderer` for rendering pixel art. The `Renderer`
class provides an interface for rendering individual pixels to various types of output or display.

Classes:
    Renderer (ABC): Abstract base class for all Renderer objects.

    render_pixel (abstract method): Renders a single pixel to some type of output or display.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

# Break circular dependencies caused by type checking.
if TYPE_CHECKING:
    from app.components.pixel import Pixel


class Renderer(ABC):
    """Abstract base class for all Renderer objects, which visit and generate an output for
    RenderableComponent objects.

    Methods:
        render_pixel: Renders a single pixel to some type of output or display.
    """

    @abstractmethod
    def render_pixel(self, pixel: Pixel):
        """Renders a single pixel to some type of output or display.

        Args:
            pixel (Pixel): The Pixel to render to the output.
        """

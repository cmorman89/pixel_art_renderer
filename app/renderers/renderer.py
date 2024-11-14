"""
Renderer Abstract Base Class Module

This module defines the abstract base class `Renderer` for rendering pixel art. The `Renderer`
class provides an interface for rendering pixels to various types of outputs or displays.

Classes:
    Renderer (ABC): Abstract base class for all Renderer objects.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from app.data.pixel_matrix import PixelMatrix

# Break circular dependencies caused by type checking.
if TYPE_CHECKING:
    from app.components.pixel import Pixel


class Renderer(ABC):
    """
    Abstract base class for all Renderer objects, which visit and generate an output for
    RenderableComponent objects.

    Methods:
        render_pixel: Renders a single pixel to the renderer's display.
        render_pixelmatrix: Renders a pixel matrix to to the renderer's display.
    """

    @abstractmethod
    def render_pixel(self, pixel: Pixel):
        """
        Renders a single pixel to the renderer's display.

        Args:
            pixel (Pixel): The Pixel object to render.
        """

    @abstractmethod
    def render_pixelmatrix(self, pixel_matrix: PixelMatrix):
        """
        Renders a pixel matrix to to the renderer's display.

        Args:
            pixel_matrix (PixelMatrix): The PixelMatrix object to render.
        """

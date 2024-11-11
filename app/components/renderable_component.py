"""
Renderable Components Module

This module defines the RenderableComponent abstract base class, which serves as a blueprint for all
renderable or displayable objects within the application.

Classes:
    RenderableComponent: An abstract base class that requires implementing a render method to
        display the component using a Renderer object.
"""

from abc import ABC, abstractmethod
from app.renderers.renderer import Renderer


class RenderableComponent(ABC):
    """Abstract base class for all renderable/displayable objects for the application.

    Methods:
        render: Calls a Renderer visitor object to display the component.
    """

    @abstractmethod
    def render(self, renderer: "Renderer"):
        """Calls the specific implementation to render this component when visited by a renderer
        in a double-dispatch manner.

        Args:
            renderer: The renderer to use on this component.
        """

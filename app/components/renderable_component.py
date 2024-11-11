"""Module: components/renderable_components.py"""

from abc import ABC, abstractmethod
from app.renderers.renderer import Renderer


class RenderableComponent:
    """Abstract base class for all renderable/displayable objects for the application.

    Methods:
        render: Calls a Renderer visitor object to display the component.
    """

    @abstractmethod
    def render(self, renderer: "Renderer"):
        """Calls the Renderer object to process and render this component.

        Args:
            renderer: The renderer to use on this component.
        """

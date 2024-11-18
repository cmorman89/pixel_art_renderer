"""
Layer Component Module
"""

from typing import Optional, Tuple
from app.components.renderable_component import RenderableComponent
from app.data.pixel_matrix import PixelMatrix
from app.renderers.renderer import Renderer


class Layer(RenderableComponent):
    """Holds a PixelMatrix object that represents the data in the layer, and holds metadata such as
    layer name and position.

    Attributes:
        name (str): The name of the layer. Defaults to "Untitled Layer"
        pixel_matrix (PixelMatrix): The PixelMatrix that holds the pixel data for the layer.
            Initializes a blank PixelMatrix by default.


    Methods:
        set_pixel_matrix: Replaces the layer's instance of a PixelMatrix with a new one.
        update_name: Update the name of the layer.
        render: Render the layer's PixelMatrix.
        __getattr__: Access PixelMatrix methods to easily update the PixelMatrix object.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        pixel_matrix: Optional[PixelMatrix] = None,
        position: Optional[Tuple[int, int]] = (0, 0),
    ):
        """Constructs a Layer object with a name and PixelMatrix object.

        Args:
            name (Optional[str]): The name of the layer. Defaults to "Untitled Layer"
            pixel_matrix (Optional[PixelMatrix]): The PixelMatrix that holds the pixel data for the
                layer. Initializes a blank PixelMatrix by default.
            position (Optional[Tuple[int, int]])
        """
        self.name: str = name if name else "Untitled Layer"
        self.pixel_matrix: PixelMatrix = pixel_matrix if pixel_matrix else PixelMatrix()
        self.position: Tuple[int, int] = position if position else (0, 0)

    def update_name(self, new_name: Optional[str] = None):
        """Updates the layer's name to a given `str`.

        Args:
            new_name (str): The new name of the layer. Defaults to "Untitled Layer"
        """
        self.name = new_name if new_name else "Untitled Layer"

    def update_position(self, position: Tuple[int, int]):
        """Updates the position relative to its parent group or window.

        Args:
            position (Tuple[int, int]): The (x, y) coordinates for the origin point of the layer.
        """
        self.position = (max(0, position[0]), max(0, position[1]))

    def set_pixel_matrix(self, pixel_matrix: PixelMatrix):
        """Sets a PixelMatrix or replaces the existing PixelMatrix held by this layer.

        Args:
            pixel_matrix (PixelMatrix): The new PixelMatrix object to store in the layer.
        """
        self.pixel_matrix = pixel_matrix

    def __getattr__(self, pixel_matrix_method):
        """Dynamically passes any unknown method calls to the PixelMatrix object held in this
        layer. Returns an error if the PixelMatrix does not implement the requested method.

        Args:
            pixel_matrix_method: The name and arguments to pass to the PixelMatrix object.

        Raises:
            NotImplementedError: If a requested method call is not found in the PixelMatrix object.

        Returns:
            The requested method from the PixelMatrix object.
        """
        if hasattr(self.pixel_matrix, pixel_matrix_method):
            return getattr(self.pixel_matrix, pixel_matrix_method)
        raise NotImplementedError(
            f"{self.pixel_matrix.__class__.__name__} objet has no method `{pixel_matrix_method}`."
        )

    def render(self, renderer: Renderer):
        """When visited by the renderer, calls PixelMatrix's specific rendering method

        Args:
            renderer (Renderer): The Renderer object that will visit and render this pixel.
        """
        renderer.render_pixelmatrix(self.pixel_matrix)

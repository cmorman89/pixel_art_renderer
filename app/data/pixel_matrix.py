"""
PIxel Matrix Module

The pixel matrix module is responsible for holding the pixel data in a 2D matrix format, providing
a representational abstraction of the pixel data that can be used by the renderer. Storage in a 2D
matrix allows for constant time access and updates of pixels, making it efficient for rendering.

Classes:
    PixelMatrix: A class representing a 2D matrix of pixels.
"""

from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from app.components.pixel import Pixel
    from app.data.pixel_matrix_manager import PixelMatrixManager


class PixelMatrix:
    """
    Represents a 2D matrix of pixels, providing a structured way to store and access pixel data.

    Attributes:
        matrix (List[List[Pixel]]): A 2D matrix of Pixel objects.
        matrix_manager (PixelMatrixManager): A PixelMatrixManager object to handle matrix
            operations.

    Methods:
        sets_matrix_manager: Sets the PixelMatrixManager object to use for the PixelMatrix.
        add_pixel: Adds a pixel to the matrix via the matrix manager.
        get_pixel: Retrieves a pixel from the matrix via the matrix manager.
        move_pixel: Moves a pixel within the matrix via the matrix manager.
        clear_pixel: Clears a pixel from the matrix via the matrix manager.
    """

    def __init__(self, matrix_manager: Optional[PixelMatrixManager] = None):
        """
        Initializes the PixelMatrix with a [[None]] matrix. Optionally takes a PixelMatrixManager
        object to manage the matrix.

        Args:
            matrix_manager (Optional[PixelMatrixManager]): An optional PixelMatrixManager object.
                Defaults to a basic PixelMatrixManager object if not set initially.
        """
        self._matrix = [[None]]
        self._matrix_manager = (
            PixelMatrixManager() if matrix_manager is None else matrix_manager
        )

    def sets_matrix_manager(self, matrix_manager: PixelMatrixManager):
        """
        Sets the PixelMatrixManager object to use for the PixelMatrix.

        Args:
            matrix_manager (PixelMatrixManager): The PixelMatrixManager object to attach.
        """
        self._matrix_manager = matrix_manager

    def add_pixel(self, pixel: Pixel):
        """
        Adds a pixel to the matrix via the matrix manager.

        Args:
            pixel (Pixel): The Pixel object to add to the matrix.
        """
        self._matrix_manager.add_pixel(self, pixel)

    def get_pixel(self, pixel_x_idx: int, pixel_y_idx: int) -> Union[Pixel, None]:
        """
        Retrieves a pixel from the matrix via the matrix manager.

        Args:
            pixel_x_idx (int): The x-index of the pixel to retrieve.
            pixel_y_idx (int): The y-index of the pixel to retrieve.

        Returns:
            Union[Pixel, None]: The Pixel or None object found at the given indices.
        """
        return self._matrix_manager.get_pixel(self, pixel_x_idx, pixel_y_idx)

    def move_pixel(self, x_old: int, y_old: int, x_new: int, y_new: int):
        """
        Moves a pixel within the matrix via the matrix manager.

        Args:
            x_old (int): The x-index of the pixel to move.
            y_old (int): The y-index of the pixel to move.
            x_new (int): The new x-index of the pixel.
            y_new (int): The new y-index of the pixel.
        """
        self._matrix_manager.move_pixel(
            self,
            pixel_x_idx_old=x_old,
            pixel_y_idx_old=y_old,
            pixel_x_idx_new=x_new,
            pixel_y_idx_new=y_new,
        )

    def clear_pixel(self, pixel_x_idx: int, pixel_y_idx: int):
        """
        Clears a pixel from the matrix via the matrix manager.

        Args:
            pixel_x_idx (int): The x-index of the pixel to clear.
            pixel_y_idx (int): The y-index of the pixel to clear.
        """
        self._matrix_manager.clear_pixel(self, pixel_x_idx, pixel_y_idx)

    @property
    def matrix(self) -> List[List[Pixel]]:
        """
        Provides the 2D matrix of Pixel objects.

        Returns:
            List[List[Pixel]]: A 2D matrix of Pixel objects.
        """
        return self._matrix

    @property
    def width(self) -> int:
        """
        Provides the width of the matrix. Measured to ensure integrity.

        Returns:
            int: The width of the matrix.

        Note:
            Cache into internal attribute if performance becomes a problem.
        """
        return len(self.matrix[0])

    @property
    def height(self) -> int:
        """
        Provides the height of the matrix. Measured to ensure integrity.

        Returns:
            int: The height of the matrix.

        Note:
            Cache into internal attribute if performance becomes a problem.
        """
        return len(self.matrix)

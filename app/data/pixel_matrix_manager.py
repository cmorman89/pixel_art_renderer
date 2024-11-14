"""
Pixel Matrix Manager Module

The PixelMatrixManager module is responsible for managing operations on a pixel matrix, including
adding, moving, and clearing pixels, as well as resizing the matrix as needed. This module is
designed to be used by the PixelMatrix class to handle the manipulation of pixel data.

Classes:
    PixelMatrixManager: A class that manages operations on a pixel matrix.
"""

from __future__ import annotations
from typing import Union, TYPE_CHECKING
from app.components.pixel import Pixel

if TYPE_CHECKING:
    from app.data.pixel_matrix import PixelMatrix


class PixelMatrixManager:
    """
    Manages operations on a pixel matrix, including adding, moving, and clearing pixels,
    as well as resizing the matrix as needed.

    Methods:
        add_pixel: Adds a pixel to the pixel matrix.
        get_pixel: Retrieves a pixel from the pixel matrix.
        move_pixel: Moves a pixel within the pixel matrix.
        clear_pixel: Clears a pixel from the pixel matrix.
    """

    def add_pixel(self, pixel_matrix: PixelMatrix, pixel: Pixel):
        """
        Adds a pixel to the pixel matrix, triggering a matrix resize if required.

        Args:
            pixel_matrix (PixelMatrix): The PixelMatrix object that is being updated.
            pixel (Pixel): The Pixel object that will be added to the PixelMatrix.
        """
        pixel_x_idx = pixel.get_position()[0]
        pixel_y_idx = pixel.get_position()[1]
        self._resize_matrix(
            pixel_matrix=pixel_matrix, pixel_x_idx=pixel_x_idx, pixel_y_idx=pixel_y_idx
        )
        pixel_matrix.matrix[pixel_y_idx][pixel_x_idx] = pixel

    def get_pixel(
        self, pixel_matrix: PixelMatrix, pixel_x_idx: int, pixel_y_idx: int
    ) -> Union[Pixel, None]:
        """
        Safely get a Pixel (or None) from the matrix if it is within the matrix bounds, or return
        an error if outside of bounds.

        Args:
            pixel_matrix (PixelMatrix): The PixelMatrix to search.
            pixel_x_idx (int): The x-index to search in the PixelMatrix.
            pixel_y_idx (int): The y-index to search in the PixelMatrix.

        Returns:
            Union[Pixel, None]: The Pixel (or None) at the given position in the matrix.
        """
        self._validate_pixel_location(
            pixel_matrix=pixel_matrix, pixel_x_idx=pixel_x_idx, pixel_y_idx=pixel_y_idx
        )
        return pixel_matrix.matrix[pixel_y_idx][pixel_x_idx]

    def move_pixel(
        self,
        pixel_matrix: PixelMatrix,
        pixel_x_idx_old: int,
        pixel_y_idx_old: int,
        pixel_x_idx_new: int,
        pixel_y_idx_new: int,
    ):
        """
        Moves a pixel from one location in the matrix to another, setting the old location to
        a `None` value.

        Args:
            pixel_matrix (PixelMatrix): The PixelMatrix to update.
            pixel_x_idx_old (int): The x-index where the pixel can be found.
            pixel_y_idx_old (int): The y-index where the pixel can be found.
            pixel_x_idx_new (int): The x-index of where to move the pixel.
            pixel_y_idx_new (int): The y-index of where to move the pixel.
        """
        # Step 1: Check/get the Pixel to move
        moved_pixel = self.get_pixel(
            pixel_matrix=pixel_matrix,
            pixel_x_idx=pixel_x_idx_old,
            pixel_y_idx=pixel_y_idx_old,
        )

        # Step 2: Resize the PixelMatrix if needed
        self._resize_matrix(
            pixel_matrix=pixel_matrix,
            pixel_x_idx=pixel_x_idx_new,
            pixel_y_idx=pixel_y_idx_new,
        )

        # Step 3: Set the Pixel in the new position in the matrix
        pixel_matrix.matrix[pixel_y_idx_new][pixel_x_idx_new] = moved_pixel

        # Step 4: Clear the value in the position where the pixel used to be.
        self.clear_pixel(
            pixel_matrix=pixel_matrix,
            pixel_x_idx=pixel_x_idx_old,
            pixel_y_idx=pixel_y_idx_old,
        )

    def clear_pixel(
        self, pixel_matrix: PixelMatrix, pixel_x_idx: int, pixel_y_idx: int
    ):
        """
        Clears the pixel (sets to `None`) at the given position in the pixel matrix.

        Args:
            pixel_matrix (PixelMatrix): The PixelMatrix to update.
            pixel_x_idx (int): The x-index to clear in the PixelMatrix.
            pixel_y_idx (int): The y-index to clear in the PixelMatrix.
        """
        self._validate_pixel_location(
            pixel_matrix=pixel_matrix, pixel_x_idx=pixel_x_idx, pixel_y_idx=pixel_y_idx
        )
        pixel_matrix.matrix[pixel_y_idx][pixel_x_idx] = None
        self._resize_matrix(
            pixel_matrix=pixel_matrix, pixel_x_idx=pixel_x_idx, pixel_y_idx=pixel_y_idx
        )

    def _validate_pixel_location(
        self, pixel_matrix: PixelMatrix, pixel_x_idx: int, pixel_y_idx: int
    ):
        """


        Args:
            pixel_matrix (PixelMatrix): The PixelMatrix to search.
            pixel_x_idx (int): The x-index to check in the PixelMatrix.
            pixel_y_idx (int): The y-index to check in the PixelMatrix.

        Raises:
            IndexError: If trying to get a pixel outside maximum bounds of matrix.
            IndexError: If trying to get a pixel using a negative position coordinate.

        """
        if (
            pixel_x_idx + 1 > pixel_matrix.width
            or pixel_y_idx + 1 > pixel_matrix.height
        ):
            raise IndexError(
                f"Cannot access pixel data at ({pixel_x_idx}, {pixel_y_idx}) in PixelMatrix."
                + "Coordinates exceed matrix maximum bounds."
            )
        elif pixel_x_idx < 0 or pixel_y_idx < 0:
            raise IndexError(
                f"Cannot access pixel data at ({pixel_x_idx}, {pixel_y_idx}) in PixelMatrix."
                + "Coordinates cannot be negative."
            )

    def _resize_matrix(
        self, pixel_matrix: PixelMatrix, pixel_x_idx: int, pixel_y_idx: int
    ):
        """
        Orchestrates the resizing operations and checks of the PixelMatrix.

        Args:
            pixel_matrix (PixelMatrix): The PixelMatrix to check or resize.
            pixel_x_idx (int): The required x-index of the pixel.
            pixel_y_idx (int): The required y-index of the pixel.
        """
        pixel_col = pixel_x_idx + 1
        pixel_row = pixel_y_idx + 1
        self._expand_matrix_cols(pixel_matrix=pixel_matrix, pixel_col=pixel_col)
        self._expand_matrix_rows(pixel_matrix=pixel_matrix, pixel_row=pixel_row)

    def _expand_matrix_cols(self, pixel_matrix: PixelMatrix, pixel_col: int):
        """
        Checks if the matrix is at least as wide as required, and expands it if not.

        Args:
            pixel_matrix (PixelMatrix): The PixelMatrix to expand.
            pixel_col (int): The minimum required width.
        """
        matrix_width = pixel_matrix.width
        if pixel_col > matrix_width:
            for row in pixel_matrix.matrix:
                row.extend([None] * (pixel_col - matrix_width))

    def _expand_matrix_rows(self, pixel_matrix: PixelMatrix, pixel_row: int):
        """
        Checks if the matrix is at least as tall as required, and expands it if not.

        Args:
            pixel_matrix (PixelMatrix): The PixelMatrix to expand.
            pixel_row (int): The minimum required height.
        """
        matrix_height = pixel_matrix.height
        matrix_width = pixel_matrix.width
        if pixel_row > matrix_height:
            for _ in range(pixel_row - matrix_height):
                pixel_matrix.matrix.append([None] * matrix_width)

    def _contract_matrix(self):
        pass

# Pixel Art Renderer

Renders pixel art to the terminal


<!-- ## Structure
### Components
 - `RenderableComponent(ABC)`: Abstract base class that represents all graphic objects and their basic methods.
    - Methods:
        - `render`: Accepts the Renderer visitor to generate an output of this component.
            - Args:
                - `renderer` (`Renderer`): The renderer used to render this component.

 - `Pixel (RenderableComponent)`: Base of the object tree. Represents a single pixel and its color and position in the pixel art output.
     - Attributes:
        - `position` (`[x: int, y: int]`): Relative [x, y] position of pixel within its parent. Defaults to `[0,0]`
        - `color` (`Color`): Holds the color information of pixel. 
    - Methods:
        - `set_position`: Updates the relative pixel position in x, y.
            - Args:
                - `x` (`int`): The new x coordinate. Defaults to 0.
                - `y` (`int`): The new y coordinate. Defaults to 0.
        - `set_color`: Updates the pixel color.
            - Args:
                - `color` (`Optional[Color]`): The new color of the pixel. Optional, defaults to `None`

 - `RenderableGroup(RenderableComponent)` Abstract class for all composite components
    - Attributes:
        - `children` (`RenderableComponent`):
        - `width` (`int`):
        - `height` (`int`):
    - Methods:
        - `add`:
        - `_update_dimensions`


 - `Layer`:  Concrete `RenderableGroup` class that represents a single layer on a canvas.
    - Attributes:
        - `pixel_matrix` (`PixelMatrix`):
    - Methods:
        - `_add_pixel` (`int`):
        - `_add_child` (`int`):
    - Inherits:
        - Inherits from 

 - `Canvas()`
    - Attributes:
        - `_default_layer` (`Layer`):
        - `layers` -->
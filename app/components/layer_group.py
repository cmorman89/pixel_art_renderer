from typing import Tuple, List, Optional
from app.components.layer import Layer


class LayerGroup:

    # TODO: Create a `Positionable` class?
    def __init__(
        self,
        name: Optional[str] = None,
        position: Optional[Tuple[int, int]] = None,
        layer: Optional[Layer] = None,
    ):
        self.name: str = name if name else "Untitled Group"
        self.position: Tuple[int, int] = (
            (max(0, position[0]), max(0, position[1])) if position else (0, 0)
        )
        self.layer_stack: List[Optional[Layer]] = [layer] if layer else []

    def add_layer(self, layer: Layer):
        self.layer_stack.append(Layer)

    def remove_layer(
        self, layer_name: Optional[str] = None, layer_idx: Optional[int] = None
    ):
        if layer_name:
            self.layer_stack

    def reorder_layer(self, old_priority, new_priority):
        pass

    def update_name(self, new_name: str):
        pass

    def set_position(self, position: Tuple[int, int]):
        pass

"""Module to define and create Color objects."""

from collections import namedtuple
from dataclasses import dataclass, field
from typing import Any, List

from .utils import (
    convert_hex_to_rgb,
    convert_rgb_to_hex,
    get_contrasting_black_or_white,
    is_hex_code_invalid,
    is_rgb_value_valid,
)


RGB = namedtuple("RGB", ["red", "green", "blue"])


@dataclass(frozen=True)
class Color:
    """Color is a dataclass to represent a color."""

    name: str
    hex_code: str
    rgb_values: RGB
    speakable_hex_code: field(init=False)
    contrasting_tone: field(init=False)  # For text color on GUI

    def __post_init__(self):
        """Populate default properties."""
        self.speakable_hex_code = ". ".join(self.hex_code.lstrip("#").upper())
        self.contrasting_tone = get_contrasting_black_or_white(self.hex_code)


class ColorFactory:
    """Factory to create Colors from different input types.

    Args:
        colors_by_name: Dict of colors using name as key.
        colors_by_hex: Dict of colors using hex as key

    # TODO should we generate colors_by_hex here instead of in Skill class?
    """

    def __init__(self, colors_by_name, colors_by_hex) -> None:
        self.colors_by_name = colors_by_name
        self.colors_by_hex = colors_by_hex

    def create(self, type: str, value: Any[str, List([int])]) -> Color:
        """Create a color from a supported value type.

        Type must be one of ['name', 'hex', 'rgb'].
        RGB value must be a list of 3 integers.
        """
        func = None
        if type == "name":
            func = self.create_color_by_name
        elif type == "hex":
            func = self.create_color_by_hex
        elif type == "rgb":
            func = self.create_color_by_rgb
        if func is None:
            raise TypeError("Invalid type for Color creation.")
        else:
            return func(value)

    def create_color_by_name(self, name: str) -> Color:
        """Create a Color object by CSS3 name."""
        hex_code = self.colors_by_name.get(name)
        if hex_code is None:
            raise ValueError(f"Invalid input for name: {name}")
        rgb_values = convert_hex_to_rgb(hex_code)
        return Color(
            name,
            hex_code,
            rgb_values,
        )

    def create_color_by_hex(self, hex_code: str) -> Color:
        """Create a Color object by hex code."""
        if is_hex_code_invalid(hex_code):
            raise ValueError(f"Invalid input for hex_code: {hex_code}")
        name = self.colors_by_hex[hex_code]
        rgb_values = convert_hex_to_rgb(hex_code)
        return Color(
            name,
            hex_code,
            rgb_values,
        )

    def create_color_by_rgb(self, rgb_values: List[int, int, int]) -> Color:
        """Create a Color object by RGB values."""
        if not is_rgb_value_valid(rgb_values):
            raise ValueError(f"Invalid input for rgb_values: {rgb_values}")
        hex_code = convert_rgb_to_hex(rgb_values)
        name = self.colors_by_hex[hex_code]
        return Color(
            name,
            hex_code,
            rgb_values,
        )

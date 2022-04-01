import unittest

from colors.color import Color, ColorFactory


class TextColorFactory(unittest.TestCase):
    def test_create_color_by_name(self):
        """Create a color by a CSS color name."""
        name = "red"
        name_to_hex_map = {"red": "#ff0000"}
        color_factory = ColorFactory(name_to_hex_map)
        color = color_factory.create("name", name)
        self.assertIsInstance(color, Color)
        self.assertEqual(color.name, name)
        self.assertEqual(color.hex_code, "#ff0000")
        self.assertEqual(color.rgb_values.red, 255)
        self.assertEqual(color.rgb_values.green, 0)
        self.assertEqual(color.rgb_values.blue, 0)

    def test_create_color_by_hex_code(self):
        hex_code = "#BADA55"
        name_to_hex_map = {}
        color_factory = ColorFactory(name_to_hex_map)
        color = color_factory.create("hex", hex_code)
        self.assertIsInstance(color, Color)
        self.assertEqual(color.name, None)
        self.assertEqual(color.hex_code, hex_code)
        self.assertEqual(color.rgb_values.red, 186)
        self.assertEqual(color.rgb_values.green, 218)
        self.assertEqual(color.rgb_values.blue, 85)

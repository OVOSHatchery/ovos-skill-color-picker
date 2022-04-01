import unittest

from colors.utils import convert_hex_to_rgb


class TextColorConversions(unittest.TestCase):
    def test_hex_to_rgb(self):
        self.assertEqual(convert_hex_to_rgb("#000000"), (0, 0, 0))
        self.assertEqual(convert_hex_to_rgb("#dc143c"), (220, 20, 60))
        self.assertEqual(convert_hex_to_rgb("fff5ee"), (255, 245, 238))
        self.assertEqual(convert_hex_to_rgb("#fff"), (255, 255, 255))
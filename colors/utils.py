
def convert_hex_to_rgb(hex: str) -> tuple((int, int, int)):
    """Convert a hex color code to RGB values."""
    hex_cleaned = hex.lstrip('#')
    if len(hex_cleaned) == 3:
        hex_cleaned = "".join([char*2 for char in hex_cleaned])
    rgb_values = tuple(int(hex_cleaned[i:i+2], 16) for i in (0, 2, 4))
    return rgb_values

def convert_input_to_css_name(input: str) -> str:
    """Convert the spoken input of a color name to the CSS official name."""
    return input.lower().replace(' ', '')

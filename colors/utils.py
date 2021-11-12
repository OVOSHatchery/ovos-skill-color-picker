
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


def get_contrasting_black_or_white(hex_code) -> str:
    """Get a contrasting black or white color for text display.

    Args:
        hex_code of base color

    Returns:
        black or white as a hex_code
    """
    rgb_values = convert_hex_to_rgb(hex_code)
    red, green, blue = rgb_values
    yiq = ((red * 299) + (green * 587) + (blue * 114)) / 1000
    return '#000000' if yiq > 125 else '#ffffff'

def convert_rgb_to_hex(rgb: tuple([int,int,int])) -> str:
    """Take an RGB value and convert it to hex code. Return None if the RGB code is invalid"""
    
    #Validate user Input is not negative or greater than 255
    for value in rgb:
        if not 256 > value >= 0:
            # Return nothing if any of the RGB values fail validation
            return None
    return '%02x%02x%02x' % rgb


def is_hex_code_invalid(hex_code: str) -> bool:
    """Validate whether the input string is a valid hex color code."""
    # TODO expand to validate 3 char codes.
    hex_code = hex_code.lstrip('#')
    try:
        assert len(hex_code) == 6
        int(hex_code, 16)
    except (AssertionError, ValueError):
        return True
    else:
        return False

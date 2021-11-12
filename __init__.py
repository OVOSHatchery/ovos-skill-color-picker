from typing import List
from mycroft import MycroftSkill, intent_handler


from .colors.utils import (
    convert_input_to_css_name,
    convert_hex_to_rgb,
    get_contrasting_black_or_white,
    is_hex_code_invalid,
    convert_rgb_to_hex
)

class ColorPicker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.colors_by_name = dict()
        self.colors_by_hex = dict()

    def initialize(self):
        self.colors_by_name = self.translate_namedvalues('color-names')
        # Generate colors_by_hex dict
        for color_name in self.colors_by_name:
            hex_code = self.colors_by_name[color_name]
            self.colors_by_hex[hex_code] = color_name

    @intent_handler('request-color-by-name.intent')
    def handle_request_color_by_name(self, message):
        """Handle named color requests.

        Example: 'Show me the color burly wood'
        """
        requested_color = message.data.get('color')
        self.log.info("Requested color: %s", requested_color)
        if requested_color is None:
            self.speak_dialog('color-not-found')
            return
        hex_code = self.colors_by_name.get(requested_color)
        if hex_code is None:
            self.speak_dialog('color-not-found')
            return

        rgb_values = convert_hex_to_rgb(hex_code)
        self.display_single_color(requested_color, hex_code, rgb_values)

        speakable_hex_code = '. '.join(hex_code.lstrip('#').upper())
        self.speak_dialog('report-color-by-name', data={
            'color_name': requested_color,
            'hex_code': speakable_hex_code,
            'red_value': rgb_values[0],
            'green_value': rgb_values[1],
            'blue_value': rgb_values[2]
        })

    @intent_handler('request-color-by-hex.intent')
    def handle_request_color_by_hex(self, message):
        """Handle named color requests.

        Example: 'what color has a hex code of bada55'
        """
        requested_hex_code = message.data.get('hex_code').replace(' ', '')
        self.log.info("Requested color: %s", requested_hex_code)
        hex_is_invalid = is_hex_code_invalid(requested_hex_code)
        if hex_is_invalid:
            self.speak_dialog('color-not-found')
            return
        self.log.info("Requested color: %s", requested_hex_code)
    
        rgb_values = convert_hex_to_rgb(requested_hex_code)
        if requested_hex_code[0] != '#':
            requested_hex_code = f'#{requested_hex_code}'
        css_color_name = self.colors_by_hex.get(requested_hex_code)
        
        if css_color_name is None:
            self.speak_dialog('report-color-by-hex-name-not-known', data={
                'hex_code': requested_hex_code.lstrip('#'),
                'red_value': rgb_values[0],
                'green_value': rgb_values[1],
                'blue_value': rgb_values[2]
            })
        else:
            self.speak_dialog('report-color-by-hex-name-known', data={
                'color_name': css_color_name,
                'hex_code': requested_hex_code.lstrip('#'),
                'red_value': rgb_values[0],
                'green_value': rgb_values[1],
                'blue_value': rgb_values[2]
            })

    @intent_handler('request-color-by-rgb.intent')
    def handle_request_color_by_rgb(self, message):
        """
        Handle RGB color requests

        Example: what color has the RGB value of 172 172 172
        """
        rgb_string  = message.data.get('rgb').split()

        requested_rgb = (int(rgb_string[0]), int(rgb_string[1]), int(rgb_string[2]))

        hex_code = convert_rgb_to_hex(requested_rgb)
        spoken_hex_code = ". ".join(list(hex_code)).upper()
        # Returns None if a match is not found
        css_color_name = self.colors_by_hex.get(hex_code)

        if css_color_name is None:
            self.speak_dialog('report-color-by-rgb-name-not-known', data={
                'hex_code': spoken_hex_code
            })
        else:
            self.speak_dialog('report-color-by-rgb-name-known', data={
                'color_name': css_color_name,
                'hex_code': spoken_hex_code
            })
    





    def display_single_color(self, name: str, hex_code: str, rgb_values: List[int]):
        """Display details of a single color"""
        text_color = get_contrasting_black_or_white(hex_code)
        self.gui.clear()
        self.gui['colorName'] = name.title()
        self.gui['colorHex'] = hex_code.upper()
        self.gui['colorRGB'] = f'RGB: {str(rgb_values)}'
        self.gui['textColor'] = text_color
        self.gui.show_page('single-color.qml')


def create_skill():
    return ColorPicker()


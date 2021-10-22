from mycroft import MycroftSkill, intent_handler

from .colors.utils import (
    convert_input_to_css_name,
    convert_hex_to_rgb,
    is_hex_code_invalid
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
        self.log.info(requested_color)
        if requested_color is None:
            self.speak_dialog('color-not-found')
            return
        css_color = convert_input_to_css_name(requested_color)
        self.log.info("Requested color: %s", css_color)
        hex_code = self.colors_by_name.get(css_color)
        if hex_code is None:
            self.speak_dialog('color-not-found')
            return
        rgb_values = convert_hex_to_rgb(hex_code)

        self.gui.show_text(requested_color.title())
        self.speak_dialog('report-color-by-name', data={
            'color_name': requested_color,
            'hex_code': hex_code.lstrip('#'),
            'red_value': rgb_values[0],
            'green_value': rgb_values[1],
            'blue_value': rgb_values[2]
        })

    @intent_handler('request-color-by-hex.intent')
    def handle_request_color_by_hex(self, message):
        """Handle named color requests.

        Example: 'what color has a hex code of bada55'
        """
        requested_hex_code = message.data.get('hex_code')
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


def create_skill():
    return ColorPicker()


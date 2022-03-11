from mycroft import MycroftSkill, intent_handler
from mycroft.messagebus.message import Message


from .colors import (
    Color,
    ColorFactory,
    is_hex_code_valid,
    is_rgb_value_valid,
)


class ColorPicker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.color_factory = None
        self.colors_by_name = dict()
        self.colors_by_hex = dict()

    def initialize(self):
        self.colors_by_name = self.translate_namedvalues("color-names")
        self.color_factory = ColorFactory(self.colors_by_name)

    @intent_handler("request-color.intent")
    def handle_request_color(self, message):
        """Handle requests for color where the color format is unknown.

        Example: 'What color is _________'
        """
        requested_color = message.data.get("requested_color")

        is_color_name = self.colors_by_name.get(requested_color) is not None
        if is_color_name:
            mock_message = Message("", {"color": requested_color})
            self.handle_request_color_by_name(mock_message)

        is_hex_code = is_hex_code_valid(requested_color.replace(" ", ""))
        if is_hex_code:
            mock_message = Message("", {"hex_code": requested_color})
            self.handle_request_color_by_hex(mock_message)

        is_rgb_value = is_rgb_value_valid(requested_color)
        if is_rgb_value:
            mock_message = Message("", {"rgb": requested_color})
            self.handle_request_color_by_rgb(mock_message)

    @intent_handler("request-color-by-name.intent")
    def handle_request_color_by_name(self, message):
        """Handle named color requests.

        Example: 'Show me the color burly wood'
        """
        requested_color = message.data.get("color")
        self.log.info("Requested color: %s", requested_color)
        try:
            color = self.color_factory.create("name", requested_color)
        except ValueError:
            self.speak_dialog("color-not-found")
            return

        self.speak_dialog(
            "report-color-by-name",
            data={
                "color_name": color.name,
                "hex_code": color.speakable_hex_code,
                "red_value": color.rgb_values.red,
                "green_value": color.rgb_values.green,
                "blue_value": color.rgb_values.blue,
            },
        )
        self.display_single_color(color)

    @intent_handler("request-color-by-hex.intent")
    def handle_request_color_by_hex(self, message):
        """Handle named color requests.

        Example: 'what color has a hex code of bada55'
        """
        requested_hex_code = message.data.get("hex_code").replace(" ", "")
        self.log.info("Requested color: %s", requested_hex_code)
        try:
            color = self.color_factory.create("hex", requested_hex_code)
        except ValueError:
            self.speak_dialog("color-not-found")
            return

        color_dialog_data = {
            "color_name": color.name,
            "hex_code": color.speakable_hex_code,
            "red_value": color.rgb_values.red,
            "green_value": color.rgb_values.green,
            "blue_value": color.rgb_values.blue,
        }
        if color.name:
            self.speak_dialog(
                "report-color-by-hex-name-known",
                data=color_dialog_data,
            )
        else:
            self.speak_dialog(
                "report-color-by-hex-name-not-known",
                data=color_dialog_data,
            )

    @intent_handler("request-color-by-rgb.intent")
    def handle_request_color_by_rgb(self, message):
        """
        Handle RGB color requests

        Example: what color has the RGB value of 172 172 172
        """
        rgb_string = message.data.get("rgb").split()

        # TODO this should be handled in the ColorFactory
        # TODO need to decide on a single RGB data type and use it consistently.
        if is_rgb_value_valid(rgb_string):
            requested_rgb = tuple([int(value) for value in rgb_string])
        try:
            color = self.color_factory.create("rgb", requested_rgb)
        except ValueError:
            self.speak_dialog("color-not-found")
            return

        color_dialog_data = {
            "color_name": color.name,
            "hex_code": color.speakable_hex_code,
        }

        if color.name is None:
            self.speak_dialog(
                "report-color-by-rgb-name-known",
                data=color_dialog_data,
            )
        else:
            self.speak_dialog(
                "report-color-by-rgb-name-not-known",
                data=color_dialog_data,
            )

    def display_single_color(self, color: Color):
        """Display details of a single color"""
        self.gui["colorName"] = color.name.title()
        self.gui["colorHex"] = color.hex_code.upper()
        self.gui["colorRGB"] = f"RGB: {str(color.rgb_values)}"
        self.gui["textColor"] = color.contrasting_tone
        self.gui.show_page("single-color.qml")


def create_skill():
    return ColorPicker()

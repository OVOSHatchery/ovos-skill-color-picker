from mycroft import MycroftSkill, intent_handler

from .colors.utils import convert_input_to_css_name

class ColorPicker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.colors = dict()

    def initialize(self):
        self.colors = self.translate_namedvalues('color-names')

    @intent_handler('request-color.intent')
    def handle_request_color(self, message):
        requested_color = message.data.get('color')
        css_color = convert_input_to_css_name(requested_color)
        self.log.info("Requested color: %s", css_color)
        hex_code = self.colors.get(css_color)
        if hex_code is None:
            self.speak_dialog('color-not-found')
            return

        self.gui.show_text(requested_color.title())
        self.speak_dialog('report-color', data={
            'color': requested_color
        })


def create_skill():
    return ColorPicker()


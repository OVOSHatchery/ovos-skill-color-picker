from mycroft import MycroftSkill, intent_file_handler


class ColorPicker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('picker.color.intent')
    def handle_picker_color(self, message):
        color = message.data.get('color')

        self.speak_dialog('picker.color', data={
            'color': color
        })


def create_skill():
    return ColorPicker()


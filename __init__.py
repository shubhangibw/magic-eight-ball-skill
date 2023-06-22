from mycroft import MycroftSkill, intent_file_handler


class MagicEightBall(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ball.eight.magic.intent')
    def handle_ball_eight_magic(self, message):
        self.speak_dialog('ball.eight.magic')


def create_skill():
    return MagicEightBall()


from Horses.Horse import Horse

class Unicorn (Horse):
    cornColor = ""

    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        message = super().__str__()
        message += " I'm also a unicorn!"
        #message += ...
        #message = message + ...
        return message

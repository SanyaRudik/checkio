VOWELS = "aeiouAEIOU"


class Chat:

    def __init__(self):
        self.human_dialogue = []
        self.robot_dialogue = []

    def connect_human(self, human):
        human.chat = self

    def connect_robot(self, robot):
        robot.chat = self

    def show_human_dialogue(self):
        print("\n".join(self.human_dialogue))
        return "\n".join(self.human_dialogue)

    def show_robot_dialogue(self):
        print("\n".join(self.robot_dialogue))
        return "\n".join(self.robot_dialogue)


class Human:

    def __init__(self, name):
        self.name = name

    def send(self, message):
        robot_message = "".join(["0" if char in VOWELS else "1" for char in message])
        self.chat.robot_dialogue.append(self.name + " said: " + robot_message)
        self.chat.human_dialogue.append(self.name + " said: " + message)


class Robot:

    def __init__(self, serial_number):
        self.serial_number = serial_number

    def send(self, message):
        self.chat.human_dialogue.append(self.serial_number + " said: " + message)
        robot_message = "".join(["0" if char in VOWELS else "1" for char in message])
        self.chat.robot_dialogue.append(self.serial_number + " said: " + robot_message)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chat1 = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat1.connect_human(karl)
    chat1.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    chat1.show_robot_dialogue()
    chat1.show_human_dialogue()
    # assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
# R2D2 said: Hello, human. Could we speak later about it?"""
#     assert chat.show_robot_dialogue() == """Karl said: 101111011111011
# R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")
class VoiceCommand:
    def __init__(self, chanel):
        self.chanel = chanel
        self.number_chanel = 0

    def first_channel(self):
        self.number_chanel = 0
        return self.current_channel()

    def last_channel(self):
        self.number_chanel = len(self.chanel)-1
        return self.current_channel()

    def turn_channel(self, number):
        self.number_chanel = number - 1
        return self.current_channel()

    def next_channel(self):
        if self.number_chanel == len(self.chanel)-1:
            self.number_chanel = 0
        else:
            self.number_chanel += 1
        return self.current_channel()

    def previous_channel(self):
        if self.number_chanel == 0:
            self.number_chanel = len(self.chanel)-1
        else:
            self.number_chanel -= 1
        return self.current_channel()

    def current_channel(self):
        return str(self.chanel[self.number_chanel])

    def is_exist(self,n):
        try:
            if n-1 < len(self.chanel) and n-1 >= 0:
                return 'Yes'
        except:
            if n in self.chanel:
                return 'Yes'
        return 'No'






if __name__ == '__main__':
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    print(controller.first_channel())
    print(controller.last_channel())
    print(controller.turn_channel(3))
    print(controller.next_channel())
    print(controller.previous_channel())
    print(controller.current_channel())
    print(controller.is_exist(4))
    print(controller.is_exist("TV1000"))
    print("Coding complete? Let's try tests!")

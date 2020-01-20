class MicrowaveBase:
    def __init__(self):
        self.time = '00:00'

    def show_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time


class Microwave1(MicrowaveBase):

    def show_time(self):
        return '_' + self.time[1:]


class Microwave2(MicrowaveBase):

    def show_time(self):
        return self.time[:-1] + '_'


class Microwave3(MicrowaveBase):
    pass


class RemoteControl:
    def __init__(self, mikrowave):
        self.microwave = mikrowave

    def convert_didg(self, s):
        if s.find(':') > -1:
            return (int(s[:2]) * 60) + int(s[3:])
        elif s.find('s') > -1:
            return int(s[:-1])
        elif s.find('m') > -1:
            return int(s[:-1]) * 60

    def convert_str(self, i):
        s_m = str(i // 60)
        if len(s_m) == 1:
            s_m = '0' + s_m
        s_s = str(i % 60)
        if len(s_s) == 1:
            s_s = '0' + s_s
        return f'{s_m}:{s_s}'

    def set_time(self, time):
        self.microwave.set_time(time)

    def add_time(self, time_a):
        if self.convert_didg(self.microwave.get_time()) + self.convert_didg(time_a) > 5400:
            self.microwave.set_time('90:00')
        else:
            self.microwave.set_time(
                self.convert_str(self.convert_didg(self.microwave.get_time()) + self.convert_didg(time_a)))

    def del_time(self, time_d):
        if self.convert_didg(self.microwave.get_time()) - self.convert_didg(time_d) < 0:
            self.microwave.set_time('00:00')
        else:
            self.microwave.set_time(
                self.convert_str(self.convert_didg(self.microwave.get_time()) - self.convert_didg(time_d)))

    def show_time(self):
        return self.microwave.show_time()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    print(remote_control_1.show_time())  # == "_1:00"
    print(remote_control_2.show_time())  # == "01:3_"
    print(remote_control_3.show_time())  # == "01:40"
    # print("Coding complete? Let's try tests!")

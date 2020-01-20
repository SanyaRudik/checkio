class HackerLanguage:
    def __init__(self):
        self.text = ''
        self.d = {str(bin(i))[2:]: chr(i) for i in range(ord('a'), ord('z'))}  # створює словник від "а" до "Z"
        self.d.update({str(bin(i))[2:]: chr(i) for i in range(ord('A'), ord('Z'))})
        self.d_val = dict(zip(self.d.values(), self.d.keys()))  # міняє місцями значення й ключ словника

    def write(self, text):
        self.text += text

    def delete(self, numb):
        self.text = self.text[:-numb]

    def send(self):
        n = ''
        for i in self.text:
            if self.d_val.get(i):
                n += self.d_val[i]
            elif i == ' ':
                n += '1000000'
            else:
                n += i
        return n

    def read(self, text):
        n = text.replace('1000000', ' ')
        s = ''
        while len(n):
            if len(n) >= 7:
                if self.d.get(n[-7:]):
                    s += self.d.get(n[-7:])
                    n = n[:-7]
                else:
                    s += n[-1]
                    n = n[:-1]
                    continue
            else:
                s += n[-1]
                n = n[:-1]
        return s[::-1]


if __name__ == '__main__':
    message_1 = HackerLanguage()
    message_1.write('Remember: 21.07.2018 at 11:11AM')
    message_1.delete(2)
    message_1.write('PM')
    message_2 = HackerLanguage()
    print(message_1.send())
    print(message_1.read(message_1.send()))

    # assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")

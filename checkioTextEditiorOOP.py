"""
write(text) - добавляет указанный текст к текущему.
set_font(font name) - устанавливает шрифт текста. Шрифт распространяется на весь текст, даже добавленный после установки
шрифта и отображается в квадратных скобках перед началом текста и после конца: "[Arial]...example...[Arial]".
 Шрифт может быть задан сколько угодно раз, но отображается только последний из них.
show() - отображает текущий текст и шрифт (если задан).
restore(SavedText.get_version(number)) - возвращает текст к указанной версии.


save_text(Text) - сохраняет текущее состояние текста и текущий шрифт. Первая сохраненная версия имеет номер 0,
 вторая - 1 и так далее.
get_version(number) - метод используется вместе с методом restore класса Text и служит для выбора нужной версии текста.
"""


class Text:
    text_edit = ''
    font_name = ''

    def write(self, text):
        self.text_edit += text

    def set_font(self, font_name):
        self.font_name = f'[{font_name}]'

    def show(self):
        return f'{self.font_name}{self.text_edit}{self.font_name}'

    def restore(self, old):
        self.text_edit = old[0]
        self.font_name = old[1]


class SavedText:

    def __init__(self):
        self.save_text_edit = []

    def save_text(self, text):
        self.save_text_edit.append([text.text_edit, text.font_name])

    def get_version(self, number):
        return [self.save_text_edit[number][0], self.save_text_edit[number][1]]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")

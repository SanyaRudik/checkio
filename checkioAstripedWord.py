VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
SEPAR = "?!,.-"


def striped(text):
    if len(text) <= 1 or not text.isalpha():
        return False
    s = ' '
    for i in text.upper():
        if (i in VOWELS) and (s in VOWELS):
            return False
        if (i in CONSONANTS) and (s in CONSONANTS):
            return False
        s = i
    return True
def replacement(text):
    if text in SEPAR:
        return ' '
    return text

def checkio(text):
    """

    :param text:
    :return:  replacement - Сравнивает Знаки препинания и заменяем их на  пробел  - map(replacement, text)
                и разбиваем по словах
                striped - выбераее которые чередуются
                подщитываем количество слов которые получились

    """
    number_of_striped = len(list(filter(striped, ''.join(map(replacement, text)).split(' '))))
    return number_of_striped


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("My name is ..."))  # == 3, "All words are striped"
    print(checkio("Hello world"))  # == 0, "No one"
    print(checkio("A quantity of striped words."))  # == 1, "Only of"
    print(checkio("Dog,cat,mouse,bird.Human."))  # == 3, "Dog, cat and human"
    print(checkio("1 2 34 43 43 54546 6  65 6 7 7667 6 7 67 6 8 78 78"))
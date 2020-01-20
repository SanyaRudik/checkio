
def checkio(text: str) -> str:
    '''
    Дві строчки
    В першій:
    Прибираємо всі символи крім букв
    Приводимо до нижнього регістру
    Сортуємо по мірі зростання і це все скріплюємо
    В Другій
    Ссртуємо по частоті букв
    '''
    s_sorted = sorted(''.join(list(filter(lambda s: s.isalpha(), text.lower()))))
    s_sorted = sorted(s_sorted, key=lambda c: s_sorted.count(c), reverse=True)

    return s_sorted[0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))
    print(checkio("How do you do?"))
    print(checkio("One"))
    print(checkio("Oops!"))
    print(checkio("AAaooo!!!!"))
    print(checkio("abe"))
    print(checkio("a" * 9000 + "b" * 1000))
    # assert checkio("Hello World!") == "l", "Hello test"
    # assert checkio("How do you do?") == "o", "O is most wanted"
    # assert checkio("One") == "e", "All letter only once."
    # assert checkio("Oops!") == "o", "Don't forget about lower case."
    # assert checkio("AAaooo!!!!") == "a", "Only letters."
    # assert checkio("abe") == "a", "The First."
    # print("Start the long test")
    # assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    # print("The local tests are done.")

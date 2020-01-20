'''
Продолжим изучение слов. Даны две строки со словами, разделенными запятыми. Попробуйте найти
что общего между этими строками. Слова внутри каждой строки не повторяются.
Ваша функция должна находить все слова, которые появляются в обеих строках. Результат должен быть представлен,
как строка со словами разделенными запятыми и отсортированными в алфавитном порядке.

Вх. данные: Два аргумента как строки (str).

Вых. данные: Общие слова как строка (str).
'''
def checkio(first, second):
    return ','.join(list(filter(lambda x: [i for i in second.split(',') if i == x], sorted(first.split(',')))))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("hello,world", "hello,earth"))  # == "hello", "Hello"
    print(checkio("one,two,three", "four,five,six"))  # == "", "Too different"
    print(checkio("one,two,three", "four,five,one,two,six,three"))  # == "one,three,two", "1 2 3"
    print(checkio("mega,cloud,two,website,final", "window,penguin,literature,network,fun,cloud,final,sausage"))

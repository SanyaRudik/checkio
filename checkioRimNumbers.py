def checkio(data):
    if data - 1000 >= 0:
        return "M" + checkio(data - 1000)
    elif data - 900 >= 0:
        return "CM" + checkio(data - 900)
    elif data - 500 >= 0:
        return "D" + checkio(data - 500)
    elif data - 400 >= 0:
        return "CD" + checkio(data - 400)
    elif data - 100 >= 0:
        return "C" + checkio(data - 100)
    elif data - 90 >= 0:
        return "XC" + checkio(data - 90)
    elif data - 50 >= 0:
        return "L" + checkio(data - 50)
    elif data - 40 >= 0:
        return "XL" + checkio(data - 40)
    elif data - 10 >= 0:
        return "X" + checkio(data - 10)
    elif data - 9 >= 0:
        return "IX" + checkio(data - 9)
    elif data - 5 >= 0:
        return "V" + checkio(data - 5)
    elif data - 4 >= 0:
        return "IV" + checkio(data - 4)
    elif data - 1 >= 0:
        return "I" + checkio(data - 1)
    return ''


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    s = int(input())
    print(checkio(s))  # == 'VI', '6'
    # print(checkio(76))  # == 'LXXVI', '76'
    # print(checkio(499))  # == 'CDXCIX', '499'
    # print(checkio(3888))  # == 'MMMDCCCLXXXVIII', '3888'

RimNum = [['M', 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50],
          ["XL", 40],["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]


def checkio(data):
    d = []
    dd = 0
    i = 0
    data += '  '
    while i <= len(data)-2:
        for c in RimNum:
            if (data[i] == c[0]) or (data[i:i+2] == c[0]):
                d.append(c[0])
                dd += c[1]
                if len(c[0]) == 2:
                    i += 1
                break
        i += 1

    return dd


if __name__ == '__main__':
    print(checkio('IIIIIXXXIII'))
    print(checkio('CDXCIX'))
    print(checkio('MMMDCCCLXXXVIII'))

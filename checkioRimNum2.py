RimNum = [['M', 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90],
          ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]


def checkio(data):
    for i in RimNum:
        if data - i[1] >= 0:
            return i[0] + checkio(data - i[1])
    return ''


if __name__ == '__main__':
    for i in range(3000):
        print(i, '-', checkio(i))

def check_doubl(first, second):
    n = 0
    for c, i in enumerate(str(first)):
        if i == str(second)[c]:
            n += 1
    if n == 2:
        return True
    return False


def checkio(numbers):
    f = [[numbers.pop(0)]]
    while f:
        c = f.pop(0)
        for i in range(len(numbers) - 1, -1, -1):
            if not check_doubl(numbers[i], c[-1]):
                continue
            if numbers[-1] == numbers[i]:
                return c + [numbers[-1]]
            f.append(c + [numbers.pop(i)])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]))  # == [123, 121, 921, 991, 999], "First"
    print(checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]))  # == [111, 121, 127, 727, 777], "Second"
    print(checkio([456, 455, 454, 356, 656, 654]))  # == [456, 454, 654], "Third, [456, 656, 654] is correct too"

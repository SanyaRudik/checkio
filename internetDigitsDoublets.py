distance = lambda a, b: sum([a[i] != b[i] for i in range(len(a))])


def checkio(numbers):
    # Start with the first number.
    paths = [[numbers.pop(0)]]
    # print(paths)
    # BFS algorithm.
    while True:
        current = paths.pop(0)
        for i in range(len(numbers) - 1, -1, -1):
            if distance(str(numbers[i]), str(current[-1])) != 1:
                continue
            if numbers[i] == numbers[-1]:
                return current + [numbers[-1]]
            paths.append(current + [numbers.pop(i)])
            print(paths)


print(checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]))  # == [123, 121, 921, 991, 999], "First"
print(checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]))  # == [111, 121, 127, 727, 777], "Second"
print(checkio([456, 455, 454, 356, 656, 654]))  # == [456,454, 654], "Third, [456, 656, 654] is correct too"

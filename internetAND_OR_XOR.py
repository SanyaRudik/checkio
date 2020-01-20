AND = lambda x, y: int(x) and int(y)
OR = lambda x, y: int(x) or int(y)
XOR = lambda x, y: int(x) ^ int(y)


def sum_table(first, second, func):
    return sum(int("".join(str(func(f, s)) for s in second), 2) for f in first)


def checkio(first, second):
    f, s = bin(first)[2:], bin(second)[2:]
    return sum_table(f, s, AND) + sum_table(f, s, OR) + sum_table(f, s, XOR)


print(checkio(4, 6))
print(checkio(2, 7))
print(checkio(7, 2))

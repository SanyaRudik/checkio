def sum_AOX(by):
    return sum(map(lambda i: int(i, 2), by))


def checkio(first, second):
    f, s = bin(first)[2:], bin(second)[2:]
    AND, OR, XOR = [], [], []
    for i, x in enumerate(f):
        AND.append('')
        OR.append('')
        XOR.append('')
        for y in s:
            AND[i] += str(int(x) and int(y))
            OR[i] += str(int(x) or int(y))
            XOR[i] += str(int(x) ^ int(y))
    return sum([sum_AOX(AND), sum_AOX(OR), sum_AOX(XOR)])


print(checkio(4, 6))
print(checkio(2, 7))
print(checkio(7, 2))

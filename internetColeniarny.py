from itertools import combinations


def L(x, y, z):
    # print(x, y, z, (y[0] - x[0]) * (z[1] - x[1]) == (y[1] - x[1]) * (z[0] - x[0]))

    return (y[0] - x[0]) * (z[1] - x[1]) == (y[1] - x[1]) * (z[0] - x[0])


def checkio(cakes):
    rows = set()
    # for i in combinations(cakes, 2):
        # print(i)
    for p, q in combinations(cakes, 2):
        colinear = frozenset(tuple(r) for r in cakes if L(p, q, r))
        print(colinear)
        if len(colinear) > 2:
            rows.add(colinear)
    return len(rows)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]])  # == 2
    # assert checkio(
    #     [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
    #      [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6

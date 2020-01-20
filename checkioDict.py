def best_stock(a):
    b = 0
    b1 = {}
    for i in a:
        if a.get(i) > b:
            b = a.get(i)
            b1 = i
    return b1


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))
    print(best_stock({"CAC": 16.0, "ATX": 39.2, "WIG": 51.2}))
    print(best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    # assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    # print("Coding complete? Click 'Check' to earn cool rewards!")

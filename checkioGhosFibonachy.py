def checkio(opacity):
    fibo = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
    proz = 10000
    for i in range(5001):
        if i in fibo:
            proz -= i
        else:
            proz += 1
        if proz == opacity:
            return i


if __name__ == '__main__':
    print(checkio(10000))  # == 0, "Newborn"
    print(checkio(9999))  # == 1, "1 year"
    print(checkio(9997))  # == 2, "2 years"
    print(checkio(9994))  # == 3, "3 years"
    print(checkio(9995))  # == 4, "4 years"
    print(checkio(9990))  # == 5, "5 years"

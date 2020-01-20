def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """
    a = []
    for ii in args:
        i = 1
        n1 = 0
        while i ** 2 <= ii:
            if ii % i == 0:
                a.append(str(i))
                n1 += 1
                if i != ii // i:
                    a.append(str(ii // i))
                    n1 += 1
            i += 1
    a = sorted(a, key=lambda cv: (a.count(cv), int(cv)), reverse=True)
    return int(a[0])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(greatest_common_divisor(3, 9, 3, 9))  # == 2, "Simple"
    print(greatest_common_divisor(2, 4, 8))  # == 2, "Three arguments"
    print(greatest_common_divisor(2, 3, 5, 7, 11))  # == 1, "Prime numbers"
    print(greatest_common_divisor(4294967296, 2))  # == 3, "Repeating arguments"

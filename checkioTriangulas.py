def checkio(number):
    a = []
    s = 0
    for i in range(1, number):
        if s + i > number:
            break
        s += i
        a.append(s)
        # print(s)
    a_top = []
    for i in range(len(a)):
        for c in range(len(a)):
            if c+i > len(a):
                break
            if sum(a[c:c+i]) == number:
                if len(a_top) < len(a[c:c+i]):
                    a_top = a[c:c+i].copy()


                # print(sum(a[c:c+i]), a[c:c+i])

    # print(a)
    print(a_top)
    return a_top


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio(64)  # == [15, 21, 28], "1st example"
    checkio(371)  # == [36, 45, 55, 66, 78, 91], "1st example"
    checkio(225)  # == [105, 120], "1st example"
    checkio(882)  # == [], "1st example"

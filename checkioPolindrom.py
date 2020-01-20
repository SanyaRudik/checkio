def longest_palindromic(a):
    d = []
    for i, c in enumerate(a):

        for ii in range(i, len(a) + 1):
            b = a[i:ii]
            if a[i:ii] == b[::-1]:
                d.append(a[i:ii])

    d = sorted(d, key=lambda c: len(c), reverse=True)
    return d[0]


if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abc'))
    print(longest_palindromic('abacada'))
    print(longest_palindromic('artrartrt'))
    print(longest_palindromic('aaaaa'))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert longest_palindromic('abc') == 'a'
    # assert longest_palindromic('abacada') == 'aba'
    # assert longest_palindromic('artrartrt') == 'rtrartr'
    # assert longest_palindromic('aaaaa') == 'aaaaa'
    # print("Coding complete? Click 'Check' to earn cool rewards!")

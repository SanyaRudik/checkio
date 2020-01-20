def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    s = []
    n = 0
    x = ''
    len_sub = 0
    try:
        x = line[0]
    except:
        pass
    for i, c in enumerate(line+' '):
        if x != c:
            if i - n > len_sub:
                len_sub = i - n
            s.append(line[n:i])
            n = i
            x = c

    return len_sub


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(long_repeat('sdsffffse'))  # == 4, "First"
    print(long_repeat('ddvvrwwwrggg'))  # == 3, "Second"
    print(long_repeat('abababaab'))  # == 2, "Third"
    print(long_repeat(''))  # == 0, "Empty"
    print('"Run" is good. How is "Check"?')

def follow(instructions):
    d = {'f': [0, 1], 'b': [0, -1], 'l': [-1, 0], 'r': [1, 0]}
    c = [0, 0]
    for i in instructions:
        c[0] += d[i][0]
        c[1] += d[i][1]
    return tuple(c)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")

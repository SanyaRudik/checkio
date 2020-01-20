def group_equal(els_1):
    kv = []
    ii = 0
    els = els_1
    els.append('#')
    for c in range(len(els)):
        if c == ii:
            for ii in range(c, len(els)):
                if els[c] != els[ii]:
                    kv.append(els[c:ii])
                    break
    return kv


if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))
    print(group_equal([1, 2, 3, 4]))
    print(group_equal([1]))
    print(group_equal([]))

    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]]
    # assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    # assert group_equal([1]) == [[1]]
    # assert group_equal([]) == []

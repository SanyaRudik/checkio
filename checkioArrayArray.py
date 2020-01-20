'''
Перетворення з впакованих масивів в одни лінійний

'''


def fl(l, a):
    for i in l:
        if isinstance(i, list):
            fl(i, a)
        else:
            a.append(i)
    return a


def flat_list(l):
    return fl(l, [])


# print(flat_list([[[1, [1, 1, [3, [4, 5, ]]]], 2, 3], [4, 5], 6], []))

if __name__ == '__main__':
    print(flat_list([1, 2, 3]))  # == [1, 2, 3], "First"
    print(flat_list([1, [2, 2, 2], 4]))  # == [1, 2, 2, 2, 4], "Second"
    print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))  # == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    print(flat_list([-1, [1, [-2], 1], -1]))  # == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')

from typing import List

'''
 _________________________________________________________________________
|   Програма для пошука  в масиві кількості одиничок які не пририваються  |
|          Схоже на кількість кораблів в грі "Морский бій"                |
|_________________________________________________________________________|

'''


def search(land_map, x, y, c, xx):
    land_map[x][y] = xx
    if land_map[x - 1][y - 1] == c:
        search(land_map, x - 1, y - 1, c, xx)
    if land_map[x - 1][y] == c:
        search(land_map, x - 1, y, c, xx)
    if land_map[x - 1][y + 1] == c:
        search(land_map, x - 1, y + 1, c, xx)
    if land_map[x][y - 1] == c:
        search(land_map, x, y - 1, c, xx)
    if land_map[x][y + 1] == c:
        search(land_map, x, y + 1, c, xx)
    if land_map[x + 1][y - 1] == c:
        search(land_map, x + 1, y - 1, c, xx)
    if land_map[x + 1][y] == c:
        search(land_map, x + 1, y, c, xx)
    if land_map[x + 1][y + 1] == c:
        search(land_map, x + 1, y + 1, c, xx)
    return land_map


def check_io(land_map1: List[List[int]]) -> List[int]:
    x = 1
    d = []
    land_map = [[0 for i in range(len(land_map1[0]) + 2)] for c in range(len(land_map1) + 2)]
    for i in range(len(land_map1)):
        for c in range(len(land_map1[0])):
            land_map[i + 1][c + 1] = land_map1[i][c]
    for c in range(1, len(land_map) - 1):
        for ii in range(1, len(land_map[0]) - 1):
            if land_map[c][ii] == 1:
                x += 1
                land_map = search(land_map, c, ii, 1, x)
    print()
    for i in land_map:
        print(i)

    land_map = [str(y) for x in land_map for y in x if y != 0]
    for i in range(2, 30):
        if ' '.join(land_map).count(str(i)):
            d.append(' '.join(land_map).count(str(i)))

    print(sorted(d))
    return sorted(d)


if __name__ == '__main__':
    print("Example:")
    check_io([[1, 0, 0, 0, 0],
              [0, 0, 1, 1, 0],
              [0, 0, 0, 1, 0],
              [0, 1, 1, 0, 0]])

    check_io([[0, 0, 0, 1, 0, 0],
             [1, 0, 0, 1, 1, 1],
             [1, 0, 0, 1, 1, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 1, 1]])

    check_io([[0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0, 0],
              [0, 1, 0, 1, 0, 0],
              [0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 0],
              [0, 1, 0, 1, 1, 1],
              [0, 0, 0, 0, 1, 0]])
    check_io([[1],
             [1],
             [1],
             [1],
             [1],
             [1],
             [1],
             [1],
             [1]])
    check_io([[1, 0, 1, 0, 0, 1],
             [0, 0, 0, 0, 1, 0],
             [1, 0, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 1],
             [0, 0, 1, 0, 0, 1],
             [1, 0, 1, 0, 1, 1]])
    #
    # assert checkio([[0, 0, 0, 0, 0],
    #                 [0, 0, 1, 1, 0],
    #                 [0, 0, 0, 1, 0],
    #                 [0, 1, 0, 0, 0],
    #                 [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    # assert checkio([,[0 0, 0, 0, 0],
    #                 [0, 0, 1, 1, 0],
    #                 [0, 0, 0, 1, 0],
    #                 [0, 1, 1, 0, 0]]) == [5], "2nd example"
    # assert checkio([[0, 0, 0, 0, 0, 0],
    #                 [1, 0, 0, 1, 1, 1],
    #                 [1, 0, 0, 0, 0, 0],
    #                 [0, 0, 1, 1, 1, 0],
    #                 [0, 0, 0, 0, 0, 0],
    #                 [0, 1, 1, 1, 1, 0],
    #                 [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    # print("Coding complete? Click 'Check' to earn cool rewards!")

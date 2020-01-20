def search(land_map, x, y, c, xx):
    land_map[x][y] = xx
    # if land_map[x - 1][y - 1] == c:
    #     search(land_map, x - 1, y - 1, c, xx)
    if land_map[x - 1][y] == c:
        search(land_map, x - 1, y, c, xx)
    # if land_map[x - 1][y + 1] == c:
    #     search(land_map, x - 1, y + 1, c, xx)
    if land_map[x][y - 1] == c:
        search(land_map, x, y - 1, c, xx)
    if land_map[x][y + 1] == c:
        search(land_map, x, y + 1, c, xx)
    # if land_map[x + 1][y - 1] == c:
    #     search(land_map, x + 1, y - 1, c, xx)
    if land_map[x + 1][y] == c:
        search(land_map, x + 1, y, c, xx)
    # if land_map[x + 1][y + 1] == c:
    #     search(land_map, x + 1, y + 1, c, xx)
    return land_map


def generator(matrix):
    for i in matrix:
        for c in i:
            yield c
    return


def can_pass(matrix, first, second):
    '''
    Пример как забить матрицу
    сразу когда ее создаешь
 ______________________________________________________________________________________________________________________
    land_map = [[border if (i == 0 or c == 0 or c == mat_x - 1 or i == mat_y - 1) else next(n) for i in range(mat_y)]
                for c in range(mat_x)]
 ______________________________________________________________________________________________________________________
    Делает границу в матрице  принимая данные с функции Генератора
    '''
    border = 88
    marker = 99
    mat_y = len(matrix[0]) + 2
    mat_x = len(matrix) + 2
    n = generator(matrix)
    land_map = [[border if (i == 0 or c == 0 or c == mat_x - 1 or i == mat_y - 1) else next(n) for i in range(mat_y)]
                for c in range(mat_x)]
    land_map = search(land_map, first[0] + 1, first[1] + 1, matrix[first[0]][first[1]], marker)

    for c, i in enumerate(land_map):  # ---------------------Print----------------------------------------------
        if 0 < c < len(land_map)-1:
            print(i[1:len(i)-1])

    if land_map[second[0] + 1][second[1] + 1] == marker:
        return True
    return False


if __name__ == '__main__':
    print(can_pass(((0, 0, 0, 0, 0, 0),
                    (0, 2, 2, 2, 3, 2),
                    (0, 2, 0, 0, 0, 2),
                    (0, 2, 0, 2, 0, 2),
                    (0, 2, 2, 2, 0, 2),
                    (0, 0, 0, 0, 0, 2),
                    (2, 2, 2, 2, 2, 2),),
                   (3, 2), (0, 5)))  # == True, 'First example'

    print(can_pass(((0, 0, 0, 0, 0, 0),
                    (0, 2, 2, 2, 3, 2),
                    (0, 2, 0, 0, 0, 2),
                    (0, 2, 0, 2, 0, 2),
                    (0, 2, 2, 2, 0, 2),
                    (0, 0, 0, 0, 0, 2),
                    (2, 2, 2, 2, 2, 2),),
                   (3, 3), (6, 0)))  # == False, 'First example'
    print(can_pass(((1, 9), (9, 1)), (0, 1), (1, 0)))
    print(can_pass(((0, 0), (0, 0)), (0, 0), (1, 1)))

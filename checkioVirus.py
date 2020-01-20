virus = []


def infected(x, y, matrix):
    global virus
    if (matrix[x][y] == 0) and ([x, y] not in virus):
        virus.append([x, y])


def capture(matrix):
    virus.clear()
    loop = 0
    a = []
    infected(0, 0, matrix)
    while len(virus) < (len(matrix) * len(matrix[0])):
        loop += 1
    # v = virus.copy()
        a.clear()
        for x, y in virus:
            if (x + 1 < len(matrix)) and [x+1, y] not in a:
                a.append([x+1, y])
                if matrix[x+1][y] == 0:
                    infected(x+1, y, matrix)
                else:
                    matrix[x+1][y] -= 1


            if (y + 1 < len(matrix[0])) and [x, y+1] not in a:
                a.append([x, y+1])
                if matrix[x][y+1] == 0:
                    infected(x, y + 1, matrix)
                else:
                    matrix[x][y+1] -= 1

            if ((x + 1 < len(matrix)) and y + 1 < len(matrix[0])) and ([x+1, y+1] not in a):
                a.append([x+1, y + 1])
                if matrix[x+1][y+1] == 0:
                    infected(x + 1, y + 1, matrix)
                else:
                    matrix[x+1][y+1] -= 1
        print()
        for i in matrix:
            print(i)
    print(loop)




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(capture([[0, 1, 0, 1, 0, 1],
                   [1, 8, 1, 0, 0, 0],
                   [0, 1, 2, 0, 0, 1],
                   [1, 0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 3, 1],
                   [1, 0, 1, 0, 1, 2]]))  # == 8, "Base example"
    capture([[0, 1, 0, 1, 0, 1],
             [1, 1, 1, 0, 0, 0],
             [0, 1, 2, 0, 0, 1],
             [1, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 3, 1],
             [1, 0, 1, 0, 1, 2]])  # == 4, "Low security"
    capture([[0, 1, 1],
             [1, 9, 1],
             [1, 1, 9]])  # == 9, "Small"




    # loop = 0
    # virus = []
    # v = []
    # matrix = matrix.copy()
    # zaraza = [[1 for y in matrix[0]] for x in matrix]
    # virus.append([0, 0])
    # while len(virus) < (len(matrix) * len(matrix[0])):
    #     loop += 1
    #     v = virus.copy()
    #     zaraza = [[1 for y in matrix[0]] for x in matrix]
    #     for x, y in v:
    #         if x + 1 < len(matrix):
    #             if matrix[x + 1][y] and zaraza[x + 1][y]:
    #                 matrix[x + 1][y] -= 1
    #                 zaraza[x + 1][y] = 0
    #             else:
    #                 if ([x + 1, y] not in virus) and not [x + 1, y]:
    #                     virus.append([x + 1, y])
    #
    #         if y + 1 < len(matrix[0]):
    #             if matrix[x][y + 1] and zaraza[x][y + 1]:
    #                 matrix[x][y + 1] -= 1
    #                 zaraza[x][y + 1] = 0
    #             else:
    #                 if ([x, y + 1] not in virus) and not [x, y + 1]:
    #                     virus.append([x, y + 1])
    #         if y + 1 < len(matrix[0]) and x + 1 < len(matrix):
    #             if matrix[x + 1][y + 1] and zaraza[x + 1][y + 1]:
    #                 matrix[x + 1][y + 1] -= 1
    #                 zaraza[x + 1][y + 1] = 0
    #             else:
    #                 if ([x + 1, y + 1] not in virus) and not [x + 1, y + 1]:
    #                     virus.append([x + 1, y + 1])
    #                     zaraza[x + 1][y + 1] = 0
    #
    #     print(virus)
    #     for i in matrix:
    #         print(i)
    #
    # print(loop)

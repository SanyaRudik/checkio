def checkio(matrix):
    for x, i in enumerate(matrix):
        for y, ii in enumerate(i):
            if matrix[x][y] + matrix[y][x]:
                return False
    return True


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([[0, 1, 2, 3, 4],
                   [-1, 0, 5, 6, 7],
                   [-2, -5, 0, 8, 9],
                   [-3, -6, -8, 0, 0],
                   [-4, -7, -9, 0, 0]]))

    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!");

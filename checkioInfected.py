def capture(matrix):
    free = list(range(1, len(matrix)))
    infected = [0]
    t = 0
    print(free)
    while free:
        t+=1
        underattack = []
        for i in infected:
            for j in free:
                if matrix[i][j] == 1 and j not in underattack:
                    underattack.append(j)
        for j in underattack:
            matrix[j][j] -= 1
            if matrix[j][j] == 0:
                free.remove(j)
                infected.append(j)

    print(t)
    return t

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

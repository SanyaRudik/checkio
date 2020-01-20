def weak_point(matrix):
    n_x = [sum(x) for x in matrix]
    n_y = [sum(y) for y in zip(*matrix)]
    return n_x.index(min(n_x)), n_y.index(min(n_y))


if __name__ == '__main__':
    print(weak_point([[7, 2, 7, 2, 8],
                      [2, 9, 4, 1, 7],
                      [3, 8, 6, 2, 4],
                      [2, 5, 2, 9, 1],
                      [6, 6, 5, 4, 5]]))  # == [3, 3], "Example"
    print(weak_point([[7, 2, 4, 2, 8],
                      [2, 8, 1, 1, 7],
                      [3, 8, 6, 2, 4],
                      [2, 5, 2, 9, 1],
                      [6, 6, 5, 4, 5]]))  # == [1, 2], "Two weak point"
    print(weak_point([[1, 1, 1],
                      [1, 1, 1],
                      [1, 1, 1]]))  # == [0, 0], "Top left"

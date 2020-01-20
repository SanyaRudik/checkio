def sum_row_column(x_m, y_m, matrix):
    n_x = [matrix[x][y_m] for x in range(len(matrix))]
    n_y = [matrix[x_m][y] for y in range(len(matrix[0]))]
    return sum(n_x + n_y)


def weak_point(matrix):
    weak = [[x, y, sum_row_column(x, y, matrix)] for x in range(len(matrix)) for y in range(len(matrix[0]))]
    return sorted(weak, key=lambda kv: kv[2])[0][:2]


if __name__ == '__main__':
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"

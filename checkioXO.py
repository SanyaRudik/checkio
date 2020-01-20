from typing import List


def f(a, b, c):
    if a == b == c == "X":
        return True
    if a == b == c == "O":
        return True
    return False


def check_io(game_map):
    if f(game_map[0][0], game_map[1][0], game_map[2][0]):
        return game_map[0][0]
    if f(game_map[0][1], game_map[1][1], game_map[2][1]):
        return game_map[0][1]
    if f(game_map[0][2], game_map[1][2], game_map[2][2]):
        return game_map[0][2]
    if f(game_map[0][0], game_map[0][1], game_map[0][2]):
        return game_map[0][0]
    if f(game_map[1][0], game_map[1][1], game_map[1][2]):
        return game_map[1][0]
    if f(game_map[2][0], game_map[2][1], game_map[2][2]):
        return game_map[2][0]
    if f(game_map[0][2], game_map[1][1], game_map[2][0]):
                        return game_map[0][2]
    if f(game_map[2][2], game_map[1][1], game_map[0][0]):
        return game_map[2][2]
    return 'D'


if __name__ == '__main__':
    print("Example:")
    print(check_io([".OX","..X",".OX"]))

    print(check_io([
        "X.O",
        "XX.",
        "XOO"]))
    print(check_io([
        "OO.",
        "XOX",
        "XOX"]))  # == "O", "Os wins"
    print('   ', check_io([
        "OOX",
        "XXO",
        "OXX"]))  # == "D", "Draw"
    print(check_io([
        "O.X",
        "XX.",
        "XOO"]))  # == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

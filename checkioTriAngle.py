from typing import List
import math


def check_io(a: int, b: int, c: int) -> List[int]:
    if (a < b + c) and (b < a + c) and (c < a + b):
        angle_a = int(round(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))))
        angle_b = int(round(math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))))
        angle_y = int(round(math.degrees(math.acos((b ** 2 + a ** 2 - c ** 2) / (2 * a * b)))))
    else:
        return [0, 0, 0]
    return [angle_a, angle_b, angle_y]


if __name__ == '__main__':
    print("Example:")
    print(check_io(4, 4, 4))
    print(check_io(3, 4, 5))
    print(check_io(2, 2, 5))


    #
    # assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    # assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    # assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    # print("Coding complete? Click 'Check' to earn cool rewards!")

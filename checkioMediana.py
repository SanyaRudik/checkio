from typing import List


def checkio(data: List[int]) -> [int, float]:
    if len(data) % 2 == 0:
        print((sorted(data)[len(data) // 2], sorted(data)[len(data) // 2-1]))
        return (sorted(data)[len(data) // 2] + sorted(data)[len(data) // 2-1]) / 2
    else:
        return sorted(data)[len(data)//2]

    # replace this for solution


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))
    print(checkio([1, 300, 2, 200, 1]))
    print(checkio([3, 6, 20, 99, 10, 15]))
    # assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    # assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    # assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    # assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    # print("Start the long test")

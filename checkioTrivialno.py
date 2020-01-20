def count_consecutive_summers(num):
    x = 0
    x1 = 0
    for i in range(1, num+1):
        x = 0
        for c in range(i,num+1):
            x += c
            if x == num:
                x1 += 1
                x = 0
                print(c)
                break
        # print(i)

    return x1


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(99))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert count_consecutive_summers(42) == 4
    # assert count_consecutive_summers(99) == 6
    # assert count_consecutive_summers(1) == 1
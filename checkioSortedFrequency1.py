def frequency_sort(items):
    # your code here
    try:
        s = list(map(str, items))
    except:
        s = items
    s = sorted(s, key=lambda c: (s.count(c), len(s) - ''.join(s).find(c)), reverse=True)
    try:
        s = list(map(int, s))
    except:
        pass
    return s


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']))
    print(frequency_sort([17, 99, 42, 42]))
    print(frequency_sort([]))
    print(frequency_sort([1]))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    # assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    # assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    # assert list(frequency_sort([])) == []
    # assert list(frequency_sort([1])) == [1]
    # print("Coding complete? Click 'Check' to earn cool rewards!")

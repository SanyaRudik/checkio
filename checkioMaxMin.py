def min1(*args, **kwargs):
    return sorted(iter(args[0]) if len(args) == 1 else args,
                  key=kwargs.get("key", None))[0]


def max1(*args, **kwargs):
    return sorted(iter(args[0]) if len(args) == 1 else args,
                  key=kwargs.get("key", None), reverse=True)[0]


def min(*args, key=None, rev=False):
    return sorted(args if len(args) > 1 else args[0], key=key, reverse=rev)[0]


def max(*args, key=None):
    return sorted(args if len(args) > 1 else args[0], key=key, reverse=True)[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    print(max([1, 2, 0, 3, 4]))  # == 4, "From a list"
    print(min("hello"))  # == "e", "From string"
    print(max(2.2, 5.6, 5.9, key=int))  # == 5.6, "Two maximal items"
    print(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))  # == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

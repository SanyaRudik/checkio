from math import exp as e, log as l


def super_root(n):
    f = lambda w, x: w if (e(w) * w - x) / (w * e(w) + e(w)) <= 10e-15 else f(w - (e(w) * w - x) / (w * e(w) + e(w)), x)
    return e(f(*[l(n)] * 2))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        print(result)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 27), "Cube"
    assert check_result(super_root, 4844), "Eighty one"
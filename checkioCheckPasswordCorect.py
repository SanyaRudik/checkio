def checkio(data: str) -> bool:
    # replace this for solution
    lower, upper, digital, length = False, False, False, False;
    for x in data:
        if (x >= 'a') and (x <= 'z'):
            lower = True
        if (x >= 'A') and (x <= 'Z'):
            upper = True
        if (x >= '0') and (x <= '9'):
            digital = True
        if len(data) >= 10:
            length = True
        if lower and upper and digital and length:
            return True

    return False


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    print(checkio('A1213pokl'))
    print(checkio('bAse730onE4'))
    print(checkio('asasasasasasasaas'))
    print(checkio('QWERTYqwerty'))
    print(checkio('123456123456'))
    print(checkio('QwErTy911poqqqq'))
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

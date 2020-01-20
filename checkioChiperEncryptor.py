def to_encrypt(text, delta):
    s = ''
    for i in text:
        if (i >= 'a') and (i <= 'z'):
            if ord(i)+delta > 122:
                s += chr(ord(i)+delta-122+96)
            elif ord(i)+delta < 97:
                s += chr(122-(96-ord(i)+abs(delta)))
            else:
                s += chr(ord(i)+delta)
        else:
            s += i
    return s


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', -1))

    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")

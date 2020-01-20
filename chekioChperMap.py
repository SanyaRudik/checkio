def generator(password):
    for i in password:
        for c in i:
            yield c


def recall_password(cipher_grille, ciphered_password):
    a = ''
    n = generator(ciphered_password)
    for i in range(len(cipher_grille)):
        for c in range(len(cipher_grille[0])):
            X = next(n)
            if cipher_grille[i][c] == "X":
                a += X

    n = generator(ciphered_password)
    for c in range(len(cipher_grille[0])):
        for i in range(len(cipher_grille) - 1, -1, -1):
            X = next(n)
            if cipher_grille[i][c] == "X":
                a += X

    n = generator(ciphered_password)
    for i in range(len(cipher_grille) - 1, -1, -1):
        for c in range(len(cipher_grille[0]) - 1, -1, -1):
            X = next(n)
            if cipher_grille[i][c] == "X":
                a += X

    n = generator(ciphered_password)
    for c in range(len(cipher_grille[0]) - 1, -1, -1):
        for i in range(len(cipher_grille)):
            X = next(n)
            if cipher_grille[i][c] == "X":
                a += X

    return a


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')))  # == 'icantforgetiddqd', 'First example'

    print(recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')))  # == 'rxqrwsfzxqxzhczy', 'Second example'

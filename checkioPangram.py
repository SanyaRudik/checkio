def check_pangram(text):
    t = ''
    for i in text.lower():
        if 'a' <= i <= 'z':
            if i not in t:
                t += i
    print(text)
    print('|' + '|'.join(sorted(t)) + '|', '-', len(t))
    '''
  ______________________   
 |   Для наглядности    |
 |______________________|
    '''

    if len(t) == 26:
        return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    check_pangram("The quick brown fox jumps over the lazy dog.")
    check_pangram("ABCDEF")
    check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!")
    # print('If it is done - it is Done. Go Check is NOW!')

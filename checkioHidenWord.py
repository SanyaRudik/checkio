def checkio(text, word):
    st = text.replace(' ', '').split('\n')
    # print(st)
    for i in st:
        low_text = i.lower().find(word)
        if low_text != -1:
            print([st.index(i) + 1, low_text + 1, st.index(i) + 1, low_text + len(word)])
            return [st.index(i) + 1, low_text + 1, st.index(i) + 1, low_text + len(word)]
    a = []
    for i in range(300):
        a.append('')
        for ii in range(len(st)):
            if i <= len(st[ii]) - 1:
                a[i] += st[ii][i]
            else:
                a[i] += ' '
        if len(a[i].replace(' ', '')) == 0:
            break
    for i in a:
        low_text = i.lower().find(word)
        if low_text != -1:
            print([low_text + 1, a.index(i) + 1, low_text + len(word), a.index(i) + 1])
            return [low_text + 1,a.index(i) + 1, low_text + len(word), a.index(i) + 1]
    return


if __name__ == '__main__':
    checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten")  # == [2, 14, 2, 16]
    checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir")  # == [4, 16, 7, 16]

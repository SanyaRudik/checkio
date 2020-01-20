def check(all_num,matix):
    k = ''
    for i in range(len(all_num)):
        if matix[i] == '1':
            k += all_num[i]
    return k

def combi(list_number):
    a = []
    for bit in range(2 ** (len(list_number)), 2 ** (len(list_number) + 1)):
        s = str(bin(bit))[3:]
        a.append(check(list_number, s))
    return a
def segment(lit_seg, broken_seg):
    didgit = {
        1: 'BC',
        2: 'ABGED',
        3: 'ABCDG',
        4: 'FBGC',
        5: 'AFGCD',
        6: 'AFEGDC',
        7: 'ABC',
        8: 'AFBGECD',
        9: 'AFGBCD',
        0: 'AFBEDC'}
    a = []
    b = []
    didg = []
    for i in lit_seg:
        if i.isupper():
            a.append(i)
    for i in broken_seg:
        if i.isupper():
            b.append(i)
    for c in combi(''.join(b)):
        for i in didgit:
            if sorted((didgit[i])) == sorted(list(a) + list(c)):
                didg.append(i)

    return didg

def seven_segment(lit_seg, broken_seg):
    finish_pac =[]
    for i in segment(lit_seg, broken_seg):
        for c in segment(list(''.join(lit_seg).swapcase()),list(''.join(broken_seg).swapcase())):
            finish_pac.append(str(i)+str(c))
    return len(list(map(str,finish_pac)))


if __name__ == '__main__':
    print(seven_segment({'B', 'C', 'b', 'c'}, {'A'}))  # == 2, '11, 71'
    print(seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}))  # == 6, '15, 16, 35, 36, 75, 76'
    print(seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}))  # == 20, '15...98'
    # print('"Run" is good. How is "Check"?')

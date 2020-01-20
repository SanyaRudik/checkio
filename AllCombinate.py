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

for c,i in enumerate(combi('ABC1545456')):
    print(c+1, '-', i)
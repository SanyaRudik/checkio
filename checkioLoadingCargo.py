def check(all_num,matix):
    k = 0
    for i in range(len(all_num)):
        if matix[i] == '1':
            k += all_num[i]
    return k


def checkio(all_num):
    a = []
    for bit in range(2**(len(all_num)), 2**(len(all_num)+1)):
        s = str(bin(bit))[3:]
        a.append(check(all_num, s))
    n = sum(all_num) - list(filter(lambda item: item >= sum(all_num)//2, sorted(a)))[0]
    return abs(list(filter(lambda item: item >= sum(all_num)//2, sorted(a)))[0] - n)


if __name__ == '__main__':
    print(checkio([10, 10]))  # == 0, "1st example"
    print(checkio([10]))  # == 10, "2nd example"
    print(checkio([5, 8, 13, 27, 14]))  # == 3, "3rd example"
    print(checkio([5, 5, 6, 5]))  # == 1, "4th example"
    print(checkio([12, 30, 30, 32, 42, 49]))  # == 9, "5th example"
    print(checkio([1, 1, 1, 3]))  # == 0, "6th example"

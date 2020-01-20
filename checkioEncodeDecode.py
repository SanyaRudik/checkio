def f(key):
    if 0 <= key <= 6:
        k = ['A', 'D', 'F', 'G', 'V', 'X']
        return str(k[key])
    return "ERROR"


def ff(key):
    k = ['A', 'D', 'F', 'G', 'V', 'X']
    for i, c in enumerate(k):
        if c == key:
            return i
    return -1


def tab_secret(secret_alphabet):
    for i in secret_alphabet:
        yield i


def corect_keyword(message):
    message = message[::-1]
    for i in message:
        if message.count(i) > 1:
            message = message.replace(i, '', 1)
    message = message[::-1]
    return message


def encode(message, secret_alphabet, keyword):
    s = ''
    dd = []
    g = tab_secret(secret_alphabet)
    d = [[next(g) for i in range(6)] for c in range(6)]
    keyword = corect_keyword(keyword)
    message = message.replace(' ', '').lower()

    for i in message:
        for ii, c in enumerate(d):
            for i_i, cc in enumerate(c):
                if cc == i:
                    s += (f(ii) + f(i_i))
                    break

    for i in keyword:
        dd.append([i, ''])
    ii = 0
    for i in s:
        if ii == len(keyword):
            ii = 0
        dd[ii][1] += i
        ii += 1
    dd = dict(dd)
    s = ''
    for i in sorted(keyword):
        s += dd.get(i)
    return s


def decode(message, secret_alphabet, keyword):
    s = []
    dd = []
    ss = ''
    s1 = ''
    x = 0
    g = tab_secret(secret_alphabet)
    d = [[next(g) for i in range(6)] for c in range(6)]
    keyword = corect_keyword(keyword)
    key_sorted = sorted(keyword)
    for i in keyword:
        dd.append([i, ''])
    ii = 0
    for i in message:
        if ii == len(keyword):
            ii = 0
        dd[ii][1] += i
        ii += 1
    dd = dict(dd)
    ii = -1
    for x, i in enumerate(key_sorted):
        s.append([i, ''])
        for c in range(len(dd.get(i))):
            ii += 1
            s[x][1] += message[ii]
    s = dict(s)
    dd = list(dd)
    dd = []
    for i in keyword:
        dd.append([i, s.get(i)])
    i = 0
    ii = -1
    x = 0
    while len(ss) < len(message):
        if ii == len(keyword) - 1:
            ii = -1
            x += 1
        ii += 1
        ss += dd[ii][1][x]
    for i in range(0, len(ss), 2):
        s1 += d[ff(ss[i])][ff(ss[i+1])]

    return s1



if __name__ == '__main__':
    print(encode("I am going",
                 "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                 "cipcher"))  # == 'FXGAFVXXAXDDDXGA', "encode I am going"

    print(decode("FXGAFVXXAXDDDXGA",
                 "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                 "cipher"))  # == 'iamgoing', "decode I am going"
    print(encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy"))# == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    print(decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy"))# == 'attackat1200am', "decode attack"
    print(encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten"))# == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    print(decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten"))# == 'ditiszeergeheim', "decode ditiszeergeheim"
    print(encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel"))
    # == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    print(decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel"))# == 'iamgoing', "decode weasel == weasl"

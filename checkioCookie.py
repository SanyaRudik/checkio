def get_cookie(cookie, name):
    # cookie.find(name+'=')
    s = ''
    for i in range(cookie.find(name+'=')+len(name)+1,len(cookie)):
        if i < len(cookie) and (cookie[i] != ';'):
            s += cookie[i]
        else:
            break

    return s


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(get_cookie('theme=light; sessionToken=abc123', 'theme'))  # == 'light', 'theme=light'
    print(get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo'))  # == 'true', 'ffo=true'
    print(get_cookie("domain=checkio.org; theme=dark", "domain"))
    # print("Looks like you know everything. It is time for 'Check'!")

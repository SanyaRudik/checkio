def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=None):
    if powers is None:
        powers = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    powers_ = powers.copy()
    result, power = number, powers_.pop(0)
    while abs(result) >= base and powers_:
        if decimals:
            result /= base
        elif result < 0:
            result = int(result / base)
        else:
            result //= base
        power = powers_.pop(0)

    return f'{result:.{decimals}f}{power}{suffix}'
    # .format(result, pw=power, sf=suffix, dec=decimals)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(friendly_number(255000000000, powers=['', 'd', 'D']))  # == '102', '102'
    print(friendly_number(10240))  # == '10k', '10k'
    print(friendly_number(12341234, decimals=1))  # == '12.3M', '12.3M'
    print(friendly_number(12461, decimals=1))  # == '12.5k', '12.5k'
    print(friendly_number(1024000000, base=1024, suffix='iB'))  # == '976MiB', '976MiB'

from datetime import datetime


def broken_clock(starting_time, wrong_time, error_description):
    timedic = {'second': 1, 'minute': 60, 'hour': 3600, 'seconds': 1, 'minutes': 60, 'hours': 3600}

    # analyze starting time and wrong time
    st = datetime.strptime(starting_time, '%H:%M:%S')
    wt = datetime.strptime(wrong_time, '%H:%M:%S')
    print(st)

    # analyze error_description
    n1, unit1, _, n2, unit2 = error_description.split()
    sec1 = int(n1) * timedic[unit1]  # 1st seconds
    sec2 = int(n2) * timedic[unit2]  # 2nd seconds

    # return correct time
    return (st + (wt - st) * sec2 / (sec1 + sec2)).strftime('%X')


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    print(broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds'))  # == '00:00:10', "First example"
    print(broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds'))  # == '06:10:30', 'Second example'
    print(broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute'))  # == '14:00:00', 'Third example'
    print(broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours'))  # == '07:05:05', 'Fourth example'
    print(broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds'))  # == '00:00:22', 'Fifth example

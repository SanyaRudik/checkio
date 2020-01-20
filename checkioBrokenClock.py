def broken_clock(starting_time, wrong_time, error_description):
    time = [['second', 1], ['minute', 60], ['hour', 3600]]
    description = 0
    s = ''
    s_wrong = ''
    for c, i in enumerate(error_description):
        if i == ' ':
            # print(error_description[:c])
            description = int(error_description[:c])
            s = error_description[c:]
            for ti in time:
                # print(s.find(ti[0]),ti[0],s)
                if s.find(ti[0]) >= 0:
                    # print(s, ti[0])
                    description = description * ti[1]
                    break
            break
    for c, i in enumerate(s):
        if i.isdigit():
            s_wrong += i
    s = s[s.find(s_wrong)+len(s_wrong):]
    des_two = int(s_wrong)
    for ti in time:
        # print(s.find(ti[0]),ti[0],s)
        if s.find(ti[0]) >= 0:
            # print(s, ti[0])
            des_two = des_two * ti[1]
            break
    # print(des_two, s)
    description = des_two // description



    defren = int(starting_time[:2]) * time[2][1] + int(starting_time[3:5]) * time[1][1] + int(starting_time[6:]) * time[0][1]
    defren = (int(wrong_time[:2]) * time[2][1] + int(wrong_time[3:5]) * time[1][1] + int(wrong_time[6:]) * time[0][1]) - defren
    # print('\n ---', defren)
    return description

if __name__ == "__main__":
    print(broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds'))  # == '00:00:10', "First example"
    print(broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds'))  # == '06:10:30', 'Second example'
    print(broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute'))  # == '14:00:00', 'Third example'
    print(broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours'))  # == '07:05:05', 'Fourth example'
    print(broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds'))  # == '00:00:22', 'Fifth example'

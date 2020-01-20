def Translation(Numer):
    Numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
               'nine', 'ten', 'eleven',
               'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
               'eighteen',
               'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
               'eighty', 'ninety', 'hundred', 'thousand', 'million', 'billion', 'trillion']
    n = str(Numer)
    if len(n) == 1:
        n = '0' + n
    if int(n) == 0:
        return ''
    elif int(n) < 20:
        return Numbers[int(n) - 1]
    elif int(n) < 100:
        return Numbers[int(n[0]) + 17] + ' ' + Translation(n[1])
    elif int(n) < 1000:
        return Translation(int(n[0])) + ' ' + Numbers[27] + ' ' + Translation(int(n[1:3]))


for i in range(150):
    print(Translation(i))

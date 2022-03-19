import re

def hms(s):
    l = list(map(int, re.split('[wdhms]', s)[:-1]))
    if len(l) == 5:
        return l[0]*604800 + l[1]*86400 + l[2]*3600 + l[3]*60 + l[4]
    elif len(l) == 4:
        return l[0]*86400 + l[1]*3600 + l[2]*60 + l[3]
    elif len(l) == 3:
        return l[0]*3600 + l[1]*60 + l[2]
    elif len(l) == 2:
        return l[0]*60 + l[1]
    else:
        return l[0]


item = '4d22h11m58'

print(hms(item))

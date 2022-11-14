def romanToInt(s: str):

    l1 = 'none'

    num = 0

    roman = ['I','V','X','L','C','D','M']

    for l2 in s:

        if l2 == roman[0]:
            num+=1
        elif l2 == roman[1]:
            num+=5
        elif l2 == roman[2]:
            num+=10
        elif l2 == roman[3]:
            num+=50
        elif l2 == roman[4]:
            num+=100
        elif l2 == roman[5]:
            num+=500
        else:
            num+=1000


        if (l1 == roman[0]) and (l2 == roman[1] or l2 == roman[2]):
            num -=2
            
        if (l1 == roman[2]) and (l2 == roman[3] or l2 == roman[4]):
            num -=2

        if (l1 == roman[4]) and (l2 == roman[5] or l2 == roman[6]):
            num -=2

        l1 = l2

    return num

print(romanToInt("III"))
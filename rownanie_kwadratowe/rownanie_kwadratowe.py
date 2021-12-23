def rownanie_kwadratowe():
    #own interpretation
    z = input('Rownanie: ').split()
    z = [float(x) for x in z]
    if z[0] == 0:
        print('To nie równanie kwadratowe')
    else:
        delta = z[1]**2 - 4*z[0]*z[2]
        if delta > 0:
            x1 = (z[1]-delta**0.5)/2*z[0]
            x2 = (z[1]+delta**0.5)/2*z[0]
            print(2)
        elif delta == 0:
            x1 = (z[1])/2*z[0]
            print(1)
        else:
            print(0)

rownanie_kwadratowe()
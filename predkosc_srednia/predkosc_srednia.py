def predkosc_srednia():
    l = (input("Testy: ")).strip()
    lst = []
    for i in range(int(l)):
        z = input("Liczby: ").split()
        z = [int(i) for i in z]
        e = 1
        f = 1
        v1 = z[0]
        v2 = z[1]
        
        #szukanie nww
        while True:
            if v1 == v2:
                break
            elif v1 > v2:
                v2 += z[1] 
                #print("v1: ", v1)
                f += 1
            else:
                v1 += z[0]
                #print("v1: ", v1)
                e += 1

        res = (v1/(e+f))*2
        lst.append(res)
    for i in lst:
        print(int(i))

predkosc_srednia()
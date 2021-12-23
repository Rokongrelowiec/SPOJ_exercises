def pesel():
    l = (input("Testy: ")).strip()
    lst = []
    for i in range(int(l)):
        z = input("Pesel: ").strip()
        lst1 = []
        sum = 0

        for e in range(len(z)):
            if e == 0 or e == 4 or e == 8 or e == 10:
                lst1.append(int(z[e])*1)
            elif e == 1 or e == 5 or e == 9:
                lst1.append(int(z[e])*3)
            elif e == 2 or e == 6:
                lst1.append(int(z[e])*7)
            elif e == 3 or e == 7:
                lst1.append(int(z[e])*9)

        for w in lst1:
            sum += w

        sum = str(sum)
        if sum[-1] == '0':
            lst.append('D')
        else:
            lst.append('N')
    
    for q in lst:
        print(q)
    
pesel()
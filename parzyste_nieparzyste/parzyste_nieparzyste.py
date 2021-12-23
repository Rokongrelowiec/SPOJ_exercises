def parzyste_nieparzyste():
    lstX = []
    l = (input("Testy: ")).strip()
    for i in range(int(l)):
        z = input("Ciąg: ").split()
        lst = []
        for e in range(2, len(z), 2):
            lst.append(z[e])
        for e in range(1, len(z), 2):
            lst.append(z[e])
        res = ' '.join(lst)
        #print(res)
        lstX.append(res)
    for i in lstX:
        print(i)

parzyste_nieparzyste()
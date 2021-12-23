def nwd():
    l = (input("Testy: ")).strip()
    lst = []
    for i in range(int(l)):
        z = (input("Liczby: ")).split()
        z = [int(e) for e in z]
        s = 1
        if z[0] > z[1]:
            max = z[0]
        else:
            max = z[1]
        for i in range(1, max):
            if z[0]%i == 0 and z[1]%i == 0:
                s = i
        lst.append(s)
    
    for y in lst:
        print(y)

nwd()
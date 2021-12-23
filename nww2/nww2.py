
def nww2():
    w = input("Testy: ").strip()
    lst = []
    for e in range(int(w)):
        lst_1 = []
        o = input("Number of elements: ") # ta linia moze zostac usunieta
        # powyzsza linia istnieje tylko na potrzebe testu
        
        z = input("Wejście: ").split()
        z = [int(x) for x in z]
        lst_1 = z[:]
        
        min1 = 0
        for i in range(len(z)):
            if z[i] < z[min1]:
                min1 = i

        while True:
            var = True

            for i in range(len(lst_1)):
                if lst_1[i] != lst_1[min1]:
                    var = False

            if var:
                lst.append(lst_1[min1])
                break
            else:
                for i in range(len(lst_1)):
                    if lst_1[i] < lst_1[min1]:
                        min1 = i
                lst_1[min1] += z[min1]
                
    for i in lst:
        print(i)
                
nww2()
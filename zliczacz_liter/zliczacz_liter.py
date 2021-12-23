def zliczacz_liter():
    a = int(input("Linie: "))
    dct = {}
    for i in range(a):
        z = input("Zdanie: ")
        for i in z:
            if i != " ":
                if i in dct:
                    dct[i] += 1
                else:
                    dct[i] = 1

    for e,y in dct.items():
        print(e, y)
        
zliczacz_liter()
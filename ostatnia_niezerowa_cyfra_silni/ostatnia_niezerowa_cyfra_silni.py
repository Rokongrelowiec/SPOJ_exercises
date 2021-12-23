def ostatnia_niezerowa_cyfra_silni():
    w = int(input("Testy: ").strip())
    lst = []
    for e in range(w):
        z = int(input("Wejście: ").strip())
        sum = 1
        for i in range(1, z+1):
            sum *= i

        sum = str(sum)
        if len(sum) > 1:
            for w in sum[::-1]:
                if w != '0':
                    lst.append(w)
                    break     
        else:
            lst.append(sum)
    for i in lst:
        print(i)

ostatnia_niezerowa_cyfra_silni()
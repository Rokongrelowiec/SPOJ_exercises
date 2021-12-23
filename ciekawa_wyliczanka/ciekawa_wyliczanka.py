def ciekawa_wyliczanka():
    w = int(input("Wejscie: ").strip())
    lst = [5, ]
    i = lst[0]

    while len(lst) < w:
        i = int(i)
        i += 1
        i = str(i)
        for e in i:
            if (e == '5' or e == '6'):
                continue
            else:
                break
        else:
            lst.append(i)

    print(lst[w-1])
        
ciekawa_wyliczanka()
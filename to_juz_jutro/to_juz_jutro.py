def to_juz_jutro():
    w = int(input("Testy: ").strip())
    lst = []
    for e in range(w):
        z = input("Wejscie: ").split()
        s = [int(x) for x in z]
        if s[1] % s[0] == 0:
            lst.append('TAK')
        else:
            lst.append('NIE')
    
    for i in lst:
        print(i)
    
to_juz_jutro()
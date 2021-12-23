def test3():
    #onw interpretation
    i = 0
    lst = []
    while i<3:
        z = int(input("Input: "))
        lst.append(z)
        if z == 42:
            if len(lst) > 1 and lst[-2] != 42:
                i += 1
        print(z)
        
test3()
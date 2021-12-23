
def dodawanie_rzymskie():
    w = input("Wejscie: ").split()
    lst_1 = []
    sum_lst_1 = 0
    lst_2 = []
    sum_lst_2 = 0
    lst_roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    lst_spec = {4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}

    for i in w[0]:
        if i == lst_roman[1]:
            lst_1.append(1)
        elif i == lst_roman[5]:
            lst_1.append(5)
        elif i == lst_roman[10]:
            lst_1.append(10)
        elif i == lst_roman[50]:
            lst_1.append(50)
        elif i == lst_roman[100]:
            lst_1.append(100)
        elif i == lst_roman[500]:
            lst_1.append(500)
        elif i == lst_roman[1000]:
            lst_1.append(1000)

    for i in w[1]:
        if i == lst_roman[1]:
            lst_2.append(1)
        elif i == lst_roman[5]:
            lst_2.append(5)
        elif i == lst_roman[10]:
            lst_2.append(10)
        elif i == lst_roman[50]:
            lst_2.append(50)
        elif i == lst_roman[100]:
            lst_2.append(100)
        elif i == lst_roman[500]:
            lst_2.append(500)
        elif i == lst_roman[1000]:
            lst_2.append(1000)
            

    for s in range(len(lst_1)-1):
        if (lst_1[s] < lst_1[s+1]):
            sum_lst_1 += (-1*lst_1[s])
        else:
            sum_lst_1 += lst_1[s]
    else:
        sum_lst_1 += lst_1[len(lst_1)-1]
        
    #print(sum_lst_1)

    for s in range(len(lst_2)-1):
        if (lst_2[s] < lst_2[s+1]):
            sum_lst_2 += (-1*lst_2[s])
        else:
            sum_lst_2 += lst_2[s]
    else:
        sum_lst_2 += lst_2[len(lst_2)-1]
        
    #print(sum_lst_2)

    res = sum_lst_1 + sum_lst_2
    #print(res)

    # below convert result into Roman number!
    # MAX -> 2000

    out = ''
    # lst_roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    # lst_spec = {4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}

    while res != 0:
        max_r = 0
        max_s = 0
        for i in lst_roman:
            if i <= res:
                max_r = i
            else:
                break
        for i in lst_spec:
            if i <= res:
                max_s = i
            else:
                break
        if max_r > max_s:
            out += lst_roman[max_r]
            res -= max_r
        else:
            out += lst_spec[max_s]
            res -= max_s
    print(out)
                

dodawanie_rzymskie()
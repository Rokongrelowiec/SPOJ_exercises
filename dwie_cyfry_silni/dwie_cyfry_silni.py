def dwie_cyfry_silni():
    case = int(input("Cases:"))
    for e in range(case):
        sum = 1
        n = int(input("Num: "))
        for i in range(1, n+1):
            sum *= i
        sum = str(sum)
        if len(sum) <= 1:
            print(0, sum)
        else:
            print(sum[-2], sum[-1])

dwie_cyfry_silni()
def spacje():
    word = input('Word: ')
    word = word.split()
    new = ""
    for i in word:
        i = i[0].upper() + i[1:]
        new += i
    print(new)
    
spacje()
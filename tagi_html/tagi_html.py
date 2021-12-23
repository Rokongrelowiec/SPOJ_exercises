def tagi_html():
    lst = []
    while True:
        tag = input('Tag input: ')
        tag_res = ""
        a = False

        for i in tag:
            if a == True:
                tag_res += i.upper()
            elif i == "<":
                a = True
                tag_res += "<"
            elif i == ">":
                a = False
                tag_res += ">"
            else:
                tag_res += i
        lst.append(tag_res)

        if tag_res == "</HTML>":
            break
    
    for i in lst:
        print(i)
        
tagi_html()
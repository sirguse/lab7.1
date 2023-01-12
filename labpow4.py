def znaki(a):
    s = {}
    for x in a: # x to będą pojedyńcze znaki
        if x in s:
            s[x] +=1
        else:
            s[x] = 1
    return s
print(znaki(a))



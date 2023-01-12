def find(a,b):
    l = []
    for x in range(len(a)):
        if a[x] == b:
            l.append(x)
    return l
print(find([10, 3, 5, 3, 2, 1], 3))

L = [5, 7, 9, 5]

wynik = find(L, 5)
print(wynik)
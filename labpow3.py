def potega(lista1,lista2):
    lista3=[]
    if len(lista1)==len(lista2):
        for x in range(len(lista1)):
            lista3.append(lista1[x]**lista2[x])
    return lista3
lista1=[2,2,2]
lista2=[0,1,2]
print(potega(lista1,lista2))
    
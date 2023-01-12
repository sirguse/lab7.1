def dodawanie(a,b):
    return a+b

def odejmowanie(a,b):
    return a-b

def mnozenie(a,b):
    return a*b

def dzielenie(a,b):
    if b == 0:
        return None
    else:
        return a/b

dzialanie = {'+': dodawanie, '-': odejmowanie, '/': dzielenie, '*': mnozenie}

x = input("Jakie działanie? ")
a = input("Podaj pierwszą liczbe: ")
b = input("Podaj drugą liczbe: ")
print(dzialanie[x](a,b))













def dodawanie(a,b):
    return a+b
def odejmowanie(a,b):
    return a-b
def mnozenie(a,b):
    return a*b
def dzielenie(a,b):
    if b == 0:
        return None
    else:
        return a/b
dzialanie = {'+': dodawanie, '-': odejmowanie, '*': mnozenie, '/': dzielenie}
x = input("Jakie działanie? ")
a = int(input("Podaj 1 liczbe: "))
b = int(input("Podaj 2 liczbe: "))
print(dzialanie[x](a,b))
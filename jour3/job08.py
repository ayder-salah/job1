a = float(input("longueur :"))
b = float(input("longueur :"))
c = float(input("longueur :"))
if a + b > c and a + c > b and b + c > a:
    print("le triangle est possible")
    if a == b and b == c:
        print("le triangle est équilatéral")
    elif a == b or a == c or b == c:
        print("le triangle est isocèle")
else:
    print("le triangle n'est pas possible")

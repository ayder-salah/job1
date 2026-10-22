capital = (10000)
taux = (5)
gain = capital * taux / 100
print("gain annuel :", gain)
capital = capital + 5000
taux = taux + 2
gain = capital * taux / 100
print("nouveau gain annuel :", gain)
capital = capital - capital * 10 / 100
taux = taux - 1
gain = capital * taux / 100
print("capital final :", capital)
print("nouveau gain annuel :", gain)
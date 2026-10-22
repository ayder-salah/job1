nom = "veste"
prix = 20
stock = 5

print("produit :" , nom, "prix :" , prix, ", stock :" , stock)
stock = stock + 5
print(stock)
quantite = int(input("combien de vestes souhaites-tu acheter ? "))
stock = stock - quantite
prix = prix * 1.10
print("produit :" , nom, "prix :" , prix, ", stock :", stock)  
def panier(type, saison):
    if type == "fruit" and saison == "hiver":
        return "orange, mandarine, kiwi"
    elif type == "fruit" and saison == "ete":
        return "poire, fraise, cassis"
    elif type == "legume" and saison == "hiver":
        return "carotte, topinambour, endive"
    elif type == "legume" and saison == "ete":
        return "artichaut, aubergine, poivron"

print(panier("fruit", "hiver"))
print(panier("fruit", "ete"))
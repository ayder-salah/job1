chaine = ("abcdefghijklmnopqrstuvwxyz") * 10
position = 0
taille = 1

while position + taille <= len(chaine):
    print(chaine[position : position + taille])
    position = taille + position
    taille = taille + 1

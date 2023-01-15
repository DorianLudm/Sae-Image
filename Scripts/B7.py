###Partie ENCODAGE###
texte_to_encode = "bonjourjesuisuntextegentil"
cle_encodage = "abcdefghijklmnopkrstuvwxyz"
lettre = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11,
          "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, 
          "v":22, "w":23, "x":24, "y":25, "z":26}
liste_val = []
texte_encoded = ""
if len(texte_to_encode) <= len(cle_encodage):
    for i in range(len(texte_to_encode)):
        liste_val.append(((lettre[texte_to_encode[i]]+lettre[cle_encodage[i]])%26))
    for val in liste_val:
        for (char, valeur) in lettre.items():
            if val == valeur:
                texte_encoded = texte_encoded + str(char)
    print(texte_encoded)
else:
    print("La clé doit être au moins de la même taille que le message à encoder")
    
###Partie DECODAGE###
texte_encoded = "cqqntayrncfuficjppmybakrhl"
liste_val = []
texte_decoded = ""
if len(texte_encoded) <= len(cle_encodage):
    for i in range(len(texte_encoded)):
        liste_val.append(((lettre[texte_encoded[i]]-lettre[cle_encodage[i]]+26)%26))
    for val in liste_val:
        for (char, valeur) in lettre.items():
            if val == valeur:
                texte_decoded = texte_decoded + str(char)
    print(texte_decoded)
else:
    print("La clé doit être au moins de la même taille que le message puisse être décodé")
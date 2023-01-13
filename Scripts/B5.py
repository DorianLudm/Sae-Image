from PIL import Image

#On modifie l'image initiale
i = Image.open("./Images/hall-mod_0.bmp")
sortie = i.copy()
for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        c = i.getpixel((x,y))
        valeur_R = c[0]-(c[0]%2)
        sortie.putpixel((x,y),(valeur_R,c[1],c[2]))
sortie.save("./Images/Imageout_steg_0.bmp")

#On obtient les valeurs de l'image à chacher
i = Image.open("./Images/Imageout3.bmp")
matrice = []
for x in range(i.size[0]): #Ligne
    matrice.append([])
    for y in range(i.size[1]): #Colonne
        matrice[x].append(None)

for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        c = i.getpixel((x,y))
        if (c[0]*c[0]+c[1]*c[1]+c[2]*c[2]) > 255*255*3/2:
            matrice[x][y] = 255 #Le pixel est blanc
        else:
            matrice[x][y] = 0 #Le pixel est noir

#On trouve l'image à cacher dans l'image modifiée
i = Image.open("./Images/Imageout_steg_0.bmp")
sortie = i.copy()
for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        c = i.getpixel((x,y))
        if x < len(matrice)  and y < len(matrice[0]) and matrice[x][y] == 255:
            sortie.putpixel((x,y),(255,255,255))
        elif x < len(matrice) and y < len(matrice[0]) and  matrice[x][y] == 0:
            sortie.putpixel((x,y),(0,0,0))
sortie.save("./Images/ImageCacheDecodee.bmp")
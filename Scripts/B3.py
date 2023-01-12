from PIL import Image

i = Image.open("./Images/ImageExemple.bmp")
sortie = i.copy()
for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        c = i.getpixel((x,y))
        gris = ((c[0]+c[1]+c[2])//3)
        sortie.putpixel((x,y),(gris,gris,gris))
sortie.save("./Images/Imageout2.bmp")
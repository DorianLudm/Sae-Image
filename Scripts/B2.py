from PIL import Image

i = Image.open("./Images/hall-mod_0.bmp")
sortie = i.copy()
for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        c = i.getpixel((x,y))
        sortie.putpixel((-x,y),(c))
sortie.save("./Images/Imageout1.bmp")
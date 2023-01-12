from PIL import Image

i = Image.open("./Images/Imagetest.bmp")
sortie = i.copy()
for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        c = i.getpixel((x,y))
        sortie.putpixel((y,x),(c))
sortie.save("./Images/Imageout0.bmp")
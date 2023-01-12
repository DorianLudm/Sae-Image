from PIL import Image

i = Image.open("./Images/ImageExemple.bmp")
sortie = i.copy()
for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        c = i.getpixel((x,y))
        if (c[0]*c[0]+c[1]*c[1]+c[2]*c[2]) > 255*255*3/2:
            sortie.putpixel((x,y),(255,255,255)) #Pixel blanc
        else:
            sortie.putpixel((x,y),(0,0,0)) #Pixel noir
sortie.save("./Images/Imageout3.bmp")
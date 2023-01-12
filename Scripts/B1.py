from PIL import Image

i = Image.open("./Images/Imagetest.bmp")
for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        c = i.getpixel((x,y))
        i.putpixel((x,y),(c))
i.save("./Images/Imageout0.bmp")
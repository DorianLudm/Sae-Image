from PIL import Image

i = Image.open("./Images/Image3.bmp")
for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        c = i.getpixel((x,y))
        i.putpixel((y,x),(c))
i.save("Imageout0.bmp")
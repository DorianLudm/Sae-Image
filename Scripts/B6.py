from PIL import Image

###PARTIE ENCODAGE###

#On modifie l'image initiale
i = Image.open("./Images/hall-mod_0.bmp")
sortie = i.copy()
for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        c = i.getpixel((x,y))
        valeur_R = c[0]-(c[0]%2)
        valeur_G = c[1]-(c[1]%2)
        valeur_B = c[2]-(c[2]%2)
        sortie.putpixel((x,y),(valeur_R,valeur_G,valeur_B))
sortie.save("./Images/Imageout_steg_1.bmp")

#On obtient les valeurs de l'image à chacher
text = "Ce texte va etre cache dans l'image" #Attention, il à la longueur de la chaine de charactères. Celle-ci ne doit pas dépasser 1/3 des pixels de l'image
list_val = []
for character in text:
    character_ascii = ord(character)
    character_binary = bin(character_ascii)[2:]
    while len(character_binary) < 8:
        character_binary = "0" + character_binary
    list_val.append(character_binary)
    
#On encode l'image
i = Image.open("./Images/Imageout_steg_1.bmp")
counter = -1
for pixel in range(0,(i.size[0])*(i.size[1]),3):
    counter +=1 
    y = pixel%(i.size[1]) #Colonne
    x = (pixel-y)//(i.size[0]-1)#Ligne
    if y + 1 >= i.size[1] or y + 2 >= i.size[1]:
        continue
    else:
        c1 = i.getpixel((x,y))
        c2 = i.getpixel((x,y+1))
        c3 = i.getpixel((x,y+2))
        i.putpixel((x,y),(c1[0]+int(list_val[counter][0]),c1[1]+int(list_val[counter][1]),c1[2]+int(list_val[counter][2])))
        i.putpixel((x,y+1),(c2[0]+int(list_val[counter][3]),c2[1]+int(list_val[counter][4]),c2[2]+int(list_val[counter][5])))
        i.putpixel((x,y+2),(c3[0]+int(list_val[counter][6]),c3[1]+int(list_val[counter][7]),c3[2]+(counter+1 >= len(text))))
        if (counter+1 >= len(text)):
            break
i.save("./Images/Imageout_steg_1.bmp")


###PARTIE DECODAGE###

#On décode désormais l'image
Stop = False
res = ""
i = Image.open("./Images/Imageout_steg_1.bmp")
for pixel in range(0,(i.size[0])*(i.size[1]),3):
    counter +=1 
    y = pixel%(i.size[1]) #Colonne
    x = (pixel-y)//(i.size[0]-1)#Ligne
    if Stop:
        break
    elif y + 1 >= i.size[1] or y + 2 >= i.size[1]:
        continue
    else:
        c1 = i.getpixel((x,y))
        c2 = i.getpixel((x,y+1))
        c3 = i.getpixel((x,y+2))
        character_binary = str(c1[0]%2) + str(c1[1]%2) + str(c1[2]%2) + str(c2[0]%2) + str(c2[1]%2) + str(c2[2]%2) + str(c3[0]%2) + str(c3[1]%2)
        res += chr(int(character_binary,2))
        Stop = c3[2]%2 == 1
print(res)
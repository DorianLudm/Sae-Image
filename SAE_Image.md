# SAE 1.03 - Image  

## Partie A  

Question 0:  
![Code de l'image 0](/RenduImages/Code0.png)  
Cette image peut s'obtenir à l'aide de l'application Okteta, qui permet d'obtenir le code de n'importe quelle image en binaire, octal, décimal ou hexadécimal.  
On utiliseras ici durant la plus grande partie du rendu l'héxadécimal par le fait qu'il est plus facile de lire les valeurs associées aux adresses.  

Expliquons désormais les valeurs que nous pouvons voir sur cette image:  
1) L'en-tête du fichier
- On apelle un octet (soit 8 bits) un duo de charactères, et une adresse la position de l'octet dans le fichier (index à 0).  
- A l'adresse 0x02, on peut retrouver la taille en bits du fichier défini sur 4 octets.
- A l'adresse 0x0A, on retrouve sur 4 octets l'adresse où on peut retrouver le début du codage des pixels, c'est à dire que allant à cette adresse, on trouveras le codage du premier pixel de l'image.
2) L'en-tête de la bitmap  
- L'adresse 0xOE permet de donner la taille de ce second en-tête. Cette taille est défini sur 4 octets.
- La largeur et la auteur de l'image sont respectivement définis aux adresses 0x12 et 0x14 sur 2 octets chaqu'un.  
- Enfin, à l'adresse 0x18 on peut retrouver le nombre de bits par pixel. Cette valeur est défini sur 4 octets.

Lorsqu'on essaye d'ouvrir l'image, on obtient l'erreur suivante:  
![Code de l'erreur de l'image A0](/RenduImages/Error_A0.png)  
Celle-ci se trouve par le fait que la taille du fichier entrée à l'adresse 0x02 n'est pas égale à la taille réelle du fichier. En effet, on code 99 73 0C 00 alors que le fichier possède une taille de 9A 73 0C 00  

Question 1:  

Question 2:  

Question 3:  

Question 4:  

Question 5:  

Question 6:  

Question 7:

Question 8:  

Question 9:  

Question 10:  
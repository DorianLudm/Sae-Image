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
En suivant la documentation donnée au début de la question, on peut facilement recoder une image de 4x4 facilement.  
![Image 0](/RenduImages/Image0_Rendu.png) 

Question 2:  
Pour efficacement arriver à l'image demandée dans cette question, on remarque que le fond est majoritairement rouge, ce qui nous permet alors de faciliter la construction en encodant tout les pixels avec 00 00 FF pour afficher une couleur rouge. Suite à cela, on ajoute alors les autres couleurs par dessus. Pour trouver facilement l'encodage des couleurs, on peut utiliser ctrl + F pour rechercher le nom de la couleur voulue, au lieu de la rechercher parmis les centaines de couleurs listées. Une fois avoir changer les 6 pixels qui ne sont pas rouges, on obtient alors l'image suivante:
![Image Test](/RenduImages/Imagetest_Rendu.png) 

Question 3:  
Pour répondre aux questions posées dans la question A.3, on utiliseras la documentation disponible via le lien [suivant](https://www.apprendre-en-ligne.net/info/images/formatbmp.pdf)  

- Pour trouver le nombre de bits par pixel, on lit l'adresse 0x1C sur 2 octets. Les deux images utilisent 18 bits par pixels, c'est à dire que chaque couleur primaire du codage RVB peut être parmis 256 possibilitées.
- Pour l'image 1, l'adresse 0x22 nous informe que la taille des données pixels est de 48 bits, codés par l'hexadécimal 30. Cette réponse peut aussi se retrouver par le calcul hauteur X largeur X nombre d'octets par pixel, soit 4x4x3= 48. Cette donnée n'est par ailleurs par disponible sur l'image 0.
- Pour définir si une compression est utilisé, il faut lire l'adresse 0x1E et regarder si la valeur est différente de 0. Pour l'image 1, on retrouve effectivement que cette valeur est nulle, ce qui signifie qu'aucune compression est utilisée.
- Enfin, l'encodage des pixels reste le même, on retrouve toujours le même ensemble de valeurs. Ils sont toujours codés en RVB, avec un octet couleur
  
Question 4:  

Question 5:  

Question 6:  

Question 7:

Question 8:  

Question 9:  

Question 10:  
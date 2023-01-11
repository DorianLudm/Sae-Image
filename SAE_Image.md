# SAE 1.03 - Image  

## Partie A  

### Question 0:  
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

### Question 1:  
En suivant la documentation donnée au début de la question, on peut facilement recoder une image de 4x4 facilement.  
![Image 0](/RenduImages/Image0_Rendu.png) 

### Question 2:  
Pour efficacement arriver à l'image demandée dans cette question, on remarque que le fond est majoritairement rouge, ce qui nous permet alors de faciliter la construction en encodant tout les pixels avec 00 00 FF pour afficher une couleur rouge. Suite à cela, on ajoute alors les autres couleurs par dessus. Pour trouver facilement l'encodage des couleurs, on peut utiliser ctrl + F pour rechercher le nom de la couleur voulue, au lieu de la rechercher parmis les centaines de couleurs listées. Une fois avoir changer les 6 pixels qui ne sont pas rouges, on obtient alors l'image suivante:  
![Image Test](/RenduImages/Imagetest_Rendu.png) 

### Question 3:  
Pour répondre aux questions posées dans la question A.3, on utiliseras la documentation disponible via le lien [suivant](https://www.apprendre-en-ligne.net/info/images/formatbmp.pdf)  

- L'image 1 possède alors un point de 102 bits.
- Pour trouver le nombre de bits par pixel, on lit l'adresse 0x1C sur 2 octets. Les deux images utilisent 18 biarts par pixels, c'est à dire que chaque couleur primaire du codage RVB peut être parmis 256 possibilitées.
- Pour l'image 1, l'adresse 0x22 nous informe que la taille des données pixels est de 48 bits, codés par l'hexadécimal 30. Cette réponse peut aussi se retrouver par le calcul hauteur X largeur X nombre d'octets par pixel, soit 4x4x3= 48. Cette donnée n'est par ailleurs par disponible sur l'image 0.
- Pour définir si une compression est utilisé, il faut lire l'adresse 0x1E et regarder si la valeur est différente de 0. Pour l'image 1, on retrouve effectivement que cette valeur est nulle, ce qui signifie qu'aucune compression est utilisée.
- Enfin, l'encodage des pixels reste le même, on retrouve toujours le même ensemble de valeurs. Ils sont toujours codés en RVB, avec un octet couleur.
  
### Question 4:  
- Comme dit précédemment, c'est l'adresse 0x1C qui encode le nombre de bits pixel. Pour l'image 2, on peut trouver que chaque bit est encodé par un unique bit, alors que les images précédentes avait pour valeur 48 bits!
- La taille des données pixels (lisible à l'adresse 0x22) est de 16 bits, soit trois fois moins que la taille des autres images.
- L'adresse 0x1E ayant pour valeur 0, on peut en conclure que l'image n'utilise pas de compression
- Comment sont codées les couleurs de la palette.  
Pour commencer, les couleurs de la palette sont définis après le bitmap info holder, et le nombre de couleurs dans la palette peut se trouver à l'adresse 0x2E. Dans la zone de définition des couleurs, celle-ci sont codées en RVBA (Rouge Vert Bleu Alpha) avec A l'indice de transparence de la couleur, chaque couleur est donc codée sur 32 bits.  
L'encodage des pixels seras détaillé ci-dessous
- Comme dit au-dessus, à l'aide de l'adresse 0x2E, on peut trouver que l'image 2 possède 2 couleurs qui sont le rouge et le blanc
- Pour ce qui est de l'encodage des pixels eux-mêmes, pour associer un pixel avec une couleur de la palette, il suffit d'appeler le numéro de palette sachant qu'elle à pour index 0. C'est à dire que pour la seconde couleur que nous avons codés, il suffit de mettre la valeur du bit à 1. Pour cette image, par le fait qu'elle ai seulement deux couleurs, chaque couleur est défini sur 1 bit, ce qui nous permet alors d'encoder les pixels via le binaire.
- Pour changer tout les pixels rouge en pixels bleu, il suffit de modifier le code de la couleur rouge pour qu'elle code du bleu. Pour cela, on modifie alors l'adresse 0x36 et on obtient le code et l'image ci-dessous:  
![Code de l'image bleue](/RenduImages/ImageBleue_Code.png)  
![Image bleue](/RenduImages/ImageBleue_Rendu.png)  
- Pour inverser les damiers de l'image bleue, il y a deux possiblités. Soit on inverse le codage des couleurs dans la palette elle même, soit on change le codage des pixels. La possibilité 1 est certainement la meilleure, surtout à grande échelle, par le fait qu'il faille uniquement changer 8 octets alors qu'il faudrais en modifier un nombre qui tend vers l'infceini plus l'image est grande.  
![Image bleue inverse](/RenduImages/ImageBleueInverse_Rendu.png)  
- Comme dit précédemment, utilisé le binaire est bien plus intuitif pour codé des images avec une palette de deux couleurs, en voilà la raison:  
![Code de l'image 3](/RenduImages/Image3_Code.png)  
![Image 3](/RenduImages/Image3_Rendu.png)  
Il suffit alors de mettre un 0 pour un pixel rouge, et un 1 pour un pixel blanc!
- En lisant l'adresse 0x2E de l'image exemple index, on peut lire qu'elle possède 16 couleurs différentes. Chaque pixel va donc être codé sur un octet (16 = 2⁴, donc il faut 4 prévoir 4 bits pour appeler les couleurs de la palette)
- Le blanc étant la couleur dominante dans l'image, elle se retrouve alors majoritairement dans le codage de celle-ci. On peut retrouver alors un grand nombre de C qui se repète. On peut alors déduire que ce C est la couleur blanche qui est majoritaire dans l'image. C étant égale à 12, la couleur blanche est la 13ème à être codée dans la palette de couleur. La couleur majoritaire est donc codée à l'adresse 0x66!
- Pour trouver où commence le tableau de pixel, il suffit de lire l'adresse 0x0A où on peuttrouver comme valeur 76. Ce 76 signifie que l'adresse 0x76 est le début de la zone de définition des pixels.
- En changeant quelque pixels de l'adresse 0x76 à 0x7A de C à 0, on peut remarquer que le coin inférieur gauche de l'image a effectivement été affecté de manière suivante:  
![Coin inférieur droit zoomer de l'image à l'aide de GIMP](/RenduImages/ExtraitGimp.png)  
- En diminuant le nombre de couleurs dans l'image exemple index, on obtient l'image exemple index 2, qui possède alors un nombre de couleur plus faible. Cette seconde version possède toujours 16 couleurs selon l'adresse 0x2E, et c'est par le fait qu'on retrouve en effet 16 couleurs dans la palette, mais qu'une majorité soit désormais égale à 00 00 00 00.  
D'un point de vu viseul, on obtient alors l'image ci-contre:  
![Image exemple index, mais avec moins de couleurs](/RenduImages/ImageIndex2_Rendu.png)  
  
### Question 5:  
Rappelant que la hauteur de l'image est défini à l'adresse 0x16, est que l'image 3 possède une hauteur de 00 00 00 04, pour trouver l'inverse on utilise l'encodage C2. FF FF FF FF représentant -1, FC FF FF FF est alors égal à -4! On obtient alors l'image suivante où l'ordre des lignes est inversé, c'est à dire que l'encodage ce fait du haut vers le bas:  
![Image 3 inversé](/RenduImages/Image3Reverse_Rendu.png)  
De la même façon, on peut retourner le logo de l'iut pour obtenir l'image suivante  
![Image exemple inversé](/RenduImages/ImageExempleReverse_Rendu.png) 
  
### Question 6:  
Suite à l'application de la conversion RLE, l'image 4 possède un poid de 1120 octets. Ce poid s'explique par le fait que la compression RLE créer une palette de 256 couleurs, même si l'image en utilise que deux.  
La zone de définition des pixels se retrouve à l'adresse 0x0A où on peut trouver l'adresse 0x0436.  
Explication de l'encodage des pixels:  
- La compression RLE est intuitive et se base sur le codage par index de couleur, avec pour différence le fait qu'on ajoute le nombre de pixels conséquent qui auront cette couleur. C'est à dire qu'une ligne de pixel rouge-rouge-blanc-rouge seras codé 02 00 (2x rouge) 01 01 (1x blanc) 01 00 (1x rouge).  
- De plus, on retrouve des 00 00 et 00 01 dans le code hexadécimal du codage des pixels. 00 00 signifie que c'est la fin de la ligne, et 00 01 la fin de l'image.  

### Question 7:  
L'image 5 pèse 1102 octet, ce qui est plus petit que l'image 4. Ceci s'explique par le fait que l'image 5 possède des répétitions de pixels alors que l'image 4 n'en possède pas, ce qui rend la compression RLE plus efficace.  
En différence au codage de l'image 4, on trouve le codage 04 00 (4 rouge) 04 01 (4 blanc) 04 00 (4 rouge) qui est là, source de la baisse du poid de l'image.  

### Question 8:  

### Question 9:  

### Question 10:  
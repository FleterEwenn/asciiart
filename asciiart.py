from PIL import Image
import random

# demande du chemin absolu de l'image à l'utilisateur pour l'ouvrir avec pillow
chemin = input("Entrez le chemin de l'image ")
image2 = Image.open(chemin)

# création de la chaîne de caractere pour le niveau de gris du plus clair au plus sombre
caracteres = '@&#]/?!:;-. '

# convertion de l'image en niveaux de gris
image = image2.convert('L')

# affiche l'image
image2.show()

# recupére la largeur et la hauteur de l'image
largeur, hauteur = image.size

# crée une boucle qui traite ligne par ligne, ici y est l'ordonnée
for y in range(hauteur):
	# initialise la boucle contenant les caractères de chaque ligne
	ascii = ''

	# crée une boucle qui traite colonne par colonne, ici x est l'abscisse
	# donc le couple (x,y) correspond au coordonnées d'un pixel de l'image
	for x in range(largeur):
		# on récupère la couleur en niveau de gris d'un pixel de coordonnées x,y
		# la valeur est comprise entre 0 et 255 :  noir=0 blanc=255
		px = image.getpixel((x, y))
		
		# proportinalité pour obtenir le niveau de gris en caractere en fonction du nombre de caracteres
		nv_gris = px*len(caracteres)/255
		# Le caractere est ajouter avce un espace pour compenser la différence entre la hauteur et la largeur
		ascii += ' ' + nv_gris

	# affiche la ligne de caractere correspondante a la ligne traitée de l'image
	print(ascii)

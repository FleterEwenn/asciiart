from PIL import Image
import random

# demande du chemin absolu de l'image à l'utilisateur pour l'ouvrir avec pillow
chemin = input("Entrez le chemin de l'image ")
image2 = Image.open(chemin)

# convertion de l'image en niveaux de gris
image = image2.convert('L')

# affiche l'image
image2.show()

# recupére la largeur et la hauteur de l'image
largeur, hauteur = image.size

# crée une boucle qui traite ligne par ligne, ici y est l'ordonnée
for y in range(hauteur):
	# initialise la boucle contenant les caractères de chaque ligne
	ascii_list = []

	# crée une boucle qui traite colonne par colonne, ici x est l'abscisse
	# donc le couple (x,y) correspond au coordonnées d'un pixel de l'image
	for x in range(largeur):
		# on récupère la couleur en niveau de gris d'un pixel de coordonnées x,y
		px = image.getpixel((x, y))
		# traitement de la valeur de la couleur(px) comprise entre 0 et 255 :  noir=0 blanc=255
		if px < 5:
			ascii_list += [' ']
		elif px < 50:
			ascii_list += ['.']
		elif px < 75:
			ascii_list += [';']
		elif px < 150:
			ascii_list += list(random.choice(['[', ']']))
		elif px < 200:
			ascii_list += ['&']
		elif px < 225:
			ascii_list += ['@']
		else:
			ascii_list += ['#']

	# rassemble les éléments de la liste, les caractères de la ligne traitée, en une variable pour les afficher
	# un espace est ajouter a chaque element pour compenser la différence entre la hauteur et la largeur d'un caractère
	ascii = " ".join(ascii_list)
	print(ascii)

from PIL import Image
import random

chemin = input("Entrez le chemin de l'image ")
image2 = Image.open(chemin)
image = image2.convert('L')
image2.show()
largeur, hauteur = image.size
ascii_list = []
for y in range(hauteur):
	ascii_list = []
	for x in range(largeur):
		px = image.getpixel((x, y))
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
	ascii = " ".join(ascii_list)
	print(ascii)

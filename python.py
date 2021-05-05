import time
start = time.time()
# Création d'un labyrinthe

labyrinthe = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1],
              [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1],
              [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1],
              [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1],
              [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
              [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
              [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1],
              [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1],
              [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
              [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

nbLignes = len(labyrinthe) # Calcul du nombre de ligne du labyrinthe
nbColonnes = len(labyrinthe[0]) # Calcul du nombre de colonne du labyrinthe

def affiche_etat(ligne,colonne):
	""" affiche les passages et la sortie du robot """
	if labyrinthe[ligne][colonne] == 0: # Si le robot passe sur une case vide
		print('Passage aux coordonnées {},{}.'.format(ligne,colonne)) # Affiche les coordonnées de la case
	elif labyrinthe[ligne][colonne] == 2: # Lorsque le robot atteint la sortie
		print('Sortie aux coordonnées {},{}.'.format(ligne,colonne)) # Affiche les coordonnées de la sortie



def affiche_labyrinthe(labyrinthe):
	""" affiche le labyrinthe """
	for i in range(nbColonnes) : print('_', end = ' ') # Création bordure
	print() # Retour à la ligne
	for l,ligne in enumerate(labyrinthe) : # Parcours chaque ligne du labyrinthe
		if l == 0 : print('|', end = ' ') # Création bordure entrée
		else : print('|', end = ' ') # Création bordure
		for e, element in enumerate(ligne) : # Parcours chaque case du labyrinthe
			if element == 1 : print('X', end=" ") # Si la case est un mur, afficher 'X'
			elif element == 0 or element == 2 : print(' ', end=" ") # Si la case est vide, afficher un blanc
			elif element == 3 : print( '\u2588', end = ' ') # Si la case est visitée, afficher full block
			else : print('\u2588', end=" ") # Lorsque la sortie est visitée (la case sera égale à 5), afficher full block
			if e == nbColonnes-1 : # Parcours les cases du bord
				if element != 2 and element !=5 : print('|', end = ' ') # Création bordure
		print() # Retour à la ligne
	for i in range(nbColonnes) : print('\u0305', end = '  ') # Création bordure

def deplacement(ligne,colonne, trace ):
    """ Parcours du labyrinthe par le robot """
    if trace : affiche_etat(ligne,colonne) # Execute la fonction affiche_etat lorsque le robot se déplace

    if   labyrinthe[ligne][colonne] == 2 : # Si le robot atteint la sortie
        labyrinthe[ligne][colonne] += 3 # On rajoute 3 à la case (2+3 = 5, donc la case prend la valeur 5)
        return True # Fin du programme, sortie trouvée, on renvoie True
    elif labyrinthe[ligne][colonne] == 1 :
        return False # Lorsque la case est un mur, renvoie False
    elif labyrinthe[ligne][colonne] == 3 :
        return False # Lorsque la case est déjà visitée, renvoie False
    else :
        labyrinthe[ligne][colonne] = 3 # Sinon (si le robot est sur une nouvelle case vide) la case devient une case visitée (égal à 3)

	# à partir d'une case, on essaie les quatre directions, la première menant jusqu'à la sortie est retenue
    if ligne < nbLignes-1 and deplacement(ligne+1, colonne, trace) :
        return True # Déplacement vers la droite
    if colonne > 0 and deplacement(ligne, colonne-1, trace)  :
        return True # Déplacement vers le bas
    if ligne > 0 and deplacement(ligne-1, colonne, trace) :
        return True # Déplacement vers la gauche
    if colonne < nbColonnes-1 and deplacement(ligne, colonne+1, trace) :
        return True # Déplacement vers le haut
    return False # Si le robot ne peut aller nul part (cul de sac/boucle) renvoie False

print("Labyrinthe : ")
affiche_labyrinthe(labyrinthe) # Affichage du labyrinthe graphiquement en format textuel
print("Parcours du labyrinthe :\n ")
deplacement(0, 1, trace = True) # Départ du robot en (0,1)
affiche_labyrinthe(labyrinthe) # Réaffiche le labyrinthe mais cette fois parcouru
print(time.time() - start)

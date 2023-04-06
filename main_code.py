"""
Created on 16/03/2023
@author: Bleuenn Even, Anaïs Febvre, Shaun Ferrand, Oliwier Ostasz
"""
import matplotlib.pyplot as plt
import random

def echange_coords(grille):
    '''
    Tant qu'un changement valable n'a pas été effectué:
    demande à l'utlisiateur un jeu de coordonnées
    vérifie s'il existe des bonbons dans les quatre directions
    propose à l'utilisateur de choisir une des directions possibles
    si ce changement créé une nouvelle combinaison, on échange les bonbons
    si ce changement ne crée pas de nouvelle combinaison, on redemande un nouveau jeu de coordonnées qui marche
    renvoie la grille avec les bonbons échangés.
    '''
    compteur_coups = 0
    switch = False
    while not switch:

        gauche,droite,haut,bas = True
        
        i = input("Entrer la ligne du bonbon séléctionné : ")
        j = input("Entrer la colonne du bonbon séléctionné : ")
        
        if i == 0:
            haut = False
        if i == len(grille)-1:
            bas = False
        if j == 0:
            gauche = False
        if j == len(grille)-1:
            droite = False
            
        directions = [gauche,droite,haut,bas]
        
        directions_possibles = []
        for i in range(len(directions)):
            if directions[i] == True:
                directions_possibles.append(directions[i])
                
        choix_directions = input(f"Veuillez choisir parmi les directions suivantes: {directions_possibles}: ")
        
        if choix_directions == "gauche":
            grille[i][j],grille[i][j-1] = grille[i][j-1],grille[i][j]
            if recherche_combinaison_grille(grille) == []:
                grille[i][j],grille[i][j-1] = grille[i][j-1],grille[i][j]
                print("Veuillez jouer un coup valable qui créé une combinaison")
            else :
                switch = True
                compteur_coups += 1

                
        if choix_directions == "droite":
            grille[i][j],grille[i][j+1] = grille[i][j+1],grille[i][j]
            if recherche_combinaison_grille(grille) == []:
                grille[i][j],grille[i][j+1] = grille[i][j+1],grille[i][j]
                print("Veuillez jouer un coup valable qui créé une combinaison")
            else :
                switch = True
                compteur_coups += 1

                
        if choix_directions == "haut":
            grille[i][j],grille[i-1][j] = grille[i-1][j],grille[i][j]
            if recherche_combinaison_grille(grille) == []:
                grille[i][j],grille[i-1][j] = grille[i-1][j],grille[i][j]
                print("Veuillez jouer un coup valable qui créé une combinaison")
            else :
                switch = True
                compteur_coups += 1

                
        if choix_directions == "bas":
            grille[i][j],grille[i+1][j] = grille[i+1][j],grille[i][j]
            if recherche_combinaison_grille(grille) == []:
                grille[i][j],grille[i+1][j] = grille[i+1][j],grille[i][j]
                print("Veuillez jouer un coup valable qui créé une combinaison")
            else :
                switch = True
                compteur_coups += 1

    return grille,compteur_coups


def detecte_coordonnees_combinaison(grille,i,j):
    """Renvoie une liste contenant les coordonnées de tout
    les bonbons appartenant à la combinaison du bonbon (i,j)
    """
    etat_cellule=grille[i][j]
    
    liste_combi=[[i,j]]
    jbis=j
    ibis=i
        
    while  j+1<=len(grille)-1 and grille[i][j+1]==etat_cellule:
        liste_combi.append([i,j+1])
        j+=1             
    j=jbis    
    
    while j-1>=0 and grille[i][j-1]==etat_cellule:
            
        liste_combi.append([i,j-1])
        j-=1        
    if len(liste_combi)<3:
            liste_combi=[]
    j=jbis     
    while i+1 <=(len(grille)-1) and grille[i+1][j]==etat_cellule:
        liste_combi.append([i+1,j])
        i+=1    
    i=ibis   
    while i-1>=0 and grille[i-1][j]==etat_cellule:            
        liste_combi.append([i-1,j])
        i-=1
    if len(liste_combi)<3:
        liste_combi=[]            
    return(liste_combi)
        

    
def recherche_combinaison_grille(grille):
    '''parcourt toute la grille et trouve toutes les combinaisons pour les mettre dans une liste (ttes_combis)
    parcourt ttes_combis et supprime toutes les listes dupliquées pour avoir une seule liste par combinaison dans la grille
    renvoie la liste de ttes_combis'''
    ttes_combis = []
    for i in range (len(grille)):
        for j in range(len(grille)):
            ttes_combis.append(detecte_coordonnees_combinaison(grille,i,j))
    parcours = 0
    while parcours <= len(ttes_combis):
        for n in range(parcours+1,len(ttes_combis)):
            if ttes_combis[parcours] == ttes_combis[n]:
                del ttes_combis[n]
        parcours += 1
    return ttes_combis


def gravite(grid):
    """
    Renvoie une liste a laquelle elle a appliquée la gravité sur toutes les cases
    
    Parameters : Grille initiale
    Output : Grille avec gravitée appliquée
    """ 
    for l in range(len(grid),0,-1):
        for c in range(len(grid)):
            if grid[l][c] == 0:
                grid[l][c] = grid[l-1][c]
                grid[l-1][c] = 0
    return(grid)


def elimination(grille,liste_combi,score):
    """
    fonction qui remplace par des zéros les valeurs dans les cases dont les 
    coordonnées apparaissent dans liste_combi
    rajoute à la variable score le nombre de valeurs modifiées
    
    Parameters
    ----------
    grille : tableau 2D
    liste_combi : tableau 2D
    score : int
    Returns
    -------
    grille, score (modifiés)
    """
    for i in range(len(liste_combi)):
        grille[liste_combi[i][0]][liste_combi[i][1]] = 0
        score += 10
    return grille, score


def regeneration(grille,score):
    """
    fonction qui parcourt la grille et remplace toutes les cases vides par un 
    bonbon d'une nouvelle couleur aléatoire, c'est à dire que les cases de 
    valeur 0 prennent une valeur aléatoire de 1 à 4
    si de nouvelles combinaisons créées, supprime les bonbons et ajoute points 
    au score, puis refait tomber nouveaux bonbons avec gravité, et en génère 
    de nouveaux jusqu'à ce qu'il n'y ait plus de combinaison
    Parameters
    ----------
    grille : liste 2D
    score : int
    Returns
    -------
    grille, score
    """
    liste_combi = [-1]
    while liste_combi != []:
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                if grille[i][j]==0:
                    grille[i][j]= random.randint(1,4)
        liste_combi = recherche_combinaison_grille(grille)
        grille, score = elimination(grille,liste_combi,score)
        grille = gravite(grille)
    return grille, score


def gen_grille_init(size):
    """
    fonction qui génère une liste de listes (grille) dont les valeurs
    sont des nombres de 1 à 4, et recherche les combinaisons qui 
    apparaissent dans cette grille. Tant qu'il existe des combinaisons,
    remplace les valeurs par des nouvelles aléatoires jusqu'à obtenir
    une grille de jeu sans aucune combinaison
    
    Parameters
    ----------
    size : int
        nombre de lignes et de colonnes de la grille voulue
        
    Returns
    grille (liste de listes)
    """
    grille = []
    score = 0
    for i in range(size):
        ligne = []
        for j in range(size):
            ligne.append(random.randint(1,4))
        grille.append(ligne)
    liste_combi = recherche_combinaison_grille(grille)
    while liste_combi != []:
        grille, score = elimination(grille,liste_combi,0)
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                if grille[i][j]==0:
                    grille[i][j]= random.randint(1,4)
        liste_combi = recherche_combinaison_grille(grille)
    return grille

def verification_deadlock(grille):
    """Cette fonction vérifie qu'il existe encore une possibilité de créer une combinaison en échangeant deux bonbons
    Si ce n'est pas le cas, le jeu est bloqué, renvoie false
    """
    switch_possible = False
    grille_verif = grille.copy()
    line = 0
    column = 0
    while not switch_possible or (line == len(grille)-1 and column == len(grille)-1):
        #tant qu'un switch possible n'est pas trouvé ou qu'on a exploré toute la grille
        for i in range(len(grille)):
            line += 1
            for j in range(len(grille)):
                column += 1
                
                #verifie à gauche
                if i != 0:
                    grille_verif[i][j],grille_verif[i][j-1] = grille_verif[i][j-1],grille_verif[i][j]
                    if recherche_combinaison_grille(grille_verif) != []:
                        switch_possible == True
                    else:
                        grille_verif[i][j],grille_verif[i][j-1] = grille_verif[i][j-1],grille_verif[i][j]
                    
                #verifie à droite
                if i != len(grille)-1:
                    grille_verif[i][j],grille_verif[i][j+1] = grille_verif[i][j+1],grille_verif[i][j]
                    if recherche_combinaison_grille(grille_verif) != []:
                        switch_possible == True
                    else:
                           grille_verif[i][j],grille_verif[i][j+1] = grille_verif[i][j+1],grille_verif[i][j]
                    
                    
                #verifie en haut
                if j != 0:
                    grille_verif[i][j],grille_verif[i-1][j] = grille_verif[i-1][j],grille_verif[i][j]
                    if recherche_combinaison_grille(grille_verif) != []:
                        switch_possible == True
                    else:
                           grille_verif[i][j],grille_verif[i-1][j] = grille_verif[i-1][j],grille_verif[i][j]
                        
                #verifie en bas
                if j != len(grille)-1:
                    grille_verif[i][j],grille_verif[i+1][j] = grille_verif[i+1][j],grille_verif[i][j]
                    if recherche_combinaison_grille(grille_verif) != []:
                        switch_possible == True
                    else:
                           grille_verif[i][j],grille_verif[i+1][j] = grille_verif[i+1][j],grille_verif[i][j]

    return switch_possible


def affichage_grille(grille, nb_type_bonbons):
    """
    Affiche la grille de jeu "grille" contenant au maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons-1, cmap='jet')
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)
    
    

    
    
 # PROGRAMME EXECUTIF DU JEU #
    
size = 8
grille = gen_grille_init(size)
score=0
score_max = 300
compteur_coups=0
nb_coups_max = 30
while score < score_max and compteur_coups < nb_coups_max and verification_deadlock(grille):
    affichage_grille(grille, 4)
    grille,compteur_coups = echange_coords(grille)
    print(f"Il vous reste {compteur_coups} coups sur {nb_coups_max}")
    liste_combis = recherche_combinaison_grille(grille)
    while liste_combis != []:
        grille,score = elimination(grille,liste_combis,score)
        grille = regeneration(grille)	
        liste_combis = recherche_combinaison_grille(grille)
        affichage_grille(grille)
if score > score_max :
    print(f"Félicitations vous avez gagné. Votre score est de {score}")
if compteur_coups >= nb_coups_max :
    print(f"Vous n'avez pas réussi à atteindre l'objectif? Votre score final était de {score}")
if not verification_deadlock(grille):
    print(f"Plus aucune combinaison possible! Votre score final était de {score}")

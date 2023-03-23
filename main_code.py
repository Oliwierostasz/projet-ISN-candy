"""
Created on 16/03/2023
@author: Bleuenn Even, Anaïs Febvre, Shaun Ferrand, Oliwier Ostasz
"""
import random

def echange_coords(grille):
    switch = False
    while not switch:

        gauche,droite,haut,bas = True
        
        i = input("Entrer la ligne du bonbon séléctionné : ")
        j = input("Entrer la colonne du bonbon séléctionné : ")
        
        if i == 0:
            haut = False
        if i == len(grille):
            bas = False
        if j == 0:
            gauche = False
        if j == len(grille):
            droite = False
            
        directions = [gauche,droite,haut,bas]
        
        directions_possibles = []
        for i in len(directions):
            if directions[i] == True:
                directions_possibles.append(directions[i])
                
        choix_directions = input(f"Veuillez choisir parmi les directions suivantes: {directions_possibles}: ")
        
        if choix_directions == "gauche":
            grille[i][j],grille[i][j-1] = grille[i][j-1],grille[i][j]
            if detecte_combinaison_grille(grille) == []:
                grille[i][j],grille[i][j-1] = grille[i][j-1],grille[i][j]
                print("Veuillez fournir un échange qui marche")
            else :
                switch = True
                
        if choix_directions == "droite":
            grille[i][j],grille[i][j+1] = grille[i][j+1],grille[i][j]
            if detecte_combinaison_grille(grille) == []:
                grille[i][j],grille[i][j+1] = grille[i][j+1],grille[i][j]
                print("Veuillez fournir un échange qui marche")
            else :
                switch = True
                
        if choix_directions == "haut":
            grille[i][j],grille[i-1][j] = grille[i-1][j],grille[i][j]
            if detecte_combinaison_grille(grille) == []:
                grille[i][j],grille[i-1][j] = grille[i-1][j],grille[i][j]
                print("Veuillez fournir un échange qui marche")
            else :
                switch = True
                
        if choix_directions == "bas":
            grille[i][j],grille[i+1][j] = grille[i+1][j],grille[i][j]
            if detecte_combinaison_grille(grille) == []:
                grille[i][j],grille[i+1][j] = grille[i+1][j],grille[i][j]
                print("Veuillez fournir un échange qui marche")
            else :
                switch = True

    return grille


def gravité(grid):
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
        score += 1
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
   

"""
Created on 16/03/2023
@author: Bleuenn Even, Anaïs Febvre, Shaun Ferrand, Oliwier Ostasz
"""
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

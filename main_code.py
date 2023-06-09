"""
Created on 16/03/2023
@author: Bleuenn Even, Anaïs Febvre, Shaun Ferrand, Oliwier Ostasz
"""
import matplotlib.pyplot as plt
import random

def switch_directions(grille,i,j,choix_directions,compteur_coups):
    '''Automatise les changements de bonbons en fonction de la direction
    a besoin de la direction, des coordonnées du bonbon visé, de la grille et du compteur de coups
    effectue le changement;
    s'il n'est pas valable, switch = False, le compteur ne varie pas, la grille revient à son état d'origine
    S'il est valable, la grille est modifiée, le compteur de coups augmente, switch = true, on sort de la boucle
    renvoie: le booléen switch, le compteur, la grille (modifiée ou non)
    '''
    switch_direction = False
    if choix_directions == "haut":
        a = -1
        b = 0
    if choix_directions == "bas":
        a = 1
        b = 0
    if choix_directions == "droite":
        a = 0
        b = 1
    if choix_directions == "gauche":
        a = 0
        b = -1
    grille[i][j],grille[i+a][j+b]=grille[i+a][j+b],grille[i][j]
    if detecte_coordonnees_combinaison(grille,i,j) == [] and detecte_coordonnees_combinaison(grille,i+a,j+b) == []:
        grille[i][j],grille[i+a][j+b]=grille[i+a][j+b],grille[i][j]
        print("Veuillez jouer un coup valable qui créé une combinaison")
    else :
        switch_direction = True
        compteur_coups += 1
    return switch_direction,compteur_coups,grille

def echange_coords(grille,compteur_coups):
    '''
    Tant qu'un changement valable n'a pas été effectué:
    demande à l'utlisiateur un jeu de coordonnées
    vérifie s'il existe des bonbons dans les quatre directions
    propose à l'utilisateur de choisir une des directions possibles
    si ce changement créé une nouvelle combinaison, on échange les bonbons
    si ce changement ne crée pas de nouvelle combinaison, on redemande un nouveau jeu de coordonnées qui marche
    renvoie la grille avec les bonbons échangés.
    '''
    switch = False
    while not switch:

        i = int(input("Entrer la ligne du bonbon séléctionné : "))
        j = int(input("Entrer la colonne du bonbon séléctionné : "))
    
        directions_possibles = valide_directions(i,j,grille)
                
        choix_directions = input("Veuillez choisir une direction parmi: " + ", ".join(directions_possibles) + "\n")
        choix_directions = choix_directions.lower()    
    
        if choix_directions not in directions_possibles:
            print("ce n'est pas une direction valable")
        else:
            switch,compteur_coups,grille = switch_directions(grille,i,j,choix_directions,compteur_coups)

    return grille,compteur_coups


def scotch(grille):
    """à patir d'une grille donnée, renvoie cette même grille entouré d'un scotch(de 0)
    """
    grille_scotch=[]
    ligne=[]
    for i in range (len(grille)+2):
        ligne.append(0)
    grille_scotch.append(ligne)
    ligne_s=[]
    for i in range (len(grille)):
        ligne_s.append(0)
        for j in range(len(grille)):
            ligne_s.append(grille[i][j])
        ligne_s.append(0)
        grille_scotch.append(ligne_s)
        ligne_s=[]
    grille_scotch.append(ligne)
    return (grille_scotch)    


def detecte_coordonnees_combinaison(grille,i,j):
    """Renvoie une liste contenant les coordonnées de tout
    les bonbons appartenant à la combinaison du bonbon (i,j)
    """
    ##on utilise i et j pour la grille sans scotch et ibis et jbis sont les meme bonbon mais pour la grille avec scotch
    ##ajout du scotch à la grille donné 
    grille_combi=scotch(grille)
    ##comme grille entourée du scotch, on rajoute +1 au coordonnée du bonbon que l'on appelera ibis et jbis 
    ibis=i+1
    jbis=j+1
    etat_bonbon=grille_combi[ibis][jbis] ##correspond au nombre que porte la case 
    liste_combi=[] ##liste combinaison locale  
    liste_combi_f=[]## liste combinaison final
    
    while ibis>0 and grille_combi[ibis-1][jbis]==etat_bonbon: ##on monte d'abord 
        ibis-=1
        liste_combi.append([ibis-1,jbis-1])
    ibis=i+1##on réinitialise ibis a la position du bonbon 
    
    while ibis<(len(grille_combi)-1) and grille_combi[ibis+1][jbis]==etat_bonbon: ##on descend 
        ibis+=1
        liste_combi.append([ibis-1,jbis-1])
    ibis=i+1 ##on réinitialise ibis à la position du bonbon 
    if len(liste_combi)<2:
        liste_combi=[]
    else:liste_combi_f+=liste_combi
    
    liste_combi=[]  ##on réinitialise la liste de combinaison (on s'occupe maitenant de la ligne) 
    while jbis>0 and grille_combi[ibis][jbis-1]==etat_bonbon:## a gauche
        jbis-=1
        liste_combi.append([ibis-1,jbis-1])
    
    jbis=j+1 ##on réinitialise jbis à la position du bonbon 
    
    while jbis<(len(grille_combi)-1) and grille_combi[ibis][jbis+1]==etat_bonbon: ##à droite
        jbis+=1
        liste_combi.append([ibis-1,jbis-1])
    jbis=i+1 ##on réinitialise jbis à la position du bonbon 
    if len(liste_combi)<2:
        liste_combi=[]
    else:liste_combi_f+=liste_combi
    
    
    if len(liste_combi_f)>=2:
        liste_combi_f.append([i,j])
        
    return(liste_combi_f)
        

def test_detecte_coordonnees_combinaison():
    """
    Teste la fonction detecte_coordonnees_combinaison(grille, i, j).
    Pour chaque cas de test, affiche True si le test passe, False sinon
    Pour éviter toute confusion par rapport à l'ordre dans lequel les combinaisons sont placées dans
    la liste renvoyée par detecte_coordonnees_combinaison, on préfère vérifier que chaque coordonnée 
    de bonbon impliquée dans la combinaison attendue est présente dans cette liste et qu'elle contient 
    le bon nombre de valeurs
    """
    # Test1: bonbon situé sur la colonne la plus à gauche, sur la 2e ligne, impliqué dans combinaison de 3 bonbons verticalement et une de 4 horizontalement
    grille = [[1,2,3,4],[1,1,1,1],[1,3,4,4],[2,2,3,1]]
    i = 1
    j = 0
    liste_combis1 = detecte_coordonnees_combinaison(grille,i,j)
    print(([i,j] and [0,0] and [2,0] and [1,1] and [1,2] and [1,3]) in liste_combis1 and len(liste_combis1)==6)
          
    # Test2 : bonbon situé à aucune ligne ou colonne extrême, impliqué dans une combinaison de 4 bonbons horizontalement et une de 4 verticalement    
    grille=[[1,2,3,4],[2,2,2,2],[1,2,3,4],[1,2,3,4]]
    i = 1
    j = 1
    liste_combis2 = detecte_coordonnees_combinaison(grille,i,j)
    print(([i,j] and [0,1] and [2,1] and [3,1] and [1,0] and [1,2] and [1,3]) in liste_combis2 and len(liste_combis2)==7)
    
    #Test3 : bonbon situé dans le coin inférieur droit de la grille, impliqué dans une combinaison de 3 bonbons verticale
    grille = [[1,2,3,4,3],[2,1,3,2,3],[1,2,2,3,4],[3,1,2,4,4],[1,2,4,3,4]]
    i = 4
    j = 4
    liste_combis3 = detecte_coordonnees_combinaison(grille,i,j)
    print(([i,j] and [3,4] and [2,4]) in liste_combis3 and len(liste_combis3)==3)
    
    #Test4 : bonbon situé au milieu d'une grille 3x3, impliqué dans aucune combinaison
    grille = [[1,2,3],[3,4,2],[1,3,1]]
    i = 1
    j = 1
    liste_combis4 = detecte_coordonnees_combinaison(grille,i,j)
    print(len(liste_combis4)==0)
    
    
def recherche_combinaison_grille(grille):
    """
    fonction qui parcourt toute la grille et trouve toutes les combinaisons pour les mettre dans une liste (ttes_combis), puis
    parcourt ttes_combis et crée une liste où sont supprimées toutes les coordonnées dupliquées pour que chacune n'apparaisse qu'une fois

    Parameters
    ----------
    grille : liste de listes (tableau 2D)
        la grille de jeu

    Returns
    -------
    combis_sans_doubles : liste de listes 
        liste contenant les coordonnées de tous les bonbons impliqués dans une combinaison dans la grille

    """
    '''
    renvoie la liste de listes combis_sans_doubles'''
    ttes_combis = []
    for i in range (len(grille)):
        for j in range(len(grille[i])):
            ttes_combis += (detecte_coordonnees_combinaison(grille,i,j))
    combis_sans_doubles = []
    for coord in ttes_combis :
        if coord not in combis_sans_doubles :
            combis_sans_doubles.append(coord)
    return combis_sans_doubles


def gravite(grille):
    """
    fonction qui applique sur la grille la "gravité", faisant descendre dans la grille les bonbons (cases de valeur non nulle) jusqu'à avoir toutes les
    cases vides (0) situées le plus haut possible sans aucun bonbon au dessus

    Parameters
    ----------
    grille : liste de listes
        la grille de jeu avec des cases vides et d'autres avec bonbons

    Returns
    -------
    g : grille sur laquelle la gravité a été appliquée

    """
    g = []
    for l in grille:
        g.append(l.copy())
    trie = False
    while not trie:
        trie = True
        for l in range(len(g)-1,0,-1):
            for c in range(len(g)):
                if g[l][c] == 0:
                    g[l][c] = g[l-1][c]
                    g[l-1][c] = 0
        for l2 in range(len(g)-1,0,-1):
            for c2 in range(len(g)):
                if g[l2-1][c2]!=0 and g[l2][c2]==0:
                      trie = False
    affichage_grille(g,4)                    
    return(g)


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
        x = liste_combi[i][0]
        y = liste_combi[i][1]
        if grille[x][y]!=0:
            grille[x][y] = 0
            score += 10
    return grille, score



def regeneration(grille,score):
    """
    fonction qui parcourt la grille et remplace toutes les cases vides par un 
    bonbon d'une nouvelle couleur aléatoire, c'est à dire que les cases de 
    valeur 0 prennent une valeur aléatoire de 1 à 4
    Quand des combinaisons sont créées, supprime les bonbons et ajoute points 
    au score, puis refait tomber nouveaux bonbons avec gravité, et en génère 
    de nouveaux jusqu'à ce qu'il n'y ait plus de combinaison déjà faite
    affiche la grille au fur et à mesure de sa modification
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
        affichage_grille(grille,4)
        liste_combi = recherche_combinaison_grille(grille)
        if liste_combi != []:
            grille, score = elimination(grille,liste_combi,score)
            affichage_grille(grille,4)
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

def valide_directions(i,j,grille):
    '''une fonction pour déterminer plus facilement dans quelle direction on peut faire des échanges
    renvoie une liste de chaines de caractères avec les directions valables'''
    
    directions_txt = ["gauche","droite","haut","bas"]
    gauche = True
    droite = True
    haut = True
    bas = True
    directions_bool = [gauche,droite,haut,bas]
    
  
    if j == 0:
        directions_bool[0] = False
    if j == len(grille)-1:
        directions_bool[1] = False
    if i == 0:
        directions_bool[2] = False
    if i == len(grille)-1:
        directions_bool[3] = False
        
    directions_possibles = []
    for k in range(len(directions_bool)):
        if directions_bool[k] == True:
            directions_possibles.append(directions_txt[k])
            
    return directions_possibles

def tests_combinaisons(i,j,a,b,grille,cpt_combis):
    '''Une fonction qui teste simplement si les échanges donnent des combinaisons
    prend comme input i et j les coordonnées du bonbon de base (on va faire parcourir tous les i et j)
    prend comme input a et b, deux variables qui dépendent de la fonction verif_deadlock et valide_direction et qui varient selon la direction voulue pour le changement
    renvoie le nombre de combinaisons trouvées
    '''
    grille[i][j],grille[i+a][j+b]=grille[i+a][j+b],grille[i][j]
    
    if detecte_coordonnees_combinaison(grille,i,j) == [] and detecte_coordonnees_combinaison(grille,i+a,j+b) == []:
        grille[i][j],grille[i+a][j+b]=grille[i+a][j+b],grille[i][j]
        
    else :
        cpt_combis += 1
        grille[i][j],grille[i+a][j+b]=grille[i+a][j+b],grille[i][j]
    
    return cpt_combis


def verification_deadlock(grille):
    cpt_combis = 0
    line = 0
    column = 0
    deadlock = True
    while column != len(grille)-1 and line != len(grille)-1:
        for i in range(len(grille)):
            line = i
            for j in range(len(grille)):
                column = j
            
                directions_possibles = valide_directions(i,j,grille)
                                
                for k in range(len(directions_possibles)):
                    direction_selectionnee = directions_possibles[k]
                    if direction_selectionnee == "haut":
                        a = -1
                        b = 0
                    if direction_selectionnee == "bas":
                        a = 1
                        b = 0
                    if direction_selectionnee == "droite":
                        a = 0
                        b = 1
                    if direction_selectionnee == "gauche":
                        a = 0
                        b = -1
                        
                    cpt_combis += tests_combinaisons(i,j,a,b,grille,cpt_combis)
        
    if cpt_combis != 0:
        deadlock = False
    if cpt_combis == 0:
        deadlock = True   
    
    return deadlock   


def affichage_grille(grille, nb_type_bonbons):
    """
    Affiche la grille de jeu "grille" contenant au maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons, cmap='jet')
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)
    
    

    
    
 # PROGRAMME EXECUTIF DU JEU #

size = 8
grille = gen_grille_init(size)
score=0
score_max = 2000
compteur_coups=0
nb_coups_max = 30
affichage_grille(grille, 4)
while score < score_max and compteur_coups < nb_coups_max and verification_deadlock(grille) == False:
    grille,compteur_coups = echange_coords(grille,compteur_coups)
    print(f"Il vous reste {nb_coups_max-compteur_coups} coups sur {nb_coups_max}")
    grille,score = regeneration(grille,score)
    print(f"Votre score est de {score}. Il vous manque {score_max-score} points pour atteindre l'objectif.")
if score >= score_max :
    print(f"Félicitations vous avez gagné. Votre score final est de {score}.")
if compteur_coups >= nb_coups_max :
    print(f"Vous n'avez pas réussi à atteindre l'objectif? Votre score final était de {score}")
if verification_deadlock(grille) == True:
    print(f"Vous avez atteint une grille irrésolvable. Votre score final était de {score}")


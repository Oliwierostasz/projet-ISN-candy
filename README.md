# projet-ISN-candy
Projet ISN Candy Crush 2023
Réalisé par Bleuenn Even, Anaïs Febvre, Shaun Ferrand, Oliwier Ostasz du groupe 101.

Vous retrouverez sous maincode, le code principal avec les fonctions utilisées accompagnées de leur docstring.
Vous retrouverez sous le rapport, le modèle de rapport demandé duement rempli et expliquant les fonctions avec une docstring et le code principal en plus d'expliquer la difficulté et les règles de notre code. Celui-ci est mis en page dans le .odt téléchargeable et ainsi que la version non mise en forme ci dessous : 

**Rapport du mini-projet Candy Crush**

I.  Quel niveau de difficulté avez-vous implémenté ?

Nous avons choisi d’imposer un nombre de coups maximum définissable dans le code ainsi un score à atteindre, le score pour une combinaison est de 30 points et le score à atteindre est de 2000 points. Ces données peuvent être changés pour ajuster la durée/difficulté du jeu.

II.  Décrivez les règles de votre jeu en quelques lignes

Le jeu se joue de la façon suivante : 
Le joueur lance le code, une partie se lance, une grille générée aléatoirement est générée. Le jeu demande alors au joueur la ligne et la colonne du bonbon qu’il souhaite déplacer. Ensuite le jeu demande dans quel sens (haut, bas, gauche ou droite) ce bonbon doit être bougé. Après avoir vérifié la validité du coup (combinaison de 3 bonbon créée) celui-ci vérifie les combinaisons créées et incrémente le compteur de points.
Ainsi, le principe du jeu est d’aligner 3 bonbons de même couleur pour obtenir des points et gagner la partie.

III.  Écrivez l’algorithme principal de votre jeu en français


def switch_directions(grille,i,j,choix_directions,compteur_coups):

    """
    Automatise les changements de bonbons en fonction de la direction
    a besoin de la direction, des coordonnées du bonbon visé, de la grille et du compteur de coups
    effectue le changement;
    s'il n'est pas valable, switch = False, le compteur ne varie pas, la grille revient à son état d'origine
    S'il est valable, la grille est modifiée, le compteur de coups augmente, switch = true, on sort de la boucle
    renvoie: le booléen switch, le compteur, la grille (modifiée ou non)
    """
def echange_coords(grille,compteur_coups):

    """
    Tant qu'un changement valable n'a pas été effectué:
    demande à l'utlisiateur un jeu de coordonnées
    vérifie s'il existe des bonbons dans les quatre directions
    propose à l'utilisateur de choisir une des directions possibles
    si ce changement créé une nouvelle combinaison, on échange les bonbons
    si ce changement ne crée pas de nouvelle combinaison, on redemande un nouveau jeu de coordonnées qui marche
    renvoie la grille avec les bonbons échangés.
    """
def scotch(grille):

    """
    à patir d'une grille donnée, renvoie cette même grille entouré d'un scotch(de 0)
    """
def detecte_coordonnees_combinaison(grille,i,j):
    """
    Renvoie une liste contenant les coordonnées de tout
    les bonbons appartenant à la combinaison du bonbon (i,j)
    """
def test_detecte_coordonnees_combinaison():

    """
    
    Teste la fonction detecte_coordonnees_combinaison(grille, i, j).
    Pour chaque cas de test, affiche True si le test passe, False sinon
    Pour éviter toute confusion par rapport à l'ordre dans lequel les combinaisons sont placées dans
    la liste renvoyée par detecte_coordonnees_combinaison, on préfère vérifier que chaque coordonnée 
    de bonbon impliquée dans la combinaison attendue est présente dans cette liste et qu'elle contient 
    le bon nombre de valeurs
    
    """
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
def valide_directions(i,j,grille):

    '''une fonction pour déterminer plus facilement dans quelle direction on peut faire des échanges
    renvoie une liste de chaines de caractères avec les directions valables'''

def tests_combinaisons(i,j,a,b,grille,cpt_combis):

    '''Une fonction qui teste simplement si les échanges donnent des combinaisons
    prend comme input i et j les coordonnées du bonbon de base (on va faire parcourir tous les i et j)
    prend comme input a et b, deux variables qui dépendent de la fonction verif_deadlock et valide_direction et qui varient selon la direction voulue pour le changement
    renvoie le nombre de combinaisons trouvées
    '''
def affichage_grille(grille, nb_type_bonbons):

    """ Affiche la grille de jeu "grille" contenant au maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    
    
size = 8
grille = gen_grille_init(size)
score=0
score_max = 2000
compteur_coups=0
nb_coups_max = 30
affichage_grille(grille, 4)

tant que le score < score_max et compteur_coups < nb_coups_max et verification_deadlock(grille) == False:
    grille,compteur_coups = echange_coords(grille,compteur_coups)
    afficher  "Il vous reste {nb_coups_max-compteur_coups} coups sur {nb_coups_max}"
    grille,score = regeneration(grille,score)
    afficher "Votre score est de {score}. Il vous manque {score_max-score} points pour atteindre l'objectif."
si score >= score_max :
    afficher "Félicitations vous avez gagné. Votre score final est de {score}."
si compteur_coups >= nb_coups_max :
    afficher "Vous n'avez pas réussi à atteindre l'objectif? Votre score final était de {score}"
si verification_deadlock(grille) == True:
    afficher "Vous avez atteint une grille irrésolvable. Votre score final était de {score}"

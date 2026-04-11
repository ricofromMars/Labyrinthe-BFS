import pygame
import sys
from maze import Maze
import solvers

# Couleurs utilisées pour le dessin
RED = (255, 44, 44)  # Rouge pour le point actuel et le chemin final
WHITE = (255, 255, 255)  # Blanc pour les murs
BLUE = (128, 206, 225)  # Bleu pour les cases visitées

# Paramètres de taille pour l'affichage
SIZE = 20  # Taille d'une case en pixels
OFFSET = 20  # Décalage pour centrer le labyrinthe
DELAI = 100  # Délai en ms entre chaque étape de recherche

def dessiner_mur(x, y):
    """Dessine un mur du labyrinthe

    Args:
        x (int): Coordonnée x en pixels
        y (int): Coordonnée y en pixels
    """
    rect = pygame.Rect(x, y, SIZE, SIZE)  # Créer un rectangle de taille SIZE x SIZE
    pygame.draw.rect(fen, WHITE, rect)  # Dessiner le rectangle en blanc

def dessiner_point(x, y, color):
    """Dessine un point du chemin

    Args:
        x (int): Coordonnée x dans la grille
        y (int): Coordonnée y dans la grille
        color (tuple): Couleur RGB du point
    """
    # Convertir les coordonnées grille en pixels, centrer le cercle
    pygame.draw.circle(fen, color, ((x*SIZE)+OFFSET+SIZE/2, (y*SIZE)+OFFSET+SIZE/2), 5)

def dessiner_cadre(lignes, colonnes):
    """Trace le cadre du labyrinthe (murs extérieurs)

    Args:
        lignes (int): Nombre de lignes du labyrinthe
        colonnes (int): Nombre de colonnes du labyrinthe
    """
    for r in range(lignes+2):  # +2 pour inclure le cadre
        for c in range(colonnes+2):
            # Si première ou dernière ligne, dessiner toute la ligne
            if r == 0 or r == lignes+1:
                x = c * SIZE
                y = r * SIZE
                dessiner_mur(x, y)
            # Sinon, dessiner seulement les bords gauche et droit
            elif c == 0 or c == colonnes+1:
                x = c * SIZE
                y = r * SIZE
                dessiner_mur(x, y)

def dessiner_labyrinthe(labyrinthe: Maze):
    """Trace le labyrinthe (murs intérieurs)

    Args:
        labyrinthe (Maze): Objet Maze contenant la grille
    """
    for r in range(labyrinthe.lignes):
        for c in range(labyrinthe.colonnes):
            valeur_case = labyrinthe.grille[r][c]  # Valeur de la case ('1' pour mur, etc.)
            # Calcul des coordonnées en pixels avec offset
            x = OFFSET + c * SIZE
            y = OFFSET + r * SIZE

            if valeur_case == "1":  # Si c'est un mur
                dessiner_mur(x, y)

def dessiner_chemin(chemin):
    """Trace le chemin trouvé en rouge

    Args:
        chemin (list): Liste de tuples (y, x) représentant le chemin
    """
    for y, x in chemin:
        dessiner_point(x, y, RED)  # Note: x et y sont inversés dans l'appel

def dessiner_visites(visites):
    """Trace les cases visitées en bleu

    Args:
        visites (list): Liste de tuples (y, x) des cases visitées
    """
    for y, x in visites:
        dessiner_point(x, y, BLUE)  # Note: x et y sont inversés dans l'appel

if __name__ == "__main__":
    # Vérifier si un nom de fichier est passé en argument
    if len(sys.argv) > 1:
        nom_fichier = sys.argv[1]
    else:
        nom_fichier = "maze.txt"  # Fichier par défaut
    
    # Charger le labyrinthe et initialiser le solveur A*
    labyrinthe = Maze(nom_fichier)

    # A FAIRE: INTEGRER LE CHOIX DU SOLVER A UTILISER
    while True:
        try:
            choix = int(input("Choix de l'algorithme (1:Bfs, 2:Dfs, 3:Dijkstra, 4:AStar) : "))
        except ValueError as e:
            print("Entrez un nombre")
        finally:
            if choix<1 and choix>4:
                print("Entrez un choix valide")
            else:
                break

    match choix:
        case 1:
            solver = solvers.SolverBfs(labyrinthe)
        case 2:
            solver = solvers.SolverDfs(labyrinthe)
        case 3:
            solver = solvers.SolverDijkstra(labyrinthe)
        case 4:
            solver = solvers.SolverAStar(labyrinthe)

    # Initialiser Pygame
    pygame.init()
    fen = pygame.display.set_mode((800, 600))  # Fenêtre de 800x600 pixels

    # Générateur pour la recherche de chemin (permet d'avancer étape par étape)
    solver_gen = solver.recherche_chemin()
    recherche = True  # Indicateur si la recherche est en cours
    start_time = pygame.time.get_ticks()  # Temps de départ pour le délai
    chemin = None  # Chemin final trouvé
    # Première étape : récupérer la position initiale et les visites
    y, x, visites = next(solver_gen)

    # Boucle principale du jeu
    while True:
        fen.fill((0, 0, 0))  # Effacer l'écran en noir
        dessiner_cadre(labyrinthe.lignes, labyrinthe.colonnes)  # Dessiner le cadre
        dessiner_labyrinthe(labyrinthe)  # Dessiner le labyrinthe

        if recherche:
            # Pendant la recherche : dessiner le point actuel et les visites
            dessiner_visites(visites)
            dessiner_point(x, y, RED)
            
            # Vérifier si le délai est écoulé pour passer à l'étape suivante
            if pygame.time.get_ticks() - start_time >= DELAI:
                start_time = pygame.time.get_ticks()  # Réinitialiser le timer
                try:
                    y, x, visites = next(solver_gen)  # Avancer d'une étape
                except StopIteration as e:
                    # Recherche terminée, récupérer le chemin
                    recherche = False
                    chemin = e.value
        else:
            # Recherche terminée : dessiner les visites et le chemin final
            if chemin:
                dessiner_visites(visites)
                dessiner_chemin(chemin)

        # Mettre à jour l'affichage
        pygame.display.update()

        # Gérer les événements (fermer la fenêtre)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
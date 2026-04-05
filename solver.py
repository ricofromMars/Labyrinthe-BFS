from collections import deque
from maze import Maze
import time

def resoudre_labyrinthe(labyrinthe: Maze):
    """
    Fonction principale de résolution.
    Prend une instance de la classe Maze en argument.
    """
    
    # 1. INITIALISATION
    # Créer la file (deque) et y ajouter le point de départ
    # Créer l'ensemble 'visites' (set) et y ajouter le départ
    # Créer le dictionnaire 'parents' : {depart: None}
    
    file = deque()
    file.append(labyrinthe.depart)
    visites = {labyrinthe.depart}
    parents = {labyrinthe.depart: None}

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # 2. BOUCLE PRINCIPALE
    while(file):
        noeud_actuel = file.popleft()

        if noeud_actuel == labyrinthe.arrivee:
            chemin = reconstruire_chemin(parents, noeud_actuel)
            return chemin
        
        # Recherche des voisins
        ar, ac = noeud_actuel
        for dr, dc in directions:
            vr = ar+dr
            vc = ac+dc

            # Tester si le voisin est dans la grille
            if labyrinthe.est_valide((vr,vc)):

                # Tester si le voisin n'est pas un mur
                if labyrinthe.grille[vr][vc] != '1':

                    # Tester si le voisin n'a pas déjà été visité
                    if (vr,vc) not in visites:

                        # Alors ajouter le voisin à visites
                        visites.add((vr,vc))
                        # Enregistrer noeud_actuel comme parent du noeud voisin
                        parents[(vr,vc)] = noeud_actuel
                        # Ajouter le voisin à la file
                        file.append((vr,vc))
    return None

def reconstruire_chemin(parents, arrivee):
    """
    Remonte le dictionnaire des parents de l'arrivée vers le départ.
    """
    chemin = []
    actuel = arrivee
    
    # Tant que actuel n'est pas None :
    #   Ajouter actuel à la liste chemin
    #   Passer au parent : actuel = parents[actuel]
    
    # Retourner le chemin inversé [::-1]
    while (actuel!=None):
        chemin.append(actuel)
        actuel = parents[actuel]

    return chemin[::-1]

if __name__ == "__main__":
    start_time = time.time()
    labyrinthe = Maze("maze.txt")
    chemin = resoudre_labyrinthe(labyrinthe)
    labyrinthe.afficher_labyrinthe(chemin)
    elapsed_time = time.time()-start_time
    print(f"Le chemin a été trouvé en {elapsed_time}s.")
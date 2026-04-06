import heapq
from maze import Maze
import time
import sys

def resoudre_labyrinthe(labyrinthe: Maze):
    """
    Fonction principale de résolution.
    Prend une instance de la classe Maze en argument.
    """
    
    # 1. INITIALISATION
    # une file heap pour stocker les noeuds à visiter sous forme (cout, (r,c))
    # un dictionnaire parents {(r,c): enfants}
    # un dictionnaire distances qui tient à jour les couts de chaque noeud
    heap = [(0, labyrinthe.depart)]
    distances = {labyrinthe.depart: 0}
    parents = {labyrinthe.depart: None}

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    couts = {"0":0, "5":5, "E":1, "S":1}

    # 2. BOUCLE PRINCIPALE
    # - retirer le noeud au cout le plus faible comme noeud_actuel (heapq.heappop())
    # - si ce n'est pas la sortie alors:
    # - explorer chaque noeud voisin
    # - si le noeud n'existe pas dans distances, créer l'entrée avec un cout infini (float('inf'))
    # - calculer le cout pour ce noeud (cout parent + cout noeud_actuel)
    # - si le cout est inférieur au cout actuel, mettre à jour le cout dans distances
    #   puis stocker le parent dans parents
    while(heap):
        noeud_actuel = heapq.heappop(heap)

        if noeud_actuel[1] == labyrinthe.arrivee:
            chemin = reconstruire_chemin(parents, noeud_actuel[1])
            return (chemin, distances[noeud_actuel[1]])
        
        # Recherche des voisins
        ar, ac = noeud_actuel[1]
        for dr, dc in directions:
            vr = ar+dr
            vc = ac+dc

            # Tester si le voisin est dans la grille
            if labyrinthe.est_valide((vr,vc)):

                # Tester si le voisin n'est pas un mur
                if labyrinthe.grille[vr][vc] != '1':

                    # Additionner le cout du noeud actuel et celui du voisin
                    # Vérifier si le cout cumulé est inférieur à celui dans distances
                    # Si oui mettre à jour voisin dans distances
                    cout = (distances[(ar,ac)]) + couts[labyrinthe.grille[vr][vc]]

                    if distances.get((vr,vc), float('inf'))>cout:
                        distances[(vr,vc)] = cout
                        parents[(vr,vc)] = (ar,ac)
                        heapq.heappush(heap, (distances[vr,vc], (vr,vc)))                                           
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
    # Vérifie si l'utilisateur a passé un nom de fichier en argument
    if len(sys.argv) > 1:
        nom_fichier = sys.argv[1]
    else:
        nom_fichier ="maze.txt"

    start_time = time.time()
    labyrinthe = Maze(nom_fichier)
    chemin = resoudre_labyrinthe(labyrinthe)

    if chemin:
        labyrinthe.afficher_labyrinthe(chemin[0])
        elapsed_time = time.time()-start_time
        print(f"Le chemin a été trouvé en {elapsed_time}s.")
        print(f"Le cout du chemin est: {chemin[1]}")

    else:
        print("Aucun chemin trouvé.")
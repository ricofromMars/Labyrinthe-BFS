# Labyrinthe BFS Solver 🧩

Un solveur de labyrinthe écrit en **Python** utilisant l'algorithme de **Recherche en Largeur (BFS)** pour garantir le chemin le plus court.

## 🚀 Fonctionnalités
- Lecture de labyrinthes personnalisés via fichiers `.txt`.
- Détection automatique du départ (`E`) et de l'arrivée (`S`).
- Algorithme BFS avec gestion des parents pour la reconstruction du chemin.

## 🛠️ Installation
bash
python3 -m venv .venv
source .venv/bin/activate

# Pas de dépendances externes pour le moment !

# Exemple d'exécution
====================
S * * * #          
# # # * #   # # #  
* * * *     #      
* # # # # # #   # #
* * * * * * * * #  
# # # # # # # * #  
      # * * * *    
  #   # * # # # # #
  #     * # * * * E
      # * * * # # #
====================

Le chemin a été trouvé en 0.0017886161804199219s.
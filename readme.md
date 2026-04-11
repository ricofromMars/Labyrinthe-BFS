Félicitations ! Ton code est devenu très propre, surtout avec l'intégration du `match/case` et du système de générateur. C'est une structure digne d'un vrai projet de visualisation d'algorithmes.

Voici une proposition de fichier `README.md` complète, structurée et rédigée dans un style professionnel pour mettre en valeur ton travail sur GitHub.

---

# 🧩 Maze Solver Visualization

Une application Python interactive utilisant **Pygame** pour visualiser en temps réel le fonctionnement de différents algorithmes de recherche de chemin dans un labyrinthe.

## ✨ Fonctionnalités

* **Visualisation Temps Réel** : Observez l'algorithme explorer le labyrinthe (cases visitées en bleu) avant de tracer le chemin optimal (en rouge).
* **Multi-Algorithmes** : Comparez l'efficacité des différentes méthodes :
    * **BFS** (Breadth-First Search) : Garantit le chemin le plus court dans un graphe non pondéré.
    * **DFS** (Depth-First Search) : Explore en profondeur, souvent moins optimal.
    * **Dijkstra** : Algorithme classique pour trouver le chemin le plus court.
    * **A*** (A-Star) : Recherche informée utilisant une heuristique pour gagner en rapidité.
* **Architecture Propre** : Utilisation du concept de **générateurs Python** (`yield`) pour une animation fluide sans bloquer l'interface utilisateur.
* **Découplage** : Logique de résolution et affichage graphique sont strictement séparés.

## 🛠️ Installation

1. **Cloner le repository** :
   ```bash
   git clone https://github.com/votre-utilisateur/maze-solver.git
   cd maze-solver
   ```

2. **Installer les dépendances** :
   Le projet nécessite uniquement `pygame`.
   ```bash
   pip install pygame
   ```

## 🚀 Utilisation

Lancez le programme principal :
```bash
python main.py [nom_du_labyrinthe.txt]
```

1. **Sélection** : Choisissez l'algorithme souhaité dans la console (1 à 4).
2. **Visualisation** : La fenêtre Pygame s'ouvre et l'animation commence automatiquement.
3. **Résultat** : Une fois la sortie trouvée, le chemin final est affiché en rouge.

## 📁 Structure du Projet

* `main.py` : Le point d'entrée du programme gérant l'interface Pygame et la boucle d'animation.
* `solvers.py` : Contient la classe mère `MazeSolver` et les classes filles héritées pour chaque algorithme.
* `maze.py` : Gestion des données du labyrinthe (lecture de fichier, validation des mouvements).
* `maze.txt` : Fichier de données représentant le labyrinthe (0 pour chemin, 1 pour mur).

## 📝 Format du Labyrinthe

Le fichier texte doit représenter le labyrinthe sous forme de grille :
* `S` : Point de départ.
* `E` : Sortie (End).
* `1` : Mur.
* `0` : Chemin libre.

---

### 💡 Axes d'amélioration futurs
* [ ] Ajout d'une interface de sélection directement dans la fenêtre Pygame.
* [ ] Possibilité de changer la vitesse de l'animation en temps réel.
* [ ] Support des déplacements en diagonale.
* [ ] Génération aléatoire de labyrinthes.

---
*Projet réalisé dans le cadre d'un apprentissage sur l'algorithmie et la programmation orientée objet en Python.*
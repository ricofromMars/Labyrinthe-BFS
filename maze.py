from pathlib import Path
import sys

class Maze:
    def __init__(self, nom_fichier):
        self.grille = Maze.charger_grille(nom_fichier)
        self.lignes = len(self.grille)
        self.colonnes = len(self.grille[0])
        self.depart = self.recherche_symbole("E")
        self.arrivee = self.recherche_symbole("S")
    

    def recherche_symbole(self, symbole):
        for r in range(self.lignes):
            for c in range(self.colonnes):
                if self.grille[r][c] == symbole:
                    return (r,c)
        match symbole:
            case "E":
                raise ValueError("Aucune entrée trouvée.")
            case "S":
                raise ValueError("Aucune sortie trouvée.")
            
    def afficher_structure(self):
        print("Structure du labyrinthe")
        print("-----------------------")
        print(f"Nombre de lignes: {self.lignes}")
        print(f"Nombre de colonnes: {self.colonnes}\n")
        print(f"Point d'entrée: {self.depart}")
        print(f"Point de sortie: {self.arrivee}")

    def est_valide(self, voisin):
        """Teste si un voisin se situe bien dans la grille"""
        vr, vc = voisin
        if vr>=0 and vc>=0 and vr<self.lignes and vc <self.colonnes:
            return True
        else:
            return False
        
    def afficher_labyrinthe(self, chemin=None):
        if chemin==None:
            chemin = []

        chemin_set = set(chemin) # plus rapide qu'une liste
        
        print("\n" + "=" * (self.colonnes*2)) # bordure supérieure

        for r in range(self.lignes):
            ligne = []
            for c in range(self.colonnes):
                valeur = self.grille[r][c]

                if (r,c) in chemin_set and valeur!="S" and valeur!="E":
                    char = "*"
                elif valeur == "1":
                    char = "#"
                elif valeur == "S":
                    char = "S"
                elif valeur == "E":
                    char = "E"
                else:
                    char = " "
                
                ligne.append(char)
            
            print(" ".join(ligne))

        print("=" * (self.colonnes*2) + "\n")

    @staticmethod
    def charger_grille(nom):
        """crée la liste contenant le labyrinthe à partir d'un fichier texte"""

        # Lit le fichier et stocke la chaine dans une variable
        try:
            contenu = Path(nom).read_text()

            # Transformer la chaine en liste de lignes
            lignes = [r.strip() for r in contenu.splitlines() if r.strip()]

            # Transformation en liste à deux dimensions
            return [[c for c in ligne if c != ' '] for ligne in lignes]
        
        except FileNotFoundError:
            print("Fichier introuvable")
            sys.exit(1)

# Test de la classe
if __name__ == "__main__":
    labyrinthe = Maze("maze.txt")
    labyrinthe.afficher_structure()
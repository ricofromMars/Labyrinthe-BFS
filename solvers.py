from abc import ABC, abstractmethod
from maze import Maze
from collections import deque
from typing import override
import heapq

class MazeSolver(ABC):
    DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
    COUTS = {"0":1, "5":5, "E":1, "S":1}

    def __init__(self, labyrinthe:Maze):
        self.labyrinthe = labyrinthe
        self.parents = {labyrinthe.depart: None}
        self.visites = {labyrinthe.depart}
        self.parcours = [labyrinthe.depart]
        self.parcours = [labyrinthe.depart]

    @abstractmethod
    def recherche_chemin(self):
        pass

    def _voisin_est_valide(self, vr, vc):
        """Teste si un voisin est valide:
        - est dans la grille
        - n'est pas un mur
        Args:
            vr (_type_): _description_
            vc (_type_): _description_

        Returns:
            _type_: _description_
        """
        # Tester si le voisin est dans la grille
        if self.labyrinthe.est_valide((vr,vc)):

            # Tester si le voisin n'est pas un mur
            if self.labyrinthe.grille[vr][vc] != '1':
                return True
            
        return False      

    def _reconstruire_chemin(self, parents, arrivee):
        """Renvoi le chemin en partant du départ

        Args:
            parents (_type_): _description_
            arrivee (_type_): _description_

        Returns:
            _type_: _description_
        """
        chemin = []
        actuel = arrivee
        
        while (actuel!=None):
            chemin.append(actuel)
            actuel = parents[actuel]

        return chemin[::-1]
    
class SolverBfs(MazeSolver):

    def __init__(self, labyrinthe):
        super().__init__(labyrinthe)
        self.file = deque()

    @override
    def recherche_chemin(self):
        
        self.file.append(self.labyrinthe.depart)
        
        while(self.file):
            noeud_actuel = self.file.popleft()
            self.parcours.append(noeud_actuel)

            yield((noeud_actuel[0], noeud_actuel[1], self.parcours))

            if noeud_actuel == self.labyrinthe.arrivee:
                chemin = self._reconstruire_chemin(self.parents, noeud_actuel)
                return chemin

            # Recherche des voisins
            ar, ac = noeud_actuel
            for dr, dc in self.DIRECTIONS:
                vr = ar+dr
                vc = ac+dc

                # Tester si le voisin est dans la grille
                if self._voisin_est_valide(vr,vc):

                    # Tester si le voisin n'a pas déjà été visité
                    if (vr,vc) not in self.visites:

                        # Alors ajouter le voisin à visites
                        self.visites.add((vr,vc))
                        # Enregistrer noeud_actuel comme parent du noeud voisin
                        self.parents[(vr,vc)] = noeud_actuel
                        # Ajouter le voisin à la file
                        self.file.append((vr,vc))
        return None
    
class SolverDfs(MazeSolver):

    def __init__(self, labyrinthe):
        super().__init__(labyrinthe)
        self.file = deque()

    @override
    def recherche_chemin(self):
        
        self.file.append(self.labyrinthe.depart)

        while(self.file):
            noeud_actuel = self.file.pop()
            self.parcours.append(noeud_actuel)

            yield((noeud_actuel[0], noeud_actuel[1], self.parcours))

            if noeud_actuel == self.labyrinthe.arrivee:
                chemin = self._reconstruire_chemin(self.parents, noeud_actuel)
                return chemin
            
            # Recherche des voisins
            ar, ac = noeud_actuel
            for dr, dc in self.DIRECTIONS:
                vr = ar+dr
                vc = ac+dc

                # Tester si le voisin est dans la grille
                if self._voisin_est_valide(vr,vc):

                    # Tester si le voisin n'a pas déjà été visité
                    if (vr,vc) not in self.visites:

                        # Alors ajouter le voisin à visites
                        self.visites.add((vr,vc))
                        # Enregistrer noeud_actuel comme parent du noeud voisin
                        self.parents[(vr,vc)] = noeud_actuel
                        # Ajouter le voisin à la file
                        self.file.append((vr,vc))
        return None
    
class SolverDijkstra(MazeSolver):

    def __init__(self, labyrinthe):
        super().__init__(labyrinthe)
        self.heap = [(0, labyrinthe.depart)]
        self.distances = {labyrinthe.depart: 0}

    @override
    def recherche_chemin(self):

        while(self.heap):
            noeud_actuel = heapq.heappop(self.heap)
            self.parcours.append(noeud_actuel[1])

            yield((noeud_actuel[1][0], noeud_actuel[1][1], self.parcours))

            if noeud_actuel[1] == self.labyrinthe.arrivee:
                chemin = self._reconstruire_chemin(self.parents, noeud_actuel[1])
                return chemin
            
            # Recherche des voisins
            ar, ac = noeud_actuel[1]
            for dr, dc in self.DIRECTIONS:
                vr = ar+dr
                vc = ac+dc

                # Tester si le voisin est valide
                if self._voisin_est_valide(vr,vc):
                    
                    cout = (self.distances[(ar,ac)]) + self.COUTS[self.labyrinthe.grille[vr][vc]]

                    if self.distances.get((vr,vc), float('inf'))>cout:
                        self.distances[(vr,vc)] = cout
                        self.parents[(vr,vc)] = (ar,ac)
                        heapq.heappush(self.heap, (self.distances[(vr,vc)], (vr,vc)))
        return None
    
class SolverAStar(MazeSolver):

    def __init__(self, labyrinthe):
        super().__init__(labyrinthe)
        self.heap = [(0, labyrinthe.depart)]
        self.distances = {labyrinthe.depart: 0}

    @override
    def recherche_chemin(self):

        while(self.heap):
            noeud_actuel = heapq.heappop(self.heap)
            self.parcours.append(noeud_actuel[1])

            yield((noeud_actuel[1][0], noeud_actuel[1][1], self.parcours))

            if noeud_actuel[1] == self.labyrinthe.arrivee:
                chemin = self._reconstruire_chemin(self.parents, noeud_actuel[1])
                return chemin
            
            # Recherche des voisins
            ar, ac = noeud_actuel[1]
            for dr, dc in self.DIRECTIONS:
                vr = ar+dr
                vc = ac+dc

                # Tester si le voisin est valide
                if self._voisin_est_valide(vr,vc):

                    cout = (self.distances[(ar,ac)]) + self.COUTS[self.labyrinthe.grille[vr][vc]]

                    if self.distances.get((vr,vc), float('inf'))>cout:
                        self.distances[(vr,vc)] = cout
                        self.parents[(vr,vc)] = (ar,ac)
                        heapq.heappush(self.heap, (self.distances[(vr,vc)] + self.__heuristique((vr,vc),self.labyrinthe.arrivee), (vr,vc)))
        return None
    
    def __heuristique(self, a, b):
        """Calcule la distance de Manhattan entre deux points"""
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
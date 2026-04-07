import random
class Pile:
    def __init__(self, name):
        self.nom = name
        self.liste = []

    def etre_vide(self):
        return self.liste == []

    def empiler(self, data):
        self.liste.append(data)

    def depiler(self):
        if not self.etre_vide():
            return self.liste.pop()
        else:
            return None

    def acceder_sommet(self):
        if not self.etre_vide():
            return self.liste[-1]
        else:
            return None

    def calculer_taille(self):
        return len(self.liste)

    def afficher(self):
        print("Début de la pile", self.nom)
        for i in range(len(self.liste)):
            print(self.liste[-1 - i])
        print("Fin de la pile", self.nom)
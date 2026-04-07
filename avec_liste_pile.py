class Pile:
    def __init__(self, name):
        self.name = name
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

    def afficher(self):
        print("Début de la pile", self.name)
        for i in range(len(self.liste)):
            print(self.liste[-1 -i])
        print("Fin de la pile", self.name)

    def calculer_taille(self):
        return len(self.liste)

# Utilisation de la classe : instanciation avec un objet
if __name__ == "__main__":

    # Création de la pile de l'exemple du cours
    pile_essai = Pile("premiere_pile")
    pile_essai.empiler(12)
    pile_essai.empiler(14)
    pile_essai.empiler(8)
    pile_essai.empiler(7)
    pile_essai.empiler(19)
    pile_essai.empiler(22)
    # Affichage de la pile
    pile_essai.afficher()

    # Récupération de la valeur en sommet de la pile (pop)
    valeur = pile_essai.depiler()
    print(valeur)
    pile_essai.afficher()

    # Ajout de la valeur 42 en sommet de pile (push)
    pile_essai.empiler(42)
    pile_essai.afficher()

    # Affichage de la valeur en sommet de pile (sommet)
    valeur = pile_essai.acceder_sommet()
    print(valeur)
    pile_essai.afficher()

    # Test de la fonction taille
    valeur = pile_essai.depiler()
    print(valeur)
    print("La taile de la pile est de ",pile_essai.calculer_taille(),"\n")

    # Test de la fonction pile_vide
    print("La pile est vide est une affirmation ",pile_essai.etre_vide(),"\n")
    for _ in range(5):
        valeur = pile_essai.depiler()
    print("La pile est vide est une affirmation ",pile_essai.etre_vide(),"\n")


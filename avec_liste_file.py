class File:
    def __init__(self, name):
        self.nom = name
        self.liste = []

    def etre_vide(self):
        return self.liste == []

    def ajouter(self, data):
        self.liste.append(data)

    def retirer(self):
        if not self.etre_vide():
            element = self.liste[0]
            self.liste.remove(element)
            return element
        else:
            return None

    def acceder_sommet(self):
        if not self.etre_vide():
            return self.liste[0]
        else:
            return None

    def calculer_taille(self):
        return len(self.liste)

    def afficher(self):
        print("Début de la file", self.nom)
        for element in self.liste:
            print(element, end = " <- ")
        print()
        print("Fin de la file", self.nom)

# Utilisation de la classe : instanciation avec un objet
if __name__ == "__main__":
        
    # Création de la file de l'exemple du cours
    file_essai = File("premiere_file")
    file_essai.ajouter(22)
    file_essai.ajouter(19)
    file_essai.ajouter(7)
    file_essai.ajouter(8)
    file_essai.ajouter(14)
    file_essai.ajouter(12)
    # Affichage de la file
    file_essai.afficher()

    input()

    # Ajout de la valeur 42 en sommet de file
    file_essai.ajouter(42)
    # Affichage de la file
    file_essai.afficher()

    input()

    # Récupération de la valeur en sommet de la file
    valeur = file_essai.retirer()
    print(valeur)
    # Affichage de la file
    file_essai.afficher()

    input()

    # Affichage de la valeur en acceder_sommet de file (sommet)
    valeur = file_essai.acceder_sommet()
    print(valeur)
    # Affichage de la file
    file_essai.afficher()

    input()

    # Test de la fonction taille
    valeur = file_essai.retirer()
    print(valeur)
    print("La taile de la file est de ",file_essai.calculer_taille(),"\n")

    # Test de la fonction file_etre_vide
    print("La file est vide est une affirmation ",file_essai.etre_vide(),"\n")
    for _ in range(5):
        valeur = file_essai.retirer()
    print("La file est vide est une affirmation ",file_essai.etre_vide(),"\n")


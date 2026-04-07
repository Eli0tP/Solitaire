'''Projet Solitaire Eliot Pechadre Term.F'''

from avec_liste_pile import Pile
from Jeucarte import *
from avec_liste_file import File
class Solitaire:
    def __init__(self, cartes, choix, visible_defausse):
        self.visible_defausse = visible_defausse
        self.choix = choix
        self.cartes = cartes
        self.pioches_visibles = File("Pioches")
        self.pioches_masque = File("Pioches suivantes")
        self.pioche_pile = Pile("pioche_pile")
        self.retirer_carte_deplacer = File("retire carte deplacer")
        self.talon1 = Pile("Défausse 1")
        self.talon2 = Pile("Défausse 2")
        self.talon3 = Pile("Défausse 3")
        self.talon4 = Pile("Défausse 4")
        self.carte_deplacer_talon = Pile("carte a deplacer vers talon")

        self.emplacements_famille = {
            'c': Pile("Coeurs"),
            'q': Pile("Carreaux"),
            'p': Pile("Piques"),
            't': Pile("Trèfles")
        }
        self.resutatT = []
        self.resutatP = []
        self.resutatC = []
        self.resutatQ = []
        self.liste32= ['7','8','9','10','V','D','R','As'] #suite attendue dans les emplacements familles pour le jeu de 32
        self.liste32T = ['As','R','D','V','10','9','8','7'] #suite attendue dans les defausses pour le jeu de 32
        self.liste52 = ['As','2','3','4','5','6','7','8','9','10','V','D','R'] #suite attendue dans les emplacements familles pour le jeu de 52
        self.liste52T = ['R','D','V','10','9','8','7','6','5','4','3','2','As'] #suite attendu dans les defausses pour le jeu de 52
        self.t = 1 ; self.p = 1  ; self.q = 1 ; self.c = 1
        self.score = 0
        self.retournements_carte = 0
        self.retournements_talon = 0

#cette fonction melange le jeu de carte et l'ajoute a la pioche puis creer les defausse avec 4, 3, 2 et 1 cartes a l'interieur
    def initialiser_jeu(self):
        self.cartes.melangerJeu()
        for carte in self.cartes.jeu:
            self.pioches_visibles.ajouter(carte)

        # Initialisation des 4 talons
        for i in range(10):
            carte = self.pioches_visibles.retirer()
            if i <= 3:
                self.talon1.empiler(carte)
            elif 3 <= i <= 6:
                self.talon2.empiler(carte)
            elif 6 <= i <= 8:
                self.talon3.empiler(carte)
            elif 8 <= i == 9:
                self.talon4.empiler(carte)

# Cette fonction gere tous l'affichage console
    def afficher_etat_jeu(self):
        print("\n~~~ ♥♦Le Solitaire♠♣ ~~~")
        print("\nTalon :", self.pioches_visibles.calculer_taille(), " cartes restantes:" ," Score actuel :", self.score ,
              "nombre de retournement de talon : ", self.retournements_talon)
        if self.pioches_visibles.etre_vide() :
            print("Pioche: vide" )
        else :
            print("Pioche:", [f"{carte.getValeur()} de {carte.getFamille()}"
                          for carte in self.pioches_visibles.liste][-1], self.interface_pioche(self.pioches_visibles.liste[-1]))
        if self.talon1.etre_vide() :
            print("Défausse 1 : vide")
        else :
            if self.visible_defausse == '1':
                print("Défausse 1:",[f"{carte.getValeur()} de {carte.getFamille()}"
                               for carte in self.talon1.liste], self.interface_pioche(self.talon1.liste[-1]))
            elif self.visible_defausse == '2' :
                print("Défausse 1:", [f"?" for i in range(self.talon1.calculer_taille() - 1)],
                                [f"{carte.getValeur()} de {carte.getFamille()}"
                                for carte in self.talon1.liste][-1], self.interface_pioche(self.talon1.liste[-1]))
        if self.talon2.etre_vide():
            print("Défausse 2 : vide")
        else:
            if visible_defausse == '1' :
                print("Défausse 2:",[f"{carte.getValeur()} de {carte.getFamille()}"
                                for carte in self.talon2.liste], self.interface_pioche(self.talon2.liste[-1]))
            elif visible_defausse == '2' :
                print("Défausse 2:",[f"?" for i in range(self.talon2.calculer_taille() - 1)],
                                [f"{carte.getValeur()} de {carte.getFamille()}"
                                for carte in self.talon2.liste][-1], self.interface_pioche(self.talon2.liste[-1]))
        if self.talon3.etre_vide():
            print("Défausse 3 : vide")
        else:
            if visible_defausse =='1' :
                print("Défausse 3:",[f"{carte.getValeur()} de {carte.getFamille()}"
                                for carte in self.talon3.liste], self.interface_pioche(self.talon3.liste[-1]))
            elif visible_defausse =='2' :
                print("Défausse 3:", [f"?" for i in range(self.talon3.calculer_taille() - 1)],
                                [f"{carte.getValeur()} de {carte.getFamille()}"
                                for carte in self.talon3.liste][-1], self.interface_pioche(self.talon3.liste[-1]))
        if self.talon4.etre_vide():
            print("Défausse 4 : vide")
        else:
            if self.visible_defausse == '1' :
                print("Défausse 4:",[f"{carte.getValeur()} de {carte.getFamille()}"
                                for carte in self.talon4.liste], self.interface_pioche(self.talon4.liste[-1]))
            elif self.visible_defausse == '2' :
                print("Défausse 4:", [f"?" for i in range(self.talon4.calculer_taille() - 1)],
                                [f"{carte.getValeur()} de {carte.getFamille()}"
                                for carte in self.talon4.liste][-1], self.interface_pioche(self.talon4.liste[-1]))
        print("\nEmplacements Famille:")
        print("\033[30m{}\033[00m".format("♣ Trèfle ♣") + ":", self.resutatT)
        print("\033[30m{}\033[00m".format("♠ Pique ♠") + ":", self.resutatP)
        print("\033[31m{}\033[00m".format("♦ Carreau ♦") + ":", self.resutatQ)
        print("\033[31m{}\033[00m".format("♥ Coeur ♥ ") + ":", self.resutatC)



# Celle-ci demande a l'utilisateur l'action qu'il souhaite effectuer
    def jouer(self):
        while not self.partie_terminee():
            self.afficher_etat_jeu()
            action = input("\nChoisissez une action (t=retourner, d=déplacer, x=abandonner): " ).lower()
            if action == 't':
                self.retourner_carte()
            elif action == 'd':
                self.deplacer_carte()
            elif action == 'x':
                print(f"Partie terminée. Votre score est de : " , self.score)
                quit()
            else:
                print("Action invalide. Choisissez parmi t, d ou x.")

#Celle-ci ajoute la valeur de la carte et un petit logo de sa famille pour plus de visuabilite a cote de la derniere carte dans la pioche et deffauses
    def interface_pioche(self, carte):
        if carte.getFamille() == 'Coeur' or carte.getFamille() == 'Carreau' :
            if carte.getFamille() == 'Coeur' :
                return ("\033[31m{}\033[00m".format(carte.getValeur() + " ♥") )
            return("\033[31m{}\033[00m".format(carte.getValeur() + " ♦"))
        elif carte.getFamille() == 'Pique' or carte.getFamille() == 'Trèfle' :
            if carte.getFamille() == 'Pique' :
                return ("\033[30m{}\033[00m".format(carte.getValeur() +" ♠"))
            return ("\033[30m{}\033[00m".format(carte.getValeur() + " ♣"))


#Celle-ci effectue l'action de retourner une carte + retire du score a chaque retournement de talon
    def retourner_carte(self):
        if self.pioches_visibles.etre_vide():
            print("Le talon est vide2.")
            return
        self.pioches_masque.ajouter(self.pioches_visibles.retirer())
        self.pioches_visibles.ajouter(self.pioches_masque.retirer())
        self.retournements_carte += 1
        if self.retournements_carte >= self.pioches_visibles.calculer_taille() :
            self.score -= 10
            self.retournements_carte = 0
            self.retournements_talon += 1


#celle ci deplace la carte si la fonction peut_deplacer est True
    def deplacer_carte(self):
        source = input("Choisissez une source ( p=pioche , 1=Défausse1, 2=Défausse2, 3=Défausse3, 4=Défausse4): ").lower()
        destinationChoix = input("Choisissez une destination (f=familles, d=Défausse): ")\
            .lower()
        if destinationChoix == 'f':
            destinationCouleur = input("Choissisez une destination (c=coeur, q=carreau, t=trèfle, p=pique)").lower()
        elif destinationChoix == 'd':
            destinationTalon = input("Choissisez une destination (1=talon1, 2=talon2, 3=talon3, 4=talon4)").lower()
        else :
            print("Destination invalide")
            return

        # Vérifiez si la source est valide et n'est pas vide
        source_pile = None
        if source == 'p':
            for carte in self.pioches_visibles.liste:
                self.pioche_pile.empiler(carte)
            source_pile = self.pioche_pile
            self.pioche_pile = Pile("pioche_pile")
        elif source == '1':
            source_pile = self.talon1
        elif source == '2':
            source_pile = self.talon2
        elif source == '3':
            source_pile = self.talon3
        elif source == '4':
            source_pile = self.talon4
        else:
            print("Source invalide.")
            return

        # Vérifiez si la destination est valide
        if destinationChoix == 'f' :
            if destinationCouleur not in self.emplacements_famille:
                print("Destination invalide.")
                return

        # Déplacez la carte si les règles sont respectées
        carte_a_deplacer = source_pile.acceder_sommet()
        if destinationChoix == 'f' :
            destination_pile = self.emplacements_famille[destinationCouleur]
        elif destinationChoix == 'd' :
            if destinationTalon == '1':
                destination_pile = self.talon1
            elif destinationTalon == '2':
                destination_pile = self.talon2
            elif destinationTalon == '3':
                destination_pile = self.talon3
            elif destinationTalon == '4':
                destination_pile = self.talon4

        if destinationChoix == 'd' :
            if destinationTalon == '1' :
                if self.peut_depalcer_carte_talon(destinationTalon,  carte_a_deplacer) == False :
                    return
                self.talon1.empiler(carte_a_deplacer)
                if source == 'p' :
                    self.retirer_carte_deplacer.liste = self.pioches_visibles.liste[:-1]
                    self.pioches_visibles = self.retirer_carte_deplacer
                self.score += 1
                if source != 'p' :
                    if source == '2':
                        self.talon2.depiler()
                    elif source == '3':
                        self.talon3.depiler()
                    elif source == '4':
                        self.talon4.depiler()
            elif destinationTalon == '2':
                if self.peut_depalcer_carte_talon(destinationTalon, carte_a_deplacer) == False:
                    return
                self.talon2.empiler(carte_a_deplacer)
                if source == 'p':
                    self.retirer_carte_deplacer.liste = self.pioches_visibles.liste[:-1]
                    self.pioches_visibles = self.retirer_carte_deplacer
                self.score += 1
                if source != 'p' :
                    if source == '1':
                        self.talon1.depiler()
                    elif source == '3':
                        self.talon3.depiler()
                    elif source == '4':
                        self.talon4.depiler()
            elif destinationTalon == '3':
                if self.peut_depalcer_carte_talon(destinationTalon, carte_a_deplacer) == False:
                    return
                self.talon3.empiler(carte_a_deplacer)
                if source == 'p':
                    self.retirer_carte_deplacer.liste = self.pioches_visibles.liste[:-1]
                    self.pioches_visibles = self.retirer_carte_deplacer
                self.score += 1
                if source != 'p' :
                    if source == '2':
                        self.talon2.depiler()
                    elif source == '1':
                        self.talon1.depiler()
                    elif source == '4':
                        self.talon4.depiler()
            elif destinationTalon == '4':
                if self.peut_depalcer_carte_talon(destinationTalon, carte_a_deplacer) == False:
                    return
                self.talon4.empiler(carte_a_deplacer)
                if source == 'p':
                    self.retirer_carte_deplacer.liste = self.pioches_visibles.liste[:-1]
                    self.pioches_visibles = self.retirer_carte_deplacer
                self.score += 1
                if source != 'p' :
                    if source == '2':
                        self.talon2.depiler()
                    elif source == '3':
                        self.talon3.depiler()
                    elif source == '1':
                        self.talon1.depiler()

        if destinationChoix == 'f' :
            if self.peut_deplacer_carte(carte_a_deplacer, destination_pile):
                source_pile.depiler()
                destination_pile.empiler(carte_a_deplacer)
                self.pioche_pile.depiler()
                if self.choix == '1' :
                    if source == 'p':
                        self.retirer_carte_deplacer.liste = self.pioches_visibles.liste[:-1]
                        self.pioches_visibles = self.retirer_carte_deplacer
                    if carte_a_deplacer.getFamille() == 'Pique':
                        self.resutatP.append(self.liste32[self.p-1])
                        self.score += 1
                    elif carte_a_deplacer.getFamille() == 'Trèfle':
                        self.resutatT.append(self.liste32[self.t-1])
                        self.score += 1
                    elif carte_a_deplacer.getFamille() == 'Coeur':
                        self.resutatC.append(self.liste32[self.c-1])
                        self.score += 1
                    elif carte_a_deplacer.getFamille() == 'Carreau':
                        self.resutatQ.append(self.liste32[self.q-1])
                        self.score += 1
                elif self.choix == '2' :
                    if source == 'p':
                        self.retirer_carte_deplacer.liste = self.pioches_visibles.liste[:-1]
                        self.pioches_visibles = self.retirer_carte_deplacer
                    if carte_a_deplacer.getFamille() == 'Pique':
                        self.resutatP.append(self.liste52[self.p-1])
                        self.score += 1
                    elif carte_a_deplacer.getFamille() == 'Trèfle':
                        self.resutatT.append(self.liste52[self.t-1])
                        self.score += 1
                    elif carte_a_deplacer.getFamille() == 'Coeur':
                        self.resutatC.append(self.liste52[self.c-1])
                        self.score += 1
                    elif carte_a_deplacer.getFamille() == 'Carreau':
                        self.resutatQ.append(self.liste52[self.q-1])
                        self.score += 1
            else:
                print("Déplacement invalide.")

#Celle-ci effectue des test pour savoir si une carte peut etre deplace suivant les regles ddu solitaire
    def peut_deplacer_carte(self, carte, destination_pile):
        if carte is None:
            return False
        # Vérifiez si la carte peut être déplacée vers la destination
        if destination_pile.etre_vide():
            if self.choix == '1' :
                return carte.getValeur() == "7"
            elif self.choix == '2' :
                return carte.getValeur() == "As"
        else:
            carte_destination = destination_pile.acceder_sommet()
            if carte.getFamille() == carte_destination.getFamille():
                if self.choix == '1' :
                    if carte.getFamille() == 'Pique':
                        if carte.getValeur() == self.liste32[self.p]:
                            self.p = self.p + 1
                            return True
                    elif carte.getFamille() == 'Trèfle':
                        if carte.getValeur() == self.liste32[self.t] :
                            self.t = self.t + 1
                            return True
                    elif carte.getFamille() == 'Carreau':
                        if carte.getValeur() == self.liste32[self.q] :
                            self.q = self.q + 1
                            return True
                    elif carte.getFamille() == 'Coeur':
                        if carte.getValeur() == self.liste32[self.c]:
                            self.c = self.c + 1
                            return True
                elif self.choix == '2' :
                    if carte.getFamille() == 'Pique':
                        if carte.getValeur() == self.liste52[self.p]:
                            self.p = self.p + 1
                            return True
                    elif carte.getFamille() == 'Trèfle':
                        if carte.getValeur() == self.liste52[self.t] :
                            self.t = self.t + 1
                            return True
                    elif carte.getFamille() == 'Carreau':
                        if carte.getValeur() == self.liste52[self.q] :
                            self.q = self.q + 1
                            return True
                    elif carte.getFamille() == 'Coeur':
                        if carte.getValeur() == self.liste52[self.c]:
                            self.c = self.c + 1
                            return True

#Celle-ci effectue la meme chose que peut_deplacer carte mais que pour la destination = les defausse
    def peut_depalcer_carte_talon(self, destinationTalon, carte):
        if self.choix == '1':
            if destinationTalon =='1':
                if self.talon1.calculer_taille() == 0:
                    return carte.getValeur() == 'As'
            elif destinationTalon =='2':
                if self.talon2.calculer_taille() == 0:
                    return carte.getValeur() == 'As'
            elif destinationTalon =='3':
                if self.talon3.calculer_taille() == 0:
                    return carte.getValeur() == 'As'
            elif destinationTalon =='4':
                if self.talon4.calculer_taille() == 0:
                    return carte.getValeur() == 'As'
        elif self.choix == '2' :
            if destinationTalon =='1':
                if self.talon1.calculer_taille() == 0:
                    return carte.getValeur() == 'R'
            elif destinationTalon =='2':
                if self.talon2.calculer_taille() == 0:
                    return carte.getValeur() == 'R'
            elif destinationTalon =='3':
                if self.talon3.calculer_taille() == 0:
                    return carte.getValeur() == 'R'
            elif destinationTalon =='4':
                if self.talon4.calculer_taille() == 0:
                    return carte.getValeur() == 'R'
        Fcarte = carte.getFamille()
        Vcarte = carte.getValeur()
        print(Vcarte, Fcarte)
        j = 0
        if self.choix == '1' :
            if Fcarte == 'Trèfle' or Fcarte == 'Pique' :
                if destinationTalon == '1':
                    carte = self.talon1.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Trèfle' or Ccarte == 'Pique' :
                        print("Impossible de deplacer cette carte ")
                        return False
                    else :
                        for i in range(len(self.liste32T)):
                            if self.liste32T[i] == Vcarte and self.liste32T[i-1] == carte.getValeur():
                                return  True
                        else :
                            print("Impossible de deplacer cette carte ")
                            return False
                elif destinationTalon == '2':
                    carte = self.talon2.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Trèfle' or Ccarte == 'Pique':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste32T)):
                            if self.liste32T[i] == Vcarte and self.liste32T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
                elif destinationTalon == '3':
                    carte = self.talon3.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Trèfle' or Ccarte == 'Pique':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste32T)):
                            if self.liste32T[i] == Vcarte and self.liste32T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
                elif destinationTalon == '4':
                    carte = self.talon4.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Trèfle' or Ccarte == 'Pique':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste32T)):
                            if self.liste32T[i] == Vcarte and self.liste32T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
            elif Fcarte == 'Carreau' or Fcarte == 'Coeur' :
                if destinationTalon == '1':
                    carte = self.talon1.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Carreau' or Ccarte == 'Coeur':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste32T)):
                            if self.liste32T[i] == Vcarte and self.liste32T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
                elif destinationTalon == '2':
                    carte = self.talon2.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Carreau' or Ccarte == 'Coeur':
                        print("Impossible de deplacer cette carte ")
                        return False
                elif destinationTalon == '3':
                    carte = self.talon3.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Carreau' or Ccarte == 'Coeur':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste32T)):
                            if self.liste32T[i] == Vcarte and self.liste32T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
                elif destinationTalon == '4':
                    carte = self.talon4.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Carreau' or Ccarte == 'Coeur':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste32T)):
                            if self.liste32T[i] == Vcarte and self.liste32T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
        elif self.choix == '2' :
            if Fcarte == 'Trèfle' or Fcarte == 'Pique' :
                if destinationTalon == '1':
                    carte = self.talon1.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Trèfle' or Ccarte == 'Pique' :
                        print("Impossible de deplacer cette carte ")
                        return False
                    else :
                        for i in range(len(self.liste52T)):
                            if self.liste52T[i] == Vcarte and self.liste52T[i-1] == carte.getValeur():
                                return  True
                        else :
                            print("Impossible de deplacer cette carte ")
                            return False
                elif destinationTalon == '2':
                    carte = self.talon2.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Trèfle' or Ccarte == 'Pique':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste52T)):
                            if self.liste52T[i] == Vcarte and self.liste52T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
                elif destinationTalon == '3':
                    carte = self.talon3.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Trèfle' or Ccarte == 'Pique':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste52T)):
                            if self.liste52T[i] == Vcarte and self.liste52T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
                elif destinationTalon == '4':
                    carte = self.talon4.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Trèfle' or Ccarte == 'Pique':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste52T)):
                            if self.liste52T[i] == Vcarte and self.liste52T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
            elif Fcarte == 'Carreau' or Fcarte == 'Coeur' :
                if destinationTalon == '1':
                    carte = self.talon1.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Carreau' or Ccarte == 'Coeur':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste52T)):
                            if self.liste52T[i] == Vcarte and self.liste52T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
                elif destinationTalon == '2':
                    carte = self.talon2.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Carreau' or Ccarte == 'Coeur':
                        print("Impossible de deplacer cette carte ")
                        return False
                elif destinationTalon == '3':
                    carte = self.talon3.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Carreau' or Ccarte == 'Coeur':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste52T)):
                            if self.liste52T[i] == Vcarte and self.liste52T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False
                elif destinationTalon == '4':
                    carte = self.talon4.liste[-1]
                    Ccarte = carte.getFamille()
                    if Ccarte == 'Carreau' or Ccarte == 'Coeur':
                        print("Impossible de deplacer cette carte ")
                        return False
                    else:
                        for i in range(len(self.liste52T)):
                            if self.liste52T[i] == Vcarte and self.liste52T[i-1] == carte.getValeur():
                                return True
                        else:
                            print("Impossible de deplacer cette carte ")
                            return False

#celle-ci verifie si le joueur a gagne la partie et l'arrete
    def partie_terminee(self):
        # Vérifiez si toutes les cartes sont dans les emplacements famille
        if self.choix =='1' :
            for famille in self.emplacements_famille.values() :
                if famille.calculer_taille() != 8 :
                    return False
            print("Vous avez gagne avec un score de :", self.score)
            quit()
        elif self.choix == '2' :
            for famille in self.emplacements_famille.values():
                if famille.calculer_taille() != 13:
                    return False
            print("Vous avez gagne avec un score de :", self.score)
            quit()

# l'instanciation avec un choix d'un jeu de 32 ou 52 et si on veut voir les cartes dans les deffauses ou pas
print("╭━━━━━━━━━━━━━━━━━━━━━━━╮")
print("|♦                     ♦|")
print("|♣ Bienvenue au jeu du ♣|")
print("|♠       Solitaire     ♠|")
print("|♥                     ♥|")
print("|♦                     ♦|")
print("|♣ Choisissez le type  ♣|")
print("|♠ de jeu :            ♠|")
print("|♥                     ♥|")
print("|♦ 1. 32 Cartes        ♦|")
print("|♣ 2. 52 Cartes        ♣|")
print("|♠                     ♠|")
print("|♥                     ♥|")
print("╰━━━━━━━━━━━━━━━━━━━━━━━╯")
choix = input("Entrez 1 pour un jeu de 32 cartes ou 2 pour un jeu de 52 cartes: ")
visible_defausse = input("Voulez voir toutes les cartes des defausses 1=Oui, 2=Non ")
# pioche_3 = input("Voulez piochez des cartes 3 par 3 (seule la 1er sera deplaçable). 1=Oui, 2=Non")
if visible_defausse == '1' :
    if choix == '1':
        cartes = JeuCarte("32")
        jeu = Solitaire(cartes , '1' ,'1')
        jeu.initialiser_jeu()
        jeu.jouer()
    elif choix == '2':
        cartes = JeuCarte("52")
        jeu = Solitaire(cartes, '2', '1')
        jeu.initialiser_jeu()
        jeu.jouer()
elif visible_defausse == '2' :
    if choix == '1':
        cartes = JeuCarte("32")
        jeu = Solitaire(cartes , '1' ,'2')
        jeu.initialiser_jeu()
        jeu.jouer()
    elif choix == '2':
        cartes = JeuCarte("52")
        jeu = Solitaire(cartes, '2', '2')
        jeu.initialiser_jeu()
        jeu.jouer()


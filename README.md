# Solitaire en console (Python)

Jeu du Solitaire (Klondike simplifié) jouable dans le terminal, réalisé en Terminale (spécialité NSI)
pour mettre en pratique les structures de données **pile** (LIFO) et **file** (FIFO).

## Fonctionnalités

- Choix du jeu : **32 cartes** ou **52 cartes**
- Mélange du paquet, distribution de quatre défausses (4, 3, 2 et 1 cartes) et pioche
- Déplacement des cartes de la pioche ou des défausses vers les fondations (une par famille) ou vers une autre
  défausse, avec vérification de l'ordre des valeurs
- Option pour afficher ou masquer les cartes des défausses
- Score et compteur de retournements

## Structures de données

| Fichier | Rôle |
|---|---|
| `cartes.py` | classe `Carte` (valeur, famille) |
| `Jeucarte.py` | classe `JeuCarte` : création et mélange d'un paquet de 32 ou 52 cartes |
| `avec_liste_pile.py` | classe `Pile` (LIFO) : défausses et fondations |
| `avec_liste_file.py` | classe `File` (FIFO) : pioche |
| `textSolitaire.py` | classe `Solitaire` : règles et boucle de jeu |

## Lancer le jeu

```bash
python textSolitaire.py
```

Aucune dépendance externe. Le jeu se pilote au clavier via les questions posées dans le terminal
(`t` retourner une carte, `d` déplacer, `x` abandonner).

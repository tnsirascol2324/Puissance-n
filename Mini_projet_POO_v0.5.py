### CODE
## Classe Grille
class Grille :
    '''Classe Grille :\n
        * Créer un objet :\n
        monObjet = (Largueur_grille = 7 (int), Hauteur_Grille = 6 (int), Nbr_Pions_A_Aligner_Pour_Gagner = 4 (int))
        
        * Attributs :\n
        hauteur | largeur | prerequis_Gagne | grille
        
        * Méthodes :\n
        afficher_Grille() = Affiche la grille de jeu'''

    def __init__ (self, pLargeur : int = 7, pHauteur : int = 6, pPrerequis_Gagne : int = 4) :
        # Assertion pour vérifier les inputs de l'utilisateur
        assert (type(pLargeur) == int) and (type(pHauteur) == int) and (type(pPrerequis_Gagne) == int), "Il faut mettre des entiers >= 2 !"
        assert (pLargeur >= 2) and (pHauteur >= 2) and (pPrerequis_Gagne >= 2), "Il faut mettre des entiers >= 2 !"

        # Attributs d'instance
        self.hauteur = pHauteur
        self.largeur = pLargeur
        self.prerequis_Gagne = pPrerequis_Gagne
        self.grille = [["_" for j in range(self.largeur)] for i in range(self.hauteur)] # Créer la grille à l'initialisation

    def afficher_Grille(self) :
        '''Print la grille actuelle dans la console, affiche un "_" si case vide, sinon affiche le symbole du joueur'''
        for i in range(self.largeur) : # Affichage des chiffres au dessus des colones
            print(f"  {i+1} ", end="")
        print()
        print(" "+ "___"*self.largeur +"_"*(self.largeur-1)) # Affichage de la ligne en haut
        for x in self.grille : # Affichage des lignes du mileu avec les pions
            for y in x :
                print(f"| {y} ", end ="")
            print("|")
        print(" "+ "‾‾‾"*self.largeur +"‾"*(self.largeur-1)) # Affichage de la ligne en bas

### TESTS
## Affichage d'une grille simple
puissance4 = Grille()
puissance4.afficher_Grille()

## Affichage d'une petite grille
puissance4 = Grille(3,4)
puissance4.afficher_Grille()

## Affichage d'une grande grille
puissance4 = Grille(25, 14)
puissance4.afficher_Grille()


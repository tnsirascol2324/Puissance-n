### CODE
## Classe Grille
class Grille :
    '''Classe Grille :\n
        * Créer un objet :\n
        monObjet = (Largueur_grille = 7 (int), Hauteur_Grille = 6 (int), Nbr_Pions_A_Aligner_Pour_Gagner = 4 (int))
        
        * Attributs :\n
        hauteur | largeur | prerequis_Gagne | grille\n
        Précision pour l'attribut grille : cet attribut contient un tableau qui ne contient que des None 
        
        * Méthodes :\n
        afficher_Grille() = Affiche la grille de jeu
        placer_Pion(objet de la classe Joueur, colonne affichée par .afficher_Grille()) = Placer un pion dans la grille (remplace le None de la case par l'objet de la classe Joueur)'''

    def __init__ (self, pLargeur : int = 7, pHauteur : int = 6, pPrerequis_Gagne : int = 4) :
        # Assertion pour vérifier les inputs de l'utilisateur
        assert (type(pLargeur) == int) and (type(pHauteur) == int) and (type(pPrerequis_Gagne) == int), "Il faut mettre des entiers >= 2 !"
        assert (pLargeur >= 2) and (pHauteur >= 2) and (pPrerequis_Gagne >= 2), "Il faut mettre des entiers >= 2 !"

        # Attributs d'instance
        self.__hauteur = pHauteur
        self.__largeur = pLargeur
        self.__prerequis_Gagne = pPrerequis_Gagne
        self.grille = [[None for j in range(self.__largeur)] for i in range(self.__hauteur)] # Crée la grille à l'initialisation

    def afficher_Grille(self) :
        '''Print la grille actuelle dans la console, affiche un "_" si case vide, sinon affiche le symbole du joueur'''
        for i in range(self.__largeur) : # Affichage des chiffres au dessus des colones
            print(f"  {i+1} ", end="")
        print()
        print(" "+ "___"*self.__largeur +"_"*(self.__largeur-1)) # Affichage de la ligne en haut
        for x in self.grille : # Affichage des lignes du mileu avec les pions
            for y in x :
                if y != None : # Si case rempli, affiche l'icône du joueur
                    print(f"| {y.icone} ", end ="")
                else : # Sinon (si case vide), mets un underscore
                    print(f"| _ ", end ="")
            print("|")
        print(" "+ "‾‾‾"*self.__largeur +"‾"*(self.__largeur-1)) # Affichage de la ligne en bas
    
    def placer_Pion(self, joueur, colonne) :
        '''Réécrit la case visé avec l'objet Joueur(paramètre joueur).\n
        Si il n'y a pas de case dispo, return False, sinon réécrit la case et return True'''
        indice_Ligne = self.__hauteur - 1
        indice_Colonne = colonne - 1
        while self.grille[indice_Ligne][indice_Colonne] != None : # Continue tant que l'on ne trouve pas de case vide dans la colonne
            indice_Ligne = indice_Ligne - 1 # Augmente l'indice 
            if indice_Ligne < 0 : # Teste si l'indice n'est pas "out of range", si oui, arrête le programme, si non, on continue à chercher
                return False
        # Dès que la boucle s'arrête, ca veut dire qu'on a trouvé une case vide
        self.grille[indice_Ligne][indice_Colonne] = joueur # Donc on réécrit la case
        return True

## Classe Joueur
class Joueur :
    '''Classe Joueur :\n
    * Créer un objet :\n
    monObjet = (Nom_Joueur (str), Icone_Pions (str))
    
    * Attributs :\n
    nom | icone
    
    * Méthodes :\n
    __str__ = affiche les attributs du joueur'''
    
    def __init__(self, pNom : str, pIcone : str) :
        while pNom == "" : # Test si l'utilisateur rentre un nom vide
            pNom = input("Merci de rentrer un nom valide : ")        
        while pIcone == "_" or pIcone == "" : # Test si l'utilisateur rentre une icone vide ou un "_"
            pIcone = input("Merci de rentrer une icone valide (non vide et ≠ de _) : ")
        self.nom = pNom
        self.icone = pIcone
    
    def __str__(self) :
        return (f"Le joueur {self.nom} utilise les pions '{self.icone}'")

### TESTS
## Affichage de la grille
puissance4 = Grille()
puissance4.afficher_Grille()

## Création des objets Joueur
joueur1 = Joueur("Steve", "x")
joueur2 = Joueur("Alex", "o")
print(f"{joueur1}\n{joueur2}")

## Placement des pions
puissance4.placer_Pion(joueur1, 3)
puissance4.afficher_Grille()
puissance4.placer_Pion(joueur2, 6)
puissance4.afficher_Grille()
puissance4.placer_Pion(joueur1, 1)
puissance4.afficher_Grille()
puissance4.placer_Pion(joueur2, 1)
puissance4.afficher_Grille()
puissance4.placer_Pion(joueur1, 1)
puissance4.afficher_Grille()
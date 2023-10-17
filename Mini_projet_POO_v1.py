### CODE
## Classe Grille
class Grille :
    '''Classe Grille :\n
        * Créer un objet :\n
        monObjet = (Largueur_grille = 7 (int), Hauteur_Grille = 6 (int), Nbr_Pions_A_Aligner_Pour_Gagner = 4 (int))
        
        * Attributs :\n
        __hauteur | __largeur | __prerequis_Gagne | __grille\n
        Précision pour l'attribut grille : cet attribut contient un tableau qui ne contient que des None 
        
        * Méthodes :\n
        get_Largeur() = Renvoie la largeur de la grille\n
        afficher_Grille() = Affiche la grille de jeu\n
        placer_Pion(objet de la classe Joueur, colonne affichée par .afficher_Grille()) = Placer un pion dans la grille (remplace le None de la case par l'objet de la classe Joueur)'''

    def __init__ (self, pLargeur : int = 7, pHauteur : int = 6, pPrerequis_Gagne : int = 4) :
        # Assertion pour vérifier les inputs de l'utilisateur
        assert (type(pLargeur) == int) and (type(pHauteur) == int) and (type(pPrerequis_Gagne) == int), "Il faut mettre des entiers >= 2 !"
        assert (pLargeur >= 2) and (pHauteur >= 2) and (pPrerequis_Gagne >= 2), "Il faut mettre des entiers >= 2 !"

        # Attributs d'instance
        self.__hauteur = pHauteur
        self.__largeur = pLargeur
        self.__prerequis_Gagne = pPrerequis_Gagne
        self.__grille = [[None for j in range(self.__largeur)] for i in range(self.__hauteur)] # Crée la grille à l'initialisation

    def get_Largeur(self) :
        '''Retourne la largeur'''
        return self.__largeur

    def afficher_Grille(self) :
        '''Print la grille actuelle dans la console, affiche un "_" si case vide, sinon affiche le symbole du joueur'''
        for i in range(self.__largeur) : # Affichage des chiffres au dessus des colones
            print(f"  {i+1} ", end="")
        print()
        print(" "+ "___"*self.__largeur +"_"*(self.__largeur-1)) # Affichage de la ligne en haut
        for x in self.__grille : # Affichage des lignes du mileu avec les pions
            for y in x :
                if y != None : # Si case rempli, affiche l'icône du joueur
                    print(f"| {y.icone} ", end ="")
                else : # Sinon (si case vide), mets un underscore
                    print(f"| _ ", end ="")
            print("|")
        print(" "+ "‾‾‾"*self.__largeur +"‾"*(self.__largeur-1)) # Affichage de la ligne en bas
    
    def placer_Pion(self, pjoueur, pcolonne) :
        '''Réécrit la case visé avec l'objet Joueur(paramètre joueur).\n
        Si il n'y a pas de case dispo, return False, sinon réécrit la case et return True'''
        indice_Ligne = self.__hauteur - 1
        indice_Colonne = pcolonne - 1
        while self.__grille[indice_Ligne][indice_Colonne] != None : # Continue tant que l'on ne trouve pas de case vide dans la colonne
            indice_Ligne = indice_Ligne - 1 # Augmente l'indice 
            if indice_Ligne < 0 : # Teste si l'indice n'est pas "out of range", si oui, arrête le programme, si non, on continue à chercher
                return False
        # Dès que la boucle s'arrête, ca veut dire qu'on a trouvé une case vide
        self.__grille[indice_Ligne][indice_Colonne] = pjoueur # Donc on réécrit la case
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
        while pIcone == "_" or pIcone == "" or len(pIcone) != 1 : # Test si l'utilisateur rentre une icone vide ou un "_"
            pIcone = input("Merci de rentrer une icone valide (un seul caractère, non vide et ≠ de _) : ")
        self.nom = pNom
        self.icone = pIcone
    
    def __str__(self) :
        return (f"Le joueur {self.nom} utilise les pions '{self.icone}'")

## Programme affichage utilisateur
# Fonction pour demarrer le jeu
def demarrage_Jeu() :
    print(r"Puissance n, ∀ n ∈ ℕ* \{1}")
    mode_De_Jeu = input("\nSelectionner un mode de jeu :\n1 - Puissance 4\n2 - Grille personnalisée\n>>> ")
    try : # Teste si l'utilisateur est con et ne rentre pas d'entier
        mode_De_Jeu = int(mode_De_Jeu)
    except :
        raise AssertionError ("Gros boloss, fallait mettre 1 ou 2, tu sais pas compter ?!?")
    mode_De_Jeu = int(mode_De_Jeu)
    
    # Gère en fonction du mode de jeu rentré
    if mode_De_Jeu == 1 :
        return Grille()
    elif mode_De_Jeu == 2 :
        print("Paramètres de la grille :")
        hauteur = int(input("Hauteur de la grille : "))
        largueur = int(input("Largueur de la grille : "))
        return Grille(largueur, hauteur)
    else :
        raise AssertionError ("Gros boloss, fallait mettre 1 ou 2, tu sais pas compter ?!?")

# Création de la grille
puissanceN = demarrage_Jeu()

# Création des personnages
print("\nCréation des joueurs :")
print("Joueur 1 (Il commencera la partie) :")
perso1 = Joueur(input("Ton nom = "), input("Icone de ton pion = "))
print("\nJoueur 2 :")
perso2 = Joueur(input("Ton nom = "), input("Icone de ton pion = "))

# Démarrage de la phase de jeu
print("\nDémarrage du jeu :\n(Si un gagnant apparait, noter -1 au moment de placer un pion)\n")

pas_De_Gagnant = True
joueurs = [perso1, perso2]
joueur_Pion = perso1
incrementeur = 1
while pas_De_Gagnant : # Boucle du jeu
    not_Entier = True
    not_Valide = True
    puissanceN.afficher_Grille() # 1 - Affiche la grille

    while not_Entier : # Teste si l'input est un entier
        colonne_Input = input(f"{joueur_Pion.nom}, place un pion : ") # Demande au joueur de jouer un pion
        try :
            assert(colonne_Input != "")
            colonne_Input = int(colonne_Input) # Si input un entier, on continue
            not_Entier = False 
        except :
            print("Colonne invalide !") # Sinon, on recommence
    colonne_Input = int(colonne_Input)

    while (colonne_Input < 1 and colonne_Input != -1) or colonne_Input > puissanceN.get_Largeur() : # 2.2 - Redemande si le joueur est con et n'a pas rentré une colonne valide
        print("Colonne invalide !")
        colonne_Input = input(f"{joueur_Pion.nom}, place un pion : ")
    
    if colonne_Input == -1 :
        pas_De_Gagnant = False
    else :
        puissanceN.placer_Pion(joueur_Pion, colonne_Input)
        joueur_Pion = joueurs[incrementeur - (incrementeur//2)*2]
        incrementeur += 1
    print()

print("Partie terminée !")
### CLASSES
## Classe Grille
class Grille :
    '''Classe Grille :\n
        * Créer un objet :\n
        monObjet = (Largueur_grille = 7 (int), Hauteur_Grille = 6 (int), Nbr_Pions_A_Aligner_Pour_Gagner = 4 (int))
        
        * Attributs :\n
        __hauteur | __largeur | __prerequis_Gagne | __grille\n
        Précision pour l'attribut grille : cet attribut contient un tableau qui ne contient que des None 
        
        * Méthodes :\n
        __str__ = Affiche les attributs de taille de la grille\n
        get_Largeur() = Renvoie la largeur de la grille\n
        grille_Pleine() = Renvoie True si la grille est pleine, sinon False\n
        afficher_Grille() = Affiche la grille de jeu\n
        placer_Pion(objet de la classe Joueur, colonne affichée par .afficher_Grille()) = Placer un pion dans la grille (remplace le None de la case par l'objet de la classe Joueur)'''

    def __init__ (self, pLargeur : int = 7, pHauteur : int = 6, pPrerequis_Gagne : int = 4) :
        # Attributs d'instance
        self.__hauteur = pHauteur
        self.__largeur = pLargeur
        self.__prerequis_Gagne = pPrerequis_Gagne
        self.__grille = [[None for j in range(self.__largeur)] for i in range(self.__hauteur)] # Crée la grille à l'initialisation

    def get_Largeur(self) :
        '''Renvoie la largeur de la grille (càd l'attribut self.__largeur)'''
        return self.__largeur

    def __str__ (self) :
        return f"Cette grille est haute de {self.__hauteur} lignes et large de {self.__largeur} colonnes."

    def grille_Pleine (self) :
        '''Renvoie True si la grille est pleine, sinon False'''
        for x in self.__grille : # Parcours toute les lignes
            if None in x : # Regarde si il y a un None
                return False # Si oui, on renvoie False
        return True # Si non, True

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
    
    def placer_Pion(self, joueur, colonne) :
        '''Réécrit la case visé avec l'objet Joueur(paramètre joueur).\n
        Si il n'y a pas de case dispo, return False, sinon réécrit la case et return True'''
        indice_Ligne = self.__hauteur - 1
        indice_Colonne = colonne - 1
        while self.__grille[indice_Ligne][indice_Colonne] != None : # Continue tant que l'on ne trouve pas de case vide dans la colonne
            indice_Ligne = indice_Ligne - 1 # Augmente l'indice 
            if indice_Ligne < 0 : # Teste si l'indice n'est pas "out of range", si oui, arrête le programme, si non, on continue à chercher
                return False
        # Dès que la boucle s'arrête, ca veut dire qu'on a trouvé une case vide
        self.__grille[indice_Ligne][indice_Colonne] = joueur # Donc on réécrit la case
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
        self.nom = pNom
        self.icone = pIcone
    
    def __str__(self) :
        return (f"Le joueur {self.nom} utilise les pions '{self.icone}'")

### CODE
## Fonction test entier
def est_Entier(valeur) :
    '''Teste si la valeur est un entier'''
    try :
        valeur = int(valeur)
        assert(valeur > 0)
        return True
    except :
        return False

## Fontion test si le nom est vide ou pas
def est_Nom_Valide(nom) :
    '''Teste si le nom est valide pour la classe Joueur'''
    if nom == "" :
        return False
    else :
        return True

## Fonction test si l'îcone est valide 
def est_Icone_Valide(icone) :
    '''Teste si l'icone est valide pour la classe Joueur'''
    if icone == "_" or len(icone) != 1 :
        return False
    else :
        return True

## Programme du jeu
# Affichage du titre du jeu
print(r"----- Puissance n, ∀ n ∈ ℕ * -----")
print("Mode de jeu : Arbitrage manuel")

# Set up de la hauteur de la grille
print("----------------------------------\nParamètres de la grille :\n----------------------------------")
hauteur_Grille = input("Hauteur de la grille\n>>> ")
while not est_Entier(hauteur_Grille) :
    hauteur_Grille = input(">>> ")
hauteur_Grille = int(hauteur_Grille)

# Set up de la largeur de la grille
largeur_Grille = input("Largeur de la grille :\n>>> ")
while not est_Entier(largeur_Grille) :
    largeur_Grille = input(">>> ")
largeur_Grille = int(largeur_Grille)

print("----------------------------------")

# Initialisation de la grille
puissanceN = Grille(largeur_Grille, hauteur_Grille)

# Set up joueur 1
print("Création des joueurs :\n----------------------------------")
print("Joueur 1 (il commencera la partie) :")

# Set up nom du joueur 1
joueur1_Nom = input("Nom\n>>> ")
while not est_Nom_Valide(joueur1_Nom) :
    joueur1_Nom = input(">>> ")

# Set up icone du joueur 1
joueur1_Icone = input("Icone de ton pion\n>>> ")
while not est_Icone_Valide(joueur1_Icone) :
    joueur1_Icone = input(">>> ")

# Set up joueur 2
print("Joueur 2 :")

# Set up nom du joueur 2
joueur2_Nom = input("Nom\n>>> ")
while (not est_Nom_Valide(joueur2_Nom)) or joueur2_Nom == joueur1_Nom :
    joueur2_Nom = input(">>> ")

# Set up icone du joueur 2
joueur2_Icone = input("Icone de ton pion\n>>> ")
while not (est_Icone_Valide(joueur2_Icone)) or joueur2_Icone == joueur1_Icone :
    joueur2_Icone = input(">>> ")

print("----------------------------------")

# Unitialisation des joueurs
joueurs = [Joueur(joueur1_Nom, joueur1_Icone), Joueur(joueur2_Nom, joueur2_Icone)]

# Démarrage du jeu
print("Démarrage du jeu :\n(Mettre 'FIN' au moment de placer un pion pour finir la partie)")
pas_De_Gagnant = True
incrementeur = 0
while pas_De_Gagnant : # Boucle de jeu qui permet de placer les pions
    joueur_Actuel = joueurs[incrementeur - (incrementeur//2)*2] # Permet de switch de joueur chaque tour
    puissanceN.afficher_Grille() # 1 - J'affiche la grille
    input_Colonne = input(f"{joueur_Actuel.nom}, place un pion\n>>> ") # 2 - Je fais jouer le joueur actuel
    if input_Colonne == "FIN" : # Si le joueur entre "FIN", j'arrête le jeu
        pas_De_Gagnant = False
        continue
    
    colonne_Valide = False
    while not colonne_Valide : # 3 - Je teste si le joueur à bien rentrée une colonne valide
        if est_Entier(input_Colonne) : # 3.1 - Test si c'est un entier, si oui je convertis en int et je passe à la suite
            input_Colonne = int(input_Colonne)
            if input_Colonne <= puissanceN.get_Largeur() and input_Colonne >= 1 : # 3.2 - Test si c'est un entier compris entre les colonnes du tableau
                if puissanceN.placer_Pion(joueur_Actuel, input_Colonne) : # 3.3 - Test si il y a assez de place pour placer un pion dans la colonne
                    colonne_Valide =  True # Si oui, je sors de la boucle (placer_Pion à déjà placé le pion si il renvoie True)
                else :
                    input_Colonne = input(">>> ") # 4 - Si jamais une des conditions est fausse, je redemande une valeur et recommence toute les verifications avec la nouvelle valeur
                    continue
            else: 
                input_Colonne = input(">>> ")
                continue
        else :
            input_Colonne = input(">>> ")
            continue
    
    if puissanceN.grille_Pleine() : # 5 - Test si la grille est pleine 
        pas_De_Gagnant = False # Si oui, j'arrête le jeu et affiche la grille une dernière fois pour voir le résultat
        puissanceN.afficher_Grille()

    incrementeur += 1 
print("Partie terminée !")
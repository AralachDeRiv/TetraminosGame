# Jeux sans les flèches 
from tetraclass import *
from tetrascena import *
import sys
import os
import datetime


if len(sys.argv) != 2:
      print("Veuillez fournir le nom d'un fichier 'carte_X.txt' existant en argument.")
      sys.exit()
else:
    file_name = sys.argv[1]



# on clean avant la partie 
cleaner()

# scenario début 
text_scrolling(beginning)
cleaner()

# set up
dimension, tetraminos = import_card(file_name)
setup_tetraminos(tetraminos, dimension)
grid = create_grid(dimension[0],dimension[1])
print_grid(grid, tetraminos)


# création d'un minuteur
duree = datetime.timedelta(minutes=5)
debut = datetime.datetime.now()


continuer = True
win = False

while continuer:

    # Vérification du minuteur
    temps_ecoule = datetime.datetime.now() - debut
    temps_restant = duree - temps_ecoule

    # Met à 0 si temps restant en dessous
    if temps_restant.total_seconds() <= 0: 
        temps_restant = datetime.timedelta(seconds=0)

    print(f"Temps restant : {temps_restant.seconds}s")
    # Sort de la boucle en cas d'explosion
    if temps_ecoule >= duree:
        break
    


    reponse = input("Voulez-vous continuer? O/N ")
    match reponse.lower():
        case 'n':
            continuer = False
            break
        case _:
            print("On continue !!")
    
    ok = False
    while not ok:
        piece = input("Quelle piece voulez-vous déplacer/tourner? ")
        try :
            numero = int(piece)
            if not 0 < numero <= len(tetraminos):
                raise ValueError
        except ValueError:
            print("Il nous faut un numéro de pièce!")
        else :
            ok = True
    
    ok_bis = False
    while not ok_bis:
        positions_initiales = tetraminos[numero-1][0][:]
        decalage_initial = tetraminos[numero-1][2][:]
    
        action = input("Déplacement Horizontal/Vertical ou Rotation Horloger/Antihorloger ? H/V/O/U ")
        match action.lower():
            case ('h'|'v'):
                deplacement = input("De combien? ")
                try :
                    deplacement = int(deplacement)
                except ValueError :
                    print("If faut un nombre positif ou négatif !")
                else :
                    if action.lower() == 'h':
                        place_tetramino(tetraminos[numero-1],deplacement, grid)
                    else :
                        place_tetramino(tetraminos[numero-1],deplacement, grid, horizontal=False)                               
            case 'o':
                rotate_tetramino(tetraminos[numero-1], grid)               
            case 'u':
                rotate_tetramino(tetraminos[numero-1], grid, clockwise=False)
            case _ :
                print("Cette commande n'est pas conforme")
        # on vérifie qu'une action a bien été effectuée
        if positions_initiales != tetraminos[numero-1][0] or decalage_initial != tetraminos[numero-1][2] :
            ok_bis = True

    
    # on clean l'écran et les interactions précédentes
    cleaner()
        

    # On réinitialise la carte
    grid = create_grid(dimension[0],dimension[1])
    # On la print avec les changements qui ont été effectués sur les tetraminos
    print_grid(grid, tetraminos)

    if check_win(dimension, grid):
        win = True
        continuer = False
        break


if win :
    print("Hourra !")
    input()
    cleaner()
    text_scrolling(win_end)
else : 
    print("Nooooon !")
    input()
    cleaner()
    text_scrolling(loose_end)




              
     
         

    


              


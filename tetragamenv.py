# py tetragamenv.py carte_1.txt
from tetraclass import *
from tetrascena import *
import sys
import os
import datetime
# Attention : importer module
import keyboard



if len(sys.argv) != 2:
      print("Veuillez fournir le nom d'un fichier 'carte_X.txt' existant en argument.")
      sys.exit()
else:
    file_name = sys.argv[1]



# on clean avant la partie 
cleaner()

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
        piece = tetraminos[numero-1]

        # !! pour claviers config en français
        action = keyboard.read_event(suppress=True)
        if action.event_type == keyboard.KEY_DOWN:
            match action.name:
                case "haut" | "up" :
                    place_tetramino(piece, 1, grid, horizontal=False)
                case "bas" | "down":
                    place_tetramino(piece, -1, grid, horizontal=False)
                case "droite" | "right":
                    place_tetramino(piece, 1, grid, horizontal=True)
                case "gauche" | "left":
                    place_tetramino(piece, -1, grid, horizontal=True)
                case "o":
                    rotate_tetramino(piece, grid)
                case "u":
                    rotate_tetramino(piece, grid, tetraminos, clockwise=False)
                case "enter":
                    ok_bis = True

        cleaner()
        grid = create_grid(dimension[0], dimension[1])
        print_grid(grid, tetraminos)



    if check_win(dimension, grid):
        win = True
        continuer = False
        break


if win :
    print("Hourra !")
    cleaner()
    text_scrolling(win_end)

else : 
    print("Nooooon !")
    cleaner()
    text_scrolling(loose_end)



# TetraminosGame

[Français](#version-française) | [English](#english-version)

## English Version

## Description

_TetraminosGame is a project inspired by an exercise given to computer science students at ULB. Entirely coded in Python, it is played directly in the terminal. This project represents my first programming accomplishment, completed in November 2023 when I was not yet working in this field. The game is available only in French._

## Launching the Game

To launch the game, open the terminal, navigate to the folder containing the files, and type one of the following commands:

```bash
python3 tetragamenv.py carte_1.txt
python3 tetragame.py carte_1.txt
```

- **tetragamenv.py**: Use this command to play with the arrow keys (requires importing the `keyboard` module).

- **tetragame.py**: This version does not use the arrow keys; movements are made by following the dialogues and using the number keys.

- `carte_1.txt` corresponds to the game board you wish to use.

## Gameplay

Once the game starts, after a brief introduction, you will see this board:

![board](board.png)

Between each round, a timer appears to show the remaining time. The goal is to place all the pieces in the central rectangle.

### Controls

- **Movement**: Use the arrow keys or follow the dialogues for movement.
- **Rotation**: Press the `o` and `u` keys to rotate the pieces.
- **Validation**: Press `Enter` to confirm the piece's placement.

Depending on the player's success or failure, a different ending will be presented.

## Creating Your Own Boards

The text file is structured as follows:

```txt
5, 4
(0, 0);(0, 1);(0, 2);(1, 1);;0;37;43
(0, 0);(0, 1);(0, 2);;0;37;41
(1, 0);(1, 1);(0, 1);(0, 2);;0;37;45
(0, 0);;0;37;46
(0, 0);(1, 0);(1, 1);;0;37;42
(0, 0);(1, 0);(2, 0);(2, 1);(2, 2);;0;37;44
```

- The first line indicates the dimensions of the central square: `5` is the width and `4` is the height.
- Each subsequent line represents a piece:
  - `(0, 0);(0, 1);(0, 2);(1, 1)` defines the shape of the piece.
  - `0;37;43` corresponds to its color in RGB code.

A maximum of 8 pieces can be used.

## Version Française

## Description

_TetraminosGame est un projet inspiré d'un exercice proposé aux étudiants en informatique de l'ULB. Entièrement codé en Python, il se joue directement dans le terminal. Ce projet représente ma première réalisation en programmation, effectuée en novembre 2023 alors que je n'étais pas encore dans ce secteur._

## Lancement du jeu

Pour lancer le jeu, ouvrez le terminal, naviguez vers le dossier contenant les fichiers, puis tapez l'une des commandes suivantes :

```bash
python3 tetragamenv.py carte_1.txt
python3 tetragame.py carte_1.txt
```

- **tetragamenv.py** : Utilisez cette commande pour jouer avec les flèches directionnelles (nécessite l'importation du module `keyboard`).
- **tetragame.py** : Cette version n'utilise pas les flèches ; les déplacements se font en suivant les dialogues et en utilisant les chiffres.

- `carte_1.txt` correspond au plateau de jeu que vous souhaitez utiliser.

## Gameplay

Une fois le jeu lancé, après un petit préambule, vous verrez ce tableau :

![board](board.png)

Entre chaque tour, un minuteur s'affiche pour montrer le temps restant. Le but est de placer toutes les pièces dans le rectangle central.

### Commandes

- **Déplacement** : Utilisez les flèches directionnelles ou suivez les dialogues pour les déplacements.
- **Rotation** : Appuyez sur les touches `o` et `u` pour faire pivoter les pièces.
- **Validation** : Appuyez sur `Entrée` pour valider l'emplacement de la pièce.

En fonction de la réussite ou de l'échec du joueur, une fin différente sera proposée.

## Création de vos propres cartes

Le fichier texte se présente comme suit :

```txt
5, 4
(0, 0);(0, 1);(0, 2);(1, 1);;0;37;43
(0, 0);(0, 1);(0, 2);;0;37;41
(1, 0);(1, 1);(0, 1);(0, 2);;0;37;45
(0, 0);;0;37;46
(0, 0);(1, 0);(1, 1);;0;37;42
(0, 0);(1, 0);(2, 0);(2, 1);(2, 2);;0;37;44
```

- La première ligne indique les dimensions du carré central : `5` est la largeur et `4` la hauteur.
- Chaque ligne suivante représente une pièce :
  - `(0, 0);(0, 1);(0, 2);(1, 1)` définit la forme de la pièce.
  - `0;37;43` correspond à sa couleur en code RGB.

Il n'est possible de disposer que de 8 pièces.

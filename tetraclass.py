
def cleaner():
    import os
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')




def create_grid(w: int, h: int):
    grid = [["  " for _ in range(3*w+2)] for _ in range(3*h+2)]
    for i, x in enumerate(grid):
        # pour les bords
        x[0] = "| "
        x[-1] = " |"
        # la partie haute et basse du centre
        if i == h or i == h*2+1:
            for n in range(w+1, w*2+1):
                x[n] = "--"
        # les bords du centre
        if i in range(h+1, 2*h+1):
            x[w] = " |"
            x[2*w+1] = "| "
    return grid


def import_card(file_path: str):
    with open(file_path, 'r') as file:
        content = file.readlines()
        dimensions = tuple(int(x) for x in content[0].split(","))
        tetraminos = []
        for x in content[1:]:
            x = x.split(";;")
            positions = [tuple(int(i) for i in pair.strip('()').split(',')) for pair in x[0].split(';')]
            color = x[1].strip()
            tetraminos.append([positions,color])
    return dimensions, tetraminos


def setup_tetraminos(tetraminos: list, dimension: tuple):
    for numero, piece in enumerate(tetraminos, start=1):
        decalage = [0,1]
        if numero in (2,7):
            decalage[1] = dimension[0] + 1
        if numero in (3,5,8):
            decalage[1] = dimension[0]*2 + 2
        if numero in (4,5):
            decalage[0] = dimension[1] + 1
        if numero in (6,7,8):
            decalage[0] = dimension[1]*2 + 2
        piece.append(decalage)
    
    return tetraminos    


def print_grid(grid: list, tetraminos: list, no_number = False):
    for num, piece in enumerate(tetraminos, start=1):
        for a,b in piece[0]:
            decalage = piece[2]
            couleur = piece[1]
            # si la place est déjà occupée
            if grid[a+decalage[0]][b+decalage[1]] not in ("  ","| "," |","--"):
                # on montre que 2 ou plusieurs pieces se superposent
                grid[a+decalage[0]][b+decalage[1]] = "\x1b[0;37;41mX \x1b[0m"
            else :
                grid[a+decalage[0]][b+decalage[1]] = f"\x1b[{couleur}m{num if not no_number else ' '} \x1b[0m"
    
    for x in grid:
        print(''.join(x))


def check_move(piece : list, grid : list) -> bool:
    
    decalage = piece[2]
    for a,b in piece[0]:
        if not 0 <= a+decalage[0] < len(grid) or not 0 <= b+decalage[1] < len(grid[0]):
            return False     
    return True


def place_tetramino(piece:list, deplacement:int, grid:list, horizontal=True):
    decalage_initial = piece[2][:]
    if horizontal :
        piece[2][1] += deplacement
    # déplacement vertical
    if horizontal == False:
        piece[2][0] += -deplacement
    
    if check_move(piece, grid) == False:
        piece[2] = decalage_initial
        print("Deplacement impossible !!!")

    
def rotate_tetramino(piece, grid, clockwise=True,):
    positions_initiales = piece[0][:]
    nouvelles_positions = []
    
    if clockwise :
        nouvelles_positions = [(b,-a) for (a,b) in piece[0]]
    if clockwise == False:
        nouvelles_positions = [(-b,a) for (a,b) in piece[0]]
        
    piece[0] = nouvelles_positions
    
    if check_move(piece, grid) == False:
        piece[0] = positions_initiales
        print("Rotation impossible !!!")


def check_win(dimension: tuple, grid: list):
    positions = []
    for n in range(dimension[1]):
        a = dimension[1] + 1
        a += n
        for n in range(dimension[0]):
            b = dimension[0] + 1
            b += n
            positions.append((a, b))
    
    for a,b in positions:
        if grid[a][b] in ("  ","| "," |","--", "\x1b[0;37;41mX \x1b[0m"):
            return False
    return True










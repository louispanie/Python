from random import randint
import time
computersameguess=False
orientationsave="hi"
justmissed=False

def justmiss():
        if orientationsave== orientation_list[0]:
                orientation = orientation_listright[randint(0, 2)]
                justhit2()
        elif orientationsave== orientation_list[1]:
                orientation = orientation_listleft[randint(0, 2)]
                justhit2()
        elif orientationsave== orientation_list[2]:
                orientation = orientation_listup[randint(0, 2)]
                justhit2()
        elif orientationsave== orientation_list[3]:
                orientation = orientation_listdown[randint(0, 2)]
                justhit2()

def justhit2():
    if orientation == "right":
        if board[y_axis][x_axis + 1] == "X":
            print("Oh Oh... Your ship got hit!🔥")
            hitscomputer += 1
            shiphit = True
            board[y_axis][x_axis + 1]="H"
            orientationsave="left"
            justmissed=False
        else:
            print("Phew,😅, it missed.")
            justmissed=True
    elif orientation == "left":
        if board[y_axis][x_axis - 1] == "X":
            print("Oh Oh... Your ship got hit!🔥")
            hitscomputer += 1
            shiphit = True
            board[y_axis][x_axis - 1]="H"
            orientationsave="left"
            justmissed=False
        else:
            print("Phew,😅, it missed.")
            justmissed=True
    elif orientation == "up":
        if board[y_axis-1][x_axis] == "X":
            print("Oh Oh... Your ship got hit!🔥")
            hitscomputer += 1
            shiphit = True
            board[y_axis-1][x_axis]="H"
            orientationsave="up"
            justmissed=False
        else:
            print("Phew,😅, it missed.")
            justmissed=True
    elif orientation == "down":
        if board[y_axis+1][x_axis] == "X":
            print("Oh Oh... Your ship got hit!🔥")
            hitscomputer += 1
            shiphit = True
            board[y_axis+1][x_axis]="H"
            orientationsave="down"
            justmissed=False
        else:
            print("Phew,😅, it missed.")
            justmissed=True

def safe_input(board, x_axis, y_axis, length_ship, orientation):
    try:
        if orientation == "right":
            if x_axis + length_ship - 1 > 10:
                return False
            for i in range(length_ship):
                if board[y_axis][x_axis + i] != "O":
                    return False

        elif orientation == "left":
            if x_axis - length_ship + 1 < 1:
                return False
            for i in range(length_ship):
                if board[y_axis][x_axis - i] != "O":
                    return False

        elif orientation == "up":
            if y_axis - length_ship + 1 < 1:
                return False
            for i in range(length_ship):
                if board[y_axis - i][x_axis] != "O":
                    return False

        elif orientation == "down":
            if y_axis + length_ship - 1 > 10:
                return False
            for i in range(length_ship):
                if board[y_axis + i][x_axis] != "O":
                    return False

        return True
    except IndexError:
        return False


def place_ship(board, x_axis, y_axis, length_ship, orientation):
    if orientation == "right":
        for a in range(length_ship):
            board[y_axis][x_axis + a] = "X"
    elif orientation == "left":
        for b in range(length_ship):
            board[y_axis][x_axis - b] = "X"
    elif orientation == "up":
        for c in range(length_ship):
            board[y_axis - c][x_axis] = "X"
    elif orientation == "down":
        for d in range(length_ship):
            board[y_axis + d][x_axis] = "X"


board = [
    ["O", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    ["A", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["D", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["F", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["G", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["H", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["I", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["J", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
]


def printboard():
    for a in range(11):
        for b in range(11):
            print(board[a][b], end=" ")
        print()


def printcomputerboard():
    for f in range(11):
        for g in range(11):
            print(computerboard[f][g], end=" ")
        print()


printboard()

# player board
shipplacing=0
ships=[2,2,3,4,5]
while shipplacing!=5:
    print("Choose the size of your ship, then choose the starting points (x-axis, y-axis), then the orientation.")
    print("These are the available ship sizes", ships)
    length_ship=int(input())
    x_axis=int(input())
    y_axis=int(input())

    # y_axis=ord(y_axis)
    # y_axis=y_axis-64

    orientation=str(input())

    for a in range(length_ship):
        if board[y_axis][x_axis]=="O":
            if orientation=="right" and board[y_axis][x_axis+a]=="O":
                for b in range(length_ship):
                    board[y_axis][x_axis+b]="X"
                ships.remove(length_ship)
                shipplacing+=1
            elif orientation=="left" and board[y_axis][x_axis-a]=="O":
                for c in range(length_ship):
                    board[y_axis][x_axis-c]="X"
                ships.remove(length_ship)
                shipplacing+=1
            elif orientation=="up" and board[y_axis-a][x_axis]=="O":
                for d in range(length_ship):
                    board[y_axis-d][x_axis]="X"
                ships.remove(length_ship)
                shipplacing+=1
            elif orientation=="down" and board[y_axis+a][x_axis]=="O":
                for e in range(length_ship):
                    board[y_axis+e][x_axis]="X"
                ships.remove(length_ship)
                shipplacing+=1
    printboard()

# #computer placing

computerboard = [
    ["O", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    ["A", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["D", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["F", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["G", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["H", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["I", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["J", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
]

orientation_list = ["right", "left", "up", "down"]
orientation_listright = ["left", "up", "down"]
orientation_listleft = ["right", "up", "down"]
orientation_listup = ["left", "right", "down"]
orientation_listdown = ["left", "up", "right"]

shipscomputer = [2, 2, 3, 4, 5]

shipscounter = 4
shipplacing = 0
while shipplacing != 5:
    orientation = orientation_list[randint(0, 3)]
    length_ship = shipscomputer[randint(0, shipscounter)]

    x_axis = randint(1, 10)
    y_axis = randint(1, 10)

    if safe_input(computerboard, x_axis, y_axis, length_ship, orientation):
        place_ship(computerboard, x_axis, y_axis, length_ship, orientation)
        shipscomputer.remove(length_ship)
        shipplacing += 1
        shipscounter -= 1
shiphit = False
hits = 0
hitscomputer = 0
gameon = True
# game human
while gameon == True:
    if hits == 16:
        print("You won, good job. 🎈🥳🥳🎂🎉🎉🎉🎂🥳🥳🎈")
        gameon = False
    print("Write the x coordinates to where you want to shoot.")
    x_axis = int(input())
    print("Write the y coordinates to where you want to shoot.")
    y_axis = int(input())

    if computerboard[y_axis][x_axis] == "X":
        print("💥You hit an ennemy ship💥")
        hits += 1
        board[y_axis][x_axis] = "B"
    elif computerboard[y_axis][x_axis] == "O":
        print("You missed!")
        if board[y_axis][x_axis] != "X":
            board[y_axis][x_axis] = "0"

    time.sleep(2)

    print("Now the computer is going to shoot!!")
    if justmissed==False:
        if shiphit == False:
            x_axis = randint(1, 10)
            y_axis = randint(1, 10)

            computersameguess=False

            time.sleep(1)
            while computersameguess==False:
                if computerboard[y_axis][x_axis] == "0":
                    x_axis = randint(1, 10)
                    y_axis = randint(1, 10)
                elif computerboard[y_axis][x_axis] != "0":
                    computersameguess=True

            if board[y_axis][x_axis] == "X":
                print("Oh Oh... Your ship got hit!🔥")
                board[y_axis][x_axis] ="H"
                hitscomputer += 1
                shiphit = True
                justmissed=False
            else:
                print("Phew,😅, it missed.")
                shiphit = False
                justmissed=False
                if computerboard[y_axis][x_axis] !="X":
                    computerboard[y_axis][x_axis] = "0"

        elif shiphit == True:
            orientation = orientation_list[randint(0, 3)]
            justhit2()
        time.sleep(1.5)
    elif justmissed==True:
        justmiss()
    printboard()
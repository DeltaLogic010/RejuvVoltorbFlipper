#############################
### Written by DeltaLogic ###
#############################
import time
import keyboard
import pyautogui
import win32api
import win32con
from tabulate import tabulate

# PixelCalc
# +row = +96y
# +2nd number = +24x
# Voltorb num = +24x, +39y
# pixel = +2 direction
stage = []
points = []
position = [1, 1]
voltsum = 0
play = True
play2 = True
possible = []
gamesplayed = 0
wins = 0
losses = 0
level = 1


def initialise():
    global stage
    global points
    global position
    global voltsum
    global possible
    global play2
    stage = []
    points = []
    position = [1, 1]
    voltsum = 0
    possible = []
    play2 = True


# reads in the values of the points and bombs in each column and row by checking certain pixels
def numb(x_val, y_val):
    # print(x_val, y_val)
    # print(pyautogui.pixel(x_val, y_val+10))
    if pyautogui.pixelMatchesColor(x=x_val + 3, y=y_val + 12, expectedRGBColor=(66, 66, 66)):
        if pyautogui.pixelMatchesColor(x=x_val + 6, y=y_val + 9, expectedRGBColor=(66, 66, 66)):
            if not pyautogui.pixelMatchesColor(x=x_val, y=y_val + 15, expectedRGBColor=(66, 66, 66)):
                return 9
            elif not pyautogui.pixelMatchesColor(x=x_val + 12, y=y_val + 6, expectedRGBColor=(66, 66, 66)):
                return 6
            else:
                return 8
        else:
            if pyautogui.pixelMatchesColor(x=x_val, y=y_val, expectedRGBColor=(66, 66, 66)):
                return 4
            else:
                return 0
    else:
        if pyautogui.pixelMatchesColor(x=x_val, y=y_val, expectedRGBColor=(66, 66, 66)):
            if pyautogui.pixelMatchesColor(x=x_val, y=y_val + 9, expectedRGBColor=(66, 66, 66)):
                return 5
            else:
                return 7
        else:
            if pyautogui.pixelMatchesColor(x=x_val, y=y_val + 3, expectedRGBColor=(66, 66, 66)):
                if pyautogui.pixelMatchesColor(x=x_val, y=y_val + 15, expectedRGBColor=(66, 66, 66)):
                    return 3
                else:
                    return 2
            else:
                return 1


# a function to tell the function above which spots to read
def pixelnum(row, col):
    if row in [1, 2, 3, 4, 5]:
        x_val = 1288
        y_val = 265 + 96 * (row - 1)
    else:
        x_val = 808 + 96 * (col - 1)
        y_val = 746
    return [(numb(x_val, y_val)) * 10 + (numb(x_val + 24, y_val)), numb(x_val + 24, y_val + 39)]


# reads an input from the board to see the numbers on the cards
def smallnum(row, col):
    x_val = 808 + 96 * (col - 1)
    y_val = 288 + 96 * (row - 1)
    if pyautogui.pixelMatchesColor(x=x_val, y=y_val, expectedRGBColor=(24, 132, 99)):
        return
    elif pyautogui.pixelMatchesColor(x=x_val, y=y_val, expectedRGBColor=(255, 206, 49)):
        return 'o'
    elif pyautogui.pixelMatchesColor(x=x_val, y=y_val, expectedRGBColor=(231, 115, 82)):
        return 'O'
    else:
        if pyautogui.pixelMatchesColor(x=x_val + 6, y=y_val + 8, expectedRGBColor=(66, 66, 66)):
            return 1
        elif pyautogui.pixelMatchesColor(x=x_val, y=y_val + 13, expectedRGBColor=(165, 181, 173)):
            return 2
        elif pyautogui.pixelMatchesColor(x=x_val, y=y_val + 13, expectedRGBColor=(255, 255, 255)):
            return 3
        else:
            return None


# note the safe spots as 'S'
def safespots():
    global stage
    for i in range(5):
        if stage[i][5][1] == 0:
            for j in range(5):
                if stage[i][j][0] is None:
                    stage[i][j] = ['S']

    for i in range(5):
        if stage[5][i][1] == 0:
            for j in range(5):
                if stage[j][i][0] is None:
                    stage[j][i] = ['S']


# note all the cards which aren't worth flipping over with 'o'
def notworth():
    global stage
    for i in range(5):
        sum_ = 0
        for k in range(5):
            if stage[i][k][0] == 2 or stage[i][k][0] == 3:
                sum_ = sum_ + stage[i][k][0] - 1
        if stage[i][5][0] + stage[i][5][1] - sum_ == 5:
            for j in range(5):
                if stage[i][j][0] is None:
                    stage[i][j] = ['o']
    for i in range(5):
        sum_ = 0
        for k in range(5):
            if stage[k][i][0] == 2 or stage[k][i][0] == 3:
                sum_ = sum_ + stage[k][i][0] - 1
        if stage[5][i][0] + stage[5][i][1] - sum_ == 5:
            for j in range(5):
                if stage[j][i][0] is None:
                    stage[j][i] = ['o']


# Sets the Stage <3
def setthestage():
    global stage
    global points
    stage = [[[smallnum(1, 1)], [smallnum(1, 2)], [smallnum(1, 3)], [smallnum(1, 4)], [smallnum(1, 5)], pixelnum(1, 1)],
             [[smallnum(2, 1)], [smallnum(2, 2)], [smallnum(2, 3)], [smallnum(2, 4)], [smallnum(2, 5)], pixelnum(2, 1)],
             [[smallnum(3, 1)], [smallnum(3, 2)], [smallnum(3, 3)], [smallnum(3, 4)], [smallnum(3, 5)], pixelnum(3, 1)],
             [[smallnum(4, 1)], [smallnum(4, 2)], [smallnum(4, 3)], [smallnum(4, 4)], [smallnum(4, 5)], pixelnum(4, 1)],
             [[smallnum(5, 1)], [smallnum(5, 2)], [smallnum(5, 3)], [smallnum(5, 4)], [smallnum(5, 5)], pixelnum(5, 1)],
             [pixelnum(6, 1), pixelnum(6, 2), pixelnum(6, 3), pixelnum(6, 4), pixelnum(6, 5), []]]
    notworth()


# moves the selector to a given card
def moveto(x, y):
    global play
    if play == True:
        time.sleep(0.5)
        global position
        win32api.SetCursorPos((827, 234))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 827, 234, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 827, 234, 0, 0)
        for i in range((x - position[0]) % 5):
            time.sleep(0.1)
            keyboard.press("right")
            time.sleep(0.1)
            keyboard.release("right")
        for i in range((y - position[1]) % 5):
            time.sleep(0.1)
            keyboard.press("down")
            time.sleep(0.1)
            keyboard.release("down")
        position = [x, y]


# presses the space button, easy!
def space():
    global play
    if play == True:
        keyboard.press("spacebar")
        time.sleep(0.1)
        keyboard.release("spacebar")


# plays all the safe spots worth playing
def playsafe():
    global stage
    global position
    for i in range(5):
        for j in range(5):
            if stage[i][j][0] == 'S':
                moveto(j + 1, i + 1)
                space()
                time.sleep(0.5)
                # print(stage[i][j])
                # print(position[1])
                # print(position[0])
                # print(smallnum(position[1], position[0]))
                stage[i][j] = [smallnum(position[1], position[0])]
                # print(tabulate(stage))
    if position != [1, 1]:
        moveto(1, 1)


# finds the index of the next best spot once all the safe spots are done
def findidx(x):
    minbomb = 100
    maxbomb = 0
    minidx = []
    maxidx = []
    for i in range(5):
        for j in range(5):
            try:
                if x[j][i][1] == minbomb:
                    minidx.append([j, i])
                    minbomb = x[j][i][1]
                elif x[j][i][1] < minbomb:
                    minidx = [[j, i]]
                    minbomb = x[j][i][1]
            except:
                continue
    # print(minidx)
    for k in minidx:
        # print(x[k[0]][k[1]])
        if x[k[0]][k[1]][0] > maxbomb:
            maxbomb = x[k[0]][k[1]][0]
            maxidx = k
    return maxidx


# The risktaker program *puts on shades*
# I realise the above comment is not useful; This kicks off the processing of the board.
def risktaker():
    global stage
    global position
    global possible
    # print(tabulate(probs2))
    # print(len(possible))
    substage = [[[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []]]
    for i in range(5):
        for j in range(5):
            if stage[j][i][0] is None:
                xnonecount = 0
                ynonecount = 0
                for k in range(5):
                    if k != i and stage[j][k][0] is None:
                        ynonecount += 1
                    if k != j and stage[k][i][0] is None:
                        xnonecount += 1
                if xnonecount == 0 or ynonecount == 0:
                    # spot is safe
                    remposs(i, j)
    probs2 = probs(possible)
    for i in range(5):
        for j in range(5):
            if stage[j][i][0] is None:
                substage[j][i] = [(stage[j][5][0] + stage[5][i][0]),
                                  round(100 * probs2[j][i] / len(possible), 1)]
    # print(tabulate(substage))
    idx = findidx(substage)
    try:
        moveto(idx[1] + 1, idx[0] + 1)
    except:
        # print(tabulate(stage))
        # print('idx: ' + str(idx))
        # print('position: ' + str(position))
        # print('Done!')
        exit()
    space()


# This returns a list of all the possible board simulations with the same number of voltorbs.
def thepossy():
    global stage
    global voltsum
    volts()
    with open('Board_Data/AllPoss' + str(voltsum - 1) + '.txt') as f:
        poss = f.readlines()
        for i in range(5):
            poss_temp = []
            for line in poss:
                if int(line[77 + (i * 3)]) == stage[i][5][1]:
                    poss_temp.append(line)
            poss = poss_temp
        for i in range(5):
            poss_temp = []
            for line in poss:
                if int(line[92 + (i * 3)]) == stage[5][i][1]:
                    poss_temp.append(line)
            poss = poss_temp
    return poss


def remposs(x, y):
    global possible
    new_poss = []
    for line in possible:
        if int(line[1 + (3 * x) + (15 * y)]) == 0:
            new_poss.append(line)
    possible = new_poss
    # print('len(poss): ' + str(len(possible)))


def probs(poss):
    subspace = [0] * 25
    for i in range(25):
        subspace[i] = sum(int(poss[j][1 + (i * 3)]) for j in range(len(poss)))
    return nest_list(subspace, 5, 5)


def nest_list(list1, rows, columns):
    result = []
    start = 0
    end = columns
    for i in range(rows):
        result.append(list1[start:end])
        start += columns
        end += columns
    return result


def checkpos():
    global position
    global stage
    global possible
    time.sleep(0.5)
    x, y = position[0], position[1]
    time.sleep(0.1)
    z = smallnum(y, x)
    # print('x: ' + str(x) + ', y: ' + str(y) + ', z: ' + str(z))
    if z == 1 or z == 2 or z == 3:
        stage[y - 1][x - 1] = [z]
        remposs(x - 1, y - 1)
        # print(tabulate(probs(possible)))
    elif z == 'O':
        # print(z)
        # print(tabulate(probs(possible)))
        # print(tabulate(stage))
        cont('L')


def newposs():
    global stage
    for i in range(5):
        for j in range(5):
            if stage[i][j] == [1] or stage[i][j] == [2] or stage[i][j] == [3]:
                remposs(j, i)


def cont(state):
    global stage
    global voltsum
    global play2
    global wins
    global losses
    global level
    if state == 'W':
        # print('Win!')
        wins += 1
        level += 1
        time.sleep(4)
        # print('space 1')
        space()
        time.sleep(2)
        # print('space 2')
        space()
        time.sleep(2)
        # print('space 3')
        space()
        time.sleep(1)
    else:
        losses += 1
        flipcount = 0
        for i in range(5):
            for j in range(5):
                if stage[j][i][0] == 2 or stage[j][i][0] == 3:
                    flipcount += 1
        # print('flipcount: ' + str(flipcount) + ', voltsum: ' + str(voltsum))
        if flipcount >= (voltsum - 5):
            # print('Lose, no drop')
            time.sleep(4)
            # print('space 1')
            space()
            time.sleep(1)
        else:
            # print('Lose, drop to level ' + str(flipcount))
            level = flipcount
            time.sleep(4)
            # print('space 1')
            space()
            time.sleep(2)
            # print('space 2')
            space()
            time.sleep(1)
        play2 = False


def volts():
    global voltsum
    voltsum = sum(stage[i][5][1] for i in range(5))


# deep breath...
def letsplay():
    global possible
    global play2
    initialise()
    # ...set the stage...
    setthestage()
    # ...locate the safe zones...
    safespots()
    # ...reveal  your secrets...
    # print(tabulate(stage))
    # ...start safe and steady...
    playsafe()

    possible = thepossy()

    while play2:
        # ...roll the die...
        if pyautogui.pixelMatchesColor(x=1300, y=770, expectedRGBColor=(41, 165, 107)):
            notworth()
            risktaker()
            checkpos()
        else:
            cont('W')
            break


while True:
    # print('---------------')
    # if gamesplayed == 0:
    #     level = 1
    # # print('Level: ' + str(level))
    letsplay()
    gamesplayed += 1
    # print('Games played: ' + str(gamesplayed))
    # if gamesplayed % 10 == 0:
    #     print('Games Won: ' + str(wins) + ', Games Lost' + str(losses))

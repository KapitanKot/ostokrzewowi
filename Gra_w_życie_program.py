import os #pygame
#from pygame.locals import *

#pygame.init()

#--okno--
okno_szerokosc = 100
okno_wysokosc = 100
#window = pygame.display.set_mode((okno_szerokosc, okno_wysokosc))

#--plansza--
x = int(okno_szerokosc/5)
y = int(okno_wysokosc/5)
plansza = [0] * x
for i in range(x):
    plansza[i] = [0] * y

#--wybor komorek--


#--zycie--
def symulacja(staraGeneracja):
    
    nowaGeneracja = [0] * x
    for i in range(x):
        nowaGeneracja[i] = [0] * y

    for i in range(x):
        for j in range(y):
            
            sasiad = 0
            #--wiersz 1--
            try:
                if staraGeneracja[i-1][j-1] == 1: sasiad += 1
            except IndexError:pass
            try:
                if staraGeneracja[i][j-1] == 1: sasiad += 1
            except IndexError:pass
            try:
                if staraGeneracja[i+1][j-1] == 1: sasiad += 1
            except IndexError:pass
            #--wiersz 2--
            try:
                if staraGeneracja[i-1][j] == 1: sasiad += 1
            except IndexError:pass
            try:
                if staraGeneracja[i+1][j] == 1: sasiad += 1
            except IndexError:pass
            #--wiersz 3--
            try:
                if staraGeneracja[i-1][j+1] == 1: sasiad += 1
            except IndexError:pass
            try:
                if staraGeneracja[i][j+1] == 1: sasiad += 1
            except IndexError:pass
            try:
                if staraGeneracja[i+1][j+1] == 1: sasiad += 1
            except IndexError:pass

            #--komorka umiera jesli ma mniej niz 2 lub wiecej niz 3 sasiadow
            if sasiad > 3 or sasiad < 2: nowaGeneracja[i][j] == 0
            #--komorka zyje dalej jesli ma 2 lub 3 sasiadow
            if sasiad == 2 and staraGeneracja[i][j] == 1: nowaGeneracja[x][y] == 1
            #--komorka ozywa gdy ma 3 sasiadow
            if sasiad == 3: nowaGeneracja[i][j] == 1    
    
    return nowaGeneracja

#--symuacja--
while True:
    print(symulacja(plansza))
    os.system('clear')

    
    

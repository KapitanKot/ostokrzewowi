import sys, pygame
from pygame.locals import *

pygame.init()

#--okno--
oknoSzerokosc = 400
oknoWysokosc = 400
okno = pygame.display.set_mode((oknoSzerokosc, oknoWysokosc))
pygame.display.set_caption('Gra w życie')

#--plansza--
r = 10
x = int(oknoSzerokosc/r)
y = int(oknoWysokosc/r)
plansza = [0] * x
for i in range(x):
    plansza[i] = [0] * y

#--pole gry--
def PoleGry():
    for j in range(y):
        for i in range(x):
            if plansza[i][j] == 1:
                pygame.draw.rect(okno, (255,255,255), (r*i, r*j, r, r),1)

#--zycie--
def Symulacja(staraGeneracja):
    
    nowaGeneracja = [0] * x
    for i in range(x):
        nowaGeneracja[i] = [0] * y

    for j in range(y):
        for i in range(x):
            
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
            if staraGeneracja[i][j] == 1 and (sasiad < 2 or sasiad > 3): nowaGeneracja[i][j] = 0
            #--komorka zyje dalej jesli ma 2 lub 3 sasiadow
            elif staraGeneracja[i][j] == 1 and (sasiad == 2 or sasiad == 3): nowaGeneracja[i][j] = 1
            #--komorka ozywa gdy ma 3 sasiadow
            elif staraGeneracja[i][j] == 0 and sasiad == 3: nowaGeneracja[i][j] = 1    
    
    return nowaGeneracja

#--symuacja--
zycieTrwa = False
while True:
    for event in pygame.event.get():

        #--wyjscie--
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #--rozpoczecie symulacji--
        if event.type == KEYDOWN and event.key == K_RETURN:
            zycieTrwa = True

        #--ozywienie komorki--
        if zycieTrwa == False:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mX, mY = pygame.mouse.get_pos()
                mX = int(mX//r)
                mY = int(mY//r)
                plansza[mX][mY] = 1
                pygame.draw.rect(okno, (255,255,255), (r*mX, r*mY, r, r),1)
                pygame.display.update()

        #--zabicie komorki--
        if zycieTrwa == False:
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                mX, mY = pygame.mouse.get_pos()
                mX = int(mX//r)
                mY = int(mY//r)
                plansza[mX][mY] = 0
                pygame.draw.rect(okno, (0,0,0), (r*mX, r*mY, r, r),1)
                pygame.display.update()

    if zycieTrwa == True:
        plansza = Symulacja(plansza)
        
        okno.fill((0,0,0))
        PoleGry()
        pygame.display.update()
        pygame.time.delay(100)

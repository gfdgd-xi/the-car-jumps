##########################
# 更新时间：2021年7月4日
# 作者：gfdgd xi
# 版本：1.0
#########################
#!/usr/bin/env python3
import os
import json
import sys
import time
import random
import pygame
#import winsound
import threading


def ExitProgram():
    global close
    close = True
    sys.exit(0)


def Up():
    global jumpTime
    global jumpTimes
    global over
    if over:
        return
    if jumpTime:
        return
    for i in range(4):
        carPlace[1] = carPlace[1] - 50
        time.sleep(0.01)
    jumpTime = True
    jumpTimes = jumpTimes + 1
    #winsound.Beep(600,1000)


def Down():
    global jumpTime
    global dolphinPlace
    global carLong
    global over
    while not close:
        time.sleep(0.01)
        if carPlace[1] >= 500 - int(1685 / 14):
            if (bigRoadPlace1[0] + 1141 >= carPlace[0] + carLong / 2) + (bigRoadPlace1[0] <= carPlace[0] + carLong / 2) == 2 or (bigRoadPlace2[0] + 1141 >= carPlace[0] + carLong / 2) + (bigRoadPlace2[0] <= carPlace[0] + carLong / 2) == 2 or (bigRoadPlace3[0] + 1141 >= carPlace[0] + carLong / 2) + (bigRoadPlace3[0] <= carPlace[0] + carLong / 2) == 2:
                jumpTime = False
                continue
        if carPlace[1] + carHeight / 2 > bigRoadPlace1[1]:
            over = True
            while not close:
                carPlace[1] = carPlace[1] + 5
                dolphinPlace = [1024 / 2 - int(2918 / 5) / 2, 720]
                time.sleep(0.01)
                if carPlace[1] > 768:
                    while not dolphinPlace[1] > 768:
                        dolphinPlace[1] = dolphinPlace[1] + 5
                        time.sleep(0.01)
                    break
            break
        carPlace[1] = carPlace[1] + 5

def RandomRoad():
    global smallRoad
    global bigRoad
    beautiful = random.randint(1, 6)
    if beautiful == 1:
        return pygame.transform.scale(bigRoad, (1141, 191))
    elif beautiful == 2:
        return pygame.transform.scale(smallRoad, (1141, int(191 / 2)))
    elif beautiful == 3:
        return pygame.transform.scale(bigRoad, (1141, int(191 / 2)))
    elif beautiful == 4:
        return pygame.transform.scale(smallRoad, (1141, int(191 / 4)))
    elif beautiful == 5:
        return pygame.transform.scale(bigRoad, (1141, int(191 / 4)))
    else:
        return pygame.transform.scale(smallRoad, (1141, 191))


def MoveRoad():
    global tips
    global suDu
    global background
    global suDuOld
    global second
    global minute
    global bigRoad1
    global bigRoad2
    global bigRoad3
    global bigRoadPlace1
    global bigRoadPlace2
    global bigRoadPlace3
    global treePlace
    global tipsPlace
    global tipsPicture
    global dolphinPicture
    while not close:
        bigRoadPlace1[0] = bigRoadPlace1[0] - suDu
        bigRoadPlace2[0] = bigRoadPlace2[0] - suDu
        bigRoadPlace3[0] = bigRoadPlace3[0] - suDu
        treePlace[0] = treePlace[0] - suDu
        tipsPlace[0] = tipsPlace[0] - suDu
        if bigRoadPlace1[0] < -1111 - random.randint(0, 900):
            bigRoadPlace1 = [0 + 1141 + 1141, 500]
            bigRoad1 = RandomRoad()
        if bigRoadPlace2[0] < -1111 - random.randint(0, 900):
            bigRoadPlace2 = [0 + 1141 + 1141, 500]
            bigRoad2 = RandomRoad()
        if bigRoadPlace3[0] < -1111 - random.randint(0, 900):
            bigRoadPlace3 = [0 + 1141 + 1141, 500]
            bigRoad3 = RandomRoad()
        elif suDuOld is not 10:
            suDu = 10
            suDuOld = suDu
        
        if int(second / 5) == second / 5:
            treePlace = [1024, 500 - int(2879 / 5) + 100]
        if int(minute / 5) == minute / 5 and second == 0 and minute > 0:
            tips = pygame.transform.scale(dolphinPicture, (450, 450))
            tipsPlace = [1024, 50]
        elif minute > 0 and second == 0:
            background = (random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
            tips = pygame.transform.scale(tipsPicture, (450, 450))
            tipsPlace = [1024, 50]
    
        if over:
            break
        time.sleep(0.01)


def Time():
    global second
    global minute
    global over
    global jumpTimes
    global textSurfaceObj2
    second = 0
    minute = 0
    while not close:
        second = second + 1
        if second >= 60:
            second = 0
            minute = minute + 1
        if second < 10:
            secondString = "0" + str(second)
        else:
            secondString = str(second)
        if minute < 10:
            minuteString = "0" + str(minute)
        else:
            minuteString = str(minute)
        if over:
            break
        if int(second / 2) == second / 2:
            dolphinPlace[1] = dolphinPlace[1] - 20
        else:
            dolphinPlace[1] = dolphinPlace[1] + 20
        textSurfaceObj2 = fontObj2.render("Time: {}:{};\nJump Time: {};\nNow: Play".format(
            minuteString, secondString, jumpTimes), False, (250, 250, 250))
        time.sleep(1)
    textSurfaceObj2 = fontObj2.render("Time: {}:{};\nJump Time: {};\nNow: Over".format(
        minuteString, secondString, jumpTimes), False, (250, 250, 250))

# 重启本应用程序


def ReStartProgram():
    python = sys.executable
    os.execl(python, python, * sys.argv)

pygame.init()
bigRoad = pygame.image.load("BigRoad.png")
smallRoad = pygame.image.load("SmallRoad.png")
tipsPicture = pygame.image.load("Tips.png")
sharpPicture = pygame.image.load("Sharp.png")
dolphinPicture = pygame.image.load("Dolphin.png")
bigRoad1 = pygame.transform.scale(
    bigRoad, (1141, 191))
bigRoad2 = pygame.transform.scale(
    smallRoad, (1141, int(191 / 2)))
bigRoad3 = pygame.transform.scale(
    smallRoad, (1141, 191))
car = pygame.transform.scale(pygame.image.load(
    "Car.png"), (int(2780 / 14), int(1685 / 14)))
tips = pygame.transform.scale(tipsPicture, (450, 450))
dolphin = pygame.transform.scale(sharpPicture, (int(2918 / 5), int(1202 / 5)))
tree = pygame.transform.scale(pygame.image.load("tree.png"), (int(1919 / 5), int(2879 / 5)))
#tree = pygame.transform.scale(pygame.image.load("tree.png"), (int(4734 / 10), int(4713 / 10)))
carLong = int(1685 / 14)
carHeight = int(2780 / 14)
bigRoadPlace1 = [0, 500]
bigRoadPlace2 = [0 + 1141, 500]
bigRoadPlace3 = [0 + 1141 + 1141, 500]
dolphinPlace = [1024 / 2 - int(2918 / 5) / 2, 720]
treePlace = [-1024, 500 - int(2879 / 10)]
carPlace = [1024 / 2 - 300 / 2, 500 - int(1685 / 14)]
tipsPlace = [1024 - 450, 50]
#background = (0, 100, 250)
background = (random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
pygame.display.set_caption("Demo")
#screen = pygame.display.set_mode((1024, 768))
screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN|pygame.HWSURFACE)
close = False
over = False
jumpTime = False
jumpTimes = 0
suDu = 5
suDuOld = suDu
start = False
fontObj2 = pygame.font.SysFont('宋体', 20)
textSurfaceObj2 = fontObj2.render(
    "Time: 0:0:0; Jump Time: 0; Now: play", False, (250, 250, 250))
textRectObj2 = textSurfaceObj2.get_rect()
threading.Thread(target=Down).start()
quickly = False
second = 0
minute = 0
while not close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ExitProgram()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                ExitProgram()
            if event.key == pygame.K_SPACE and not start:
                start = True
                threading.Thread(target=MoveRoad).start()
                threading.Thread(target=Time).start()
                continue
            if event.key == pygame.K_r:
                ReStartProgram()
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                threading.Thread(target=Up).start()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if quickly:
                    quickly = False
                    suDu = suDuOld
                else:
                    quickly = True
                    suDu = suDu * 2
    screen.fill(background)
    screen.blit(textSurfaceObj2, textRectObj2)
    screen.blit(dolphin, dolphinPlace)
    screen.blit(tree, treePlace)
    screen.blit(tips, tipsPlace)
    screen.blit(bigRoad1, bigRoadPlace1)
    screen.blit(bigRoad2, bigRoadPlace2)
    screen.blit(bigRoad3, bigRoadPlace3)
    screen.blit(car, carPlace)
    pygame.display.flip()

#tictactoe
import time
from colorama import Fore, Style
from z3 import parse_smt2_string
import pygame
pygame.mixer.init()

def draw_board(xstate,ystate):
    zero=f'{Fore.GREEN}X{Fore.RESET}' if xstate[0] else f'{Fore.RED}O{Fore.RESET}' if ystate[0] else 0
    one=f'{Fore.GREEN}X{Fore.RESET}' if xstate[1] else f'{Fore.RED}O{Fore.RESET}' if ystate[1] else 1
    two = f'{Fore.GREEN}X{Fore.RESET}' if xstate[2] else f'{Fore.RED}O{Fore.RESET}' if ystate[2] else 2
    three = f'{Fore.GREEN}X{Fore.RESET}' if xstate[3] else f'{Fore.RED}O{Fore.RESET}' if ystate[3] else 3
    four = f'{Fore.GREEN}X{Fore.RESET}' if xstate[4] else f'{Fore.RED}O{Fore.RESET}' if ystate[4] else 4
    five = f'{Fore.GREEN}X{Fore.RESET}' if xstate[5] else f'{Fore.RED}O{Fore.RESET}' if ystate[5] else 5
    six = f'{Fore.GREEN}X{Fore.RESET}' if xstate[6] else f'{Fore.RED}O{Fore.RESET}' if ystate[6] else 6
    seven = f'{Fore.GREEN}X{Fore.RESET}' if xstate[7] else f'{Fore.RED}O{Fore.RESET}' if ystate[7] else 7
    eight = f'{Fore.GREEN}X{Fore.RESET}' if xstate[8] else f'{Fore.RED}O{Fore.RESET}' if ystate[8] else 8

    print(f"  {zero}  |  {one}  |  {two}  |")
    print(f"------------------")
    print(f"  {three}  |  {four}  |  {five}  |")
    print(f"------------------")
    print(f"  {six}  |  {seven}  |  {eight}  |")

def checkwin(xstate,ystate):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for a,b,c in win:
       if(xstate[a]==xstate[b]==xstate[c] and xstate[a]!=0):
           return 1;
       elif(ystate[a]==ystate[b]==ystate[c] and ystate[a]!=0):
           return -1;
    return 0




print("Welcome to tic tac toe")
xstate=[0,0,0,0,0,0,0,0,0]
ystate=[0,0,0,0,0,0,0,0,0]
turn=1
while True:
    draw_board(xstate,ystate)
    if turn ==1:
        inp=int(input("Input no for x:\n"));
        pygame.mixer.Sound("click.wav").play()
        xstate[inp]=1
    else:
        inp=int(input("input no for O:\n"))
        ystate[inp]=1
        pygame.mixer.Sound("click.wav").play()
    turn=1-turn
    wincheck=checkwin(xstate,ystate)
    if(wincheck==1):
        draw_board(xstate, ystate)
        print(f"\n{Fore.GREEN}X wins!!!!!!!{Fore.RESET}\n")
        sound=pygame.mixer.Sound("gameover.wav")
        sound.play()
        time.sleep(2)
        break
    elif(wincheck==-1):
        draw_board(xstate, ystate)
        print(f"\n{Fore.GREEN}O wins!!!!!!!{Fore.RESET}\n")
        sound=pygame.mixer.Sound("gameover.wav")
        sound.play()
        time.sleep(2)
        break



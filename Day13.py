import time
import pygame
import random
from colorama import Fore, Style

pygame.mixer.init()


def update_board(stage):
    if stage==0:
        print(f"""\n{Fore.GREEN}
           ------
           |    |
                |
                |
                |
                |
        =========
        
        {Fore.RESET}""")
    elif stage==1:
        print(f"""\n{Fore.GREEN}
           ------
           |    |
           O    |
                |
                |
                |
        =========
        {Fore.RESET}""")
    elif stage == 2:
        print(f"""\n{Fore.GREEN}
           ------
           |    |
           O    |
           |    |
                |
                |
        =========
        {Fore.RESET}""")
    elif stage == 3:
        print(f"""\n{Fore.GREEN}
           ------
           |    |
           O    |
          /|    |
                |
                |
        =========
        {Fore.RESET}""")
    elif stage == 4:
        print(f"""{Fore.GREEN}
           ------
           |    |
           O    |
          /|\   |
                |
                |
        =========
        {Fore.RESET}""")
    elif stage==5:
        print(f"""{Fore.GREEN}
           ------
           |    |
           O    |
          /|\   |
           |    |
                |
        =========
        {Fore.RESET}""")
    elif stage==6:
        print(f"""{Fore.GREEN}
           ------
           |    |
           O    |
          /|\   |
           |    |
                |
        =========
        {Fore.RESET}""")
    elif stage==7:
        print(f"""{Fore.GREEN}
           ------
           |    |
           O    |
          /|\   |
           |    |
          /     |
        =========
        {Fore.RESET}""")
    elif stage == 8:
        print(f"""{Fore.GREEN}
           ------
           |    |
           O    |
          /|\   |
           |    |
          / \   |
        =========
        {Fore.RESET}""")
        sound = pygame.mixer.Sound("gameover.wav")
        sound.play()
        time.sleep(2)

with open("words.txt","r") as f:
    word=f.read().split(",")


def game():
    randomword = random.choice(word).strip()
    run=True
    stage = 0
    gaps = ["-" for i in randomword]
    guess=[]
    while run:
        update_board(stage)
        print("".join(gaps))
        userinput=input("\nEnter letter:\n").lower()

        if userinput in guess:
            print("\nAlready guessed!!!\n")
            continue
        guess.append(userinput)
        if userinput in randomword:
            sound=pygame.mixer.Sound("close.wav")
            sound.play()
            for i in range(len(randomword)):
                if randomword[i]==userinput:
                    gaps[i]=userinput
        else:
            stage+=1
            print(f"Oops! {userinput} is not in the word.")
            sound=pygame.mixer.Sound("oops.wav")
            sound.play()


        if "-" not in gaps:
            print("You won!!")
            print("Congratulations! You guessed the word:", randomword)
            sound=pygame.mixer.Sound("win.wav")
            sound.play()
            time.sleep(2)
            run=False
        if stage==8:
            update_board(8)
            print("Game over! The word was:", randomword)
            run=False
game()
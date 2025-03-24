#Number guess
import random
import pygame,time
pygame.mixer.init()
x=random.randint(1,1000)
y=random.randint(x,1000000)
real_guess=random.randint(x,y)
guess=print("Enter No in range(1-1000000):\n")
while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 1000000:
            print("⚠️ Please enter a number within the range (1-1000000).")
        elif guess == real_guess:
            print(f"🎉 Congratulations! You guessed the correct number: {real_guess} 🎉")
            sound = pygame.mixer.Sound("rightguess.wav")
            sound.play()
            time.sleep(2)
            break
        elif guess < real_guess - 10000:
            print("📉 Way too low! (10^4 range)")
        elif guess > real_guess + 10000:
            print("📈 Way too high! (10^4 range)")
        elif guess < real_guess - 5000:
            print("📉 Very low! (5000+ range)")
        elif guess > real_guess + 5000:
            print("📈 Very high! (5000+ range)")
        elif guess < real_guess - 2000:
            print("⬇️ Low! (2000+ range)")
        elif guess > real_guess + 2000:
            print("⬆️ High! (2000+ range)")
        elif guess < real_guess - 1000:
            print("⬇️ Quite low! (1000+ range)")
        elif guess > real_guess + 1000:
            print("⬆️ Quite high! (1000+ range)")
        elif guess < real_guess - 500:
            print("📉 A bit low! (500+ range)")
        elif guess > real_guess + 500:
            print("📈 A bit high! (500+ range)")
        elif guess < real_guess - 300:
            print("📉 Low! (300 range)")
        elif guess > real_guess + 300:
            print("📈 High! (300 range)")
        elif guess < real_guess - 200:
            print("📉 A little low! (200 range)")
        elif guess > real_guess + 200:
            print("📈 A little high! (200 range)")
        elif guess < real_guess - 100:
            print("🔽 A bit low! (100 range)")
        elif guess > real_guess + 100:
            print("🔼 A bit high! (100 range)")
        elif guess < real_guess - 50:
            print("📉 Almost there, but still low! (50 range)")
        elif guess > real_guess + 50:
            print("📈 Almost there, but still high! (50 range)")
        elif guess < real_guess - 10:
            print("📉 Very close! Just a bit low. (10 range)")
            sound = pygame.mixer.Sound("close.wav")
            sound.play()
        elif guess > real_guess + 10:
            print("📈 Very close! Just a bit high. (10 range)")
            sound = pygame.mixer.Sound("close.wav")
            sound.play()
        else:
            print("🔥 Super close! Almost there.")
            sound = pygame.mixer.Sound("veryclose.wav")
            sound.play()
    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")
import random
name = input("Hello! What is your name? ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.Take a guess. ")
r = random.randint(1,20)
t = 0
while True:
    num = int(input())
    if r < num:
        print("Your guess is too high.Take a guess.")
        t += 1
    elif r > num:
        print("Your guess is too low.Take a guess.")
        t += 1
    else:
        print (f"Good job, {name}! You guessed my number in {t} guesses!")
        break



import random
print("Number Guessing Game")
number=random.randint(1,9)

chance=5
print("Guess any number between 1-9")
while chance>0:
    guess=int(input("Enter your Guess"))

    if guess==number:
        print(guess)
        print("Congratulations!! You won")

    elif guess<number:
        print(guess)
        print("Your Guess is too Low")

    else:
        print(guess)
        print("Your guess is too High")
        
    chance-=1

    if not chance>0:
        print(guess)
        print("You Loose, The number is ", number)
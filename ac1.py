import random
n=random.randint(1,100)

def intro():
    print("Hello, May I know your name?")
    global name
    name=input()
    print(name+ " ,we are going to play a random number game. Guess the number between 1 to 100")
    if n%2==0:
        x="even"
    else:
        x="odd"
    print("The number is",x)
    print("Go ahead and guess:")

def pick():
    if guess<=100 and guess>=1:
        if guess<n:
            print("The guessed number is too low")
        if guess>n:
            print("The guessed number is too high")
    if guess>100 or guess<1:
        print("Invalid guess. Please enter the number between 1 to 100")


intro()
guess=int(input("Enter the guess number"))
pick()
if guess==n:
    print("You have guessed correct number. Congratulations you won!")
if guess!=n:
    print("You have guessed wrong number. I was thinking of", str(n))
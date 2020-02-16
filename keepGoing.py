correct = "IndyPy"
tries = 0

keepGoing = True
while(keepGoing):

    tries = tries + 1
    print("try #",tries)

    guess = input("What is the password?: ")
    if guess == correct:
        print("That's correct! Here's the Treasure!")
        keepGoing = False

    elif tries >= 3:
        print("Too many attempts Loser!")
        keepGoing = False   
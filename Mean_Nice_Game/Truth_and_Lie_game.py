#
# Python:       3.11.7
#
# Author:       Danny Firth
#
# Purpose:      Tech Academy Python course project. Creating my first functional
#               Program in the form of a truth and lie game. Demonstrating how
#               to pass variables from function to function.

def start(truth=0,lie=0,name=""):
    # Get users name
    name = describe_game(name)
    truth,lie,name = truth_lie(truth,lie,name)

def describe_game(name):
    """
        check if this is a new game or not
        If it is new, get the users name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this users name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game you will be greeted \nby several different people. \nYou can choose to tell the truth or to lie")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def truth_lie(truth,lie,name):
    stop = True
    while stop:
        show_score(truth,lie,name)
        pick = input("\nA stranger approaches you and asks \nfor directions. Will you tell the \ntruth or a lie? (T/L) \n>>: ").lower()
        if pick == "t":
            print("\nThe stranger walks away safely down the correct path...")
            truth = (truth + 1)
            stop = False
        if pick == "l":
            print("\nThe stranger walks down the \ndark path never to be seen \nagain...")
            lie = (lie + 1)
            stop = False
    score(truth,lie,name)
        
def show_score(truth,lie,name):
    print ("\n{}, your current total: \n({}, Truths) and ({}, Lies)".format(name,truth,lie))

def score(truth,lie,name):
    # score function is being passed the values stored within 3 variables
    if truth > 2: # if condition is valid, call win function passing in the variables so it can use them.
        win(truth,lie,name)
    if lie > 2: # if condition is valid, call lose function passing in the variables so it can use them.
        lose(truth,lie,name)
    else:       # else, call nice_mean function passing in the variables so it can use them
        truth_lie(truth,lie,name)

def win(truth,lie,name):
    # Substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nYou've been honest with your \ndirections and kept everyone safe!".format(name))
    # Call again function and pass in our variables
    again(truth,lie,name)

def lose(truth,lie,name):
    # Substitute the {} wildcards with our variable values
    print("\nGame over! \n{}, who taught you to be so heartless? \nYour actions have sent innocent \npeople to their doom!".format(name))
    # Call again function and pass in our variables
    again(truth,lie,name)


def again(truth,lie,name):
    stop = True
    while stop:
        choice = input("\nWould you like to play again? (Y/N): \n>>> ").lower()
        if choice == "y":
            stop = False
            reset(truth,lie,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\n Enter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(truth,lie,name):
    truth = 0
    lie = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(truth,lie,name)


if __name__ == "__main__":
    start()

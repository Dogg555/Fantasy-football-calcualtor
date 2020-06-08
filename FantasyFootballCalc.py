#functions of the code
def NFL():
    leagueTypeInput = input("Is the league you are in using defensive players in it (Yes or No)? ")
    if leagueTypeInput == "Yes":
        NFLIDP()
    elif leagueTypeInput == "No":
        NONNFLIDP()
    else:
        print("Sorry you have put invalid input here, please try again.")

    




def ESPN():
    print("This is placeholder text for now.")

def Yahoo():
    print("This is placeholder text for now.")

#Functions of the NFL code
def NFLIDP():
    print("This is placeholder text for now.")

def NONNFLIDP():
    print("This is placeholder text for now.")

#Main Area of the code 
def Main():
    while True:
        websiteChoiceInput = input("Which Website are you using for fantasy football? ")
        if websiteChoiceInput == "NFL":
            NFL()
        elif websiteChoiceInput == "ESPN":
            ESPN()
        elif websiteChoiceInput == "Yahoo":
            Yahoo()
        else:
            print("Sorry either you inputted an ivalid site or this application does not support the site you use at this time")
            break
Main()

#functions of the code
def NFL():
    print("This is placeholder text for now.")
def ESPN():
    print("This is placeholder text for now.")
def Yahoo():
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

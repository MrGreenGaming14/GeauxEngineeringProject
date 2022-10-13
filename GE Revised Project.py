# Import all needed libraries
import random

# NOTES: Add score system to keep track of when the player completes the game

# Global variable that tracks if the player is dead or alive
alive = True
gameOn = True


# Welcome player, Give them directions, Start the quest
def welcome():
    print("\nWelcome to planet PFT-1269. Here you will choose your own adventure. "
          "\nWill you escape the planet or die trying? The choice is yours.")

    input("\nPress 'Enter' to continue; Do not enter any input other then '1' or '2'.\n"
          "Be careful, some choices can result in death! You will have THREE lives\n"
          "To move to the next encounter press 'Enter'.")

    mike_hab()


# If the player dies, this is what prints
def ending():
    print("\nYou have survived your journey through planet PFT-1269\n"
          "Your story will be told for thousands of years across\n"
          "PFT-1269 and you will be known as 'The Escaped.' Thank\n"
          "you for playing! :)")
    gameOn = False


# Start at Mike's habitat and continue the adventure from there
def mike_hab():
    mike_crash = input("\nYou have crashed landed in King Mike's Habitat.\n"
                       "There are two ways you can try to get out.\n"
                       "Either climb the gate (1) or grab the key that's\n"
                       "around King Mike's neck (2): ")

    if mike_crash == "1":
        r = random.randint(1, 100)
        if r <= 85:
            input("\nYou climbed over the gate! Move on to the next thing!")
            bmac()
        else:
            print("\nYou got electrocuted and died")
            alive = False
    elif mike_crash == "2":
        r1 = random.randint(1, 100)
        if r1 <= 65:
            input("\nYou wrestled with King Mike and stole the key!")
            bmac()
        else:
            print("\nKing Mike mauled you and you died.")
            alive = False



# Location change to PMAC
def bmac():
    stad_choice = input(
        "\nYou encounter Pistol Pete (the Human) in the BMAC and he challenges you to a game of HORSE for your honor.\n"
        "Do you Accept (1) or\n"
        "Deny (2): ")

    if stad_choice == "1":
        r = random.randint(1, 100)
        if r <= 100:
            next = input("\nYou lose, however Pete shakes your hand and you retain your honor.")
            fb_stad()

    elif stad_choice == "2":
        r1 = random.randint(1, 100)
        if r1 <= 100:
            next = input(
                "\nPete spits in your face and calls you a loser. You cry in the bathroom, but as you are leaving you\n"
                "run into Shaq (the Human) who comforts you until you feel better.")
            fb_stad()


#Head to the Football Stadium (Alien Colussium)
def fb_stad():
    stad_choice = input("\nYou walk by the empty concessions stand and find a water bottle.\n"
                        "Leave (1) or\n"
                        "Drink the water (2): ")

    if stad_choice == "1":
        r = random.randint(1, 100)
        if r <= 100:
            next = input("\nYou gain the will power of all previous LSU quarterbacks")
            quad()

    elif stad_choice == "2":
        r1 = random.randint(1, 100)
        if r1 <= 100:

            print("\nYou died of dysentery.")
            alive = False



# Location Change to Quad
def quad():
    q1 = input("\nYou find a bike, do you continue walking or ride the bike?.\n"
               "Ride the Bike (1) or\n"
               "Walk (2): ")

    if q1 == "1":
        r = random.randint(1, 100)
        if r <= 100:
            next = input("\nYou crash into a classroom and are viciously attacked by alien kindergarteners with crayons")
            union()


    elif q1 == "2":
        r1 = random.randint(1, 100)
        if r1 < 100:
            next = print("\nYou run into a teacher who teaches you to speak their language.")
            union()


# Location Change to Union


def union():
    union = input(
        "\nYou have wandered into  PTF-1269's Capital city\n You see  alien citizens starving in the streets\n"
        "while the rich government gets fat off of their excess labor.\n"
        "Do you overthrow the current societal system to better (1)\n"
        "or visit Smoothie King (2)")

    if union == "1":
        next = print(
            "\nYou successfully become the new king of this strange alien world;"
            "\n however, you are not cut out for leadership and no significant"
            "\n""change is made in the aliens' life."
            "\n""You grab some Chick-Fil-A on your way out of the union.\n")
        par()
    elif union == "2":
        r1 = random.randint(1, 100)
        if r1 <= 50:
            next1 = print("\nYou visit Smoothie King and get robbed.")
            par()


# Location Change to Parade Grounds


def par():
    par1 = input("\nYou walk into an alien place of worship Do you mock them or join them?.\n"
                 "Mock (1) or \n"
                 "Join (2): ")

    if par1 == "1":
        next = input("\nYou become the new god and aliens spit on your feet.")
        street()

    elif par1 == "2":
        print("\nYou see the aliens spitting on their god's feet. You refuse to do the same and they kill you.")
        alive = False


# Sidewalk Encounters


def street():
    # Creates 3 scenarios
    r1 = random.randint(1, 100)

    # Scenario 1
    if r1 <= 33:
        street = input("\nYou wander across an alien street dancer,\n"
                       "do you challenge him to  dance battle (1) or walk away (2)\n")
        if street == "1":
            # Randomizer to die
            r2 = random.randint(1, 100)
            if r2 <= 50:
                next = input("\nYou use your fresh moves to win the competition and take all\n"
                             "the money in the alien dancer’s hat, leaving him broke and helpless\n")
                din_hall()
            else:
                next = input("\nYou fall over while dancing and crack your skull. You are dead\n")
                alive = False
        elif street == "2":
            next1 = input("\nYou walk away ashamed and regretful\n")
            din_hall()

        # Scenario 2
    elif r1 <= 66:
        street = input("\nYou come across a lone Cane's chicken finger in the middle of the road.\n"
                       "Do you eat the finger (1) or risk starvation (2)?\n")
        if street == "1":
            # Randomizer to die of monkeypox
            r2 = random.randint(1, 100)
            if r2 <= 30:
                next = print("\nYou contract lethal monkeypox and die from the street chicken\n")
                alive = False
            else:
                next = print("\nYou contract non-lethal monkeypox from the street chicken\n")
                din_hall()
        elif street == "2":
            next = print("\nYou continue walking but now hunger for chicken fingers.\n")

            din_hall()

        # Scenario 3
    else:
        street = input("\nYou are hit by an alien school bus. Do you\n"
                       "sue the school (1) or carry on (2)\n")
        if street == "1":
            # Randomize if you win the court case or not
            r2 = random.randint(1, 100)
            if r2 <= 50:
                next = input("\nLSU had better lawyers than you and now you owe the\n"
                             "school $200,000. You die of going hungry \nfrom too much debt.\n")
                alive = False
            else:
                next = input("\nYou somehow beat the LSU lawyers and win $200 back.\n"
                             "You continue on your journey.")
                din_hall()
        elif street == "2":
            next = input("\nYou have a mild concussion but only throw up a little bit.\n"
                         "You continue on your adventure")
            din_hall()


# Location Change to The 459
def din_hall():
    dh = input("\nYou find Crawfish. Do you steal the crawfish?\n"
               "Yes (1) or \n"
               "No (2): ")
    if dh == "1":
        r = random.randint(1, 100)
        if r <= 65:
            print("\nYou get shot and survive with minimal injuries.")
            ending()
        else:
            print("You get shot and die.")
            alive = False

    elif dh == "2":
        r1 = random.randint(1, 100)
        if r1 < 100:
            next = print("\nYou go hungry and die.")
            alive = False


# Function that starts the game, They have three tries to get as far as they can
while gameOn == True:
    for i in range(3):
        welcome()
        if alive == False:
            alive = True
            i += 1
        remain = str(2 - i)
        print("\nYou have " + remain + " lives left")
        gameOn = False

while gameOn == False:
    print("Thank you for playing the game! Try again later :)")
    break
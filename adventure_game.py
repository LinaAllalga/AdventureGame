import time
import random


def playing_game():
    creatures = ["dragon", "witch", "monster", "pirate", "demon"]
    creatures = random.choice(creatures)
    input = ""
    weapon = ""
    start()
    firstchoice(creatures, weapon)


def print_pause(content):
    print(content)
    time.sleep(1)


def valid_input(content):
    while True:
        choose = input(content)
        if choose == "1" or choose == "2":
            break
    return choose


def start():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here,"
                " and has been terrifying the nearby village.\n")
    print_pause("In front of you, there is a house.\n")
    print_pause("To your right\n" "There is a dark cave")
    print_pause("In your hand you hold your trusty"
                "(but not effective) dagger.\n")


def firstchoice(creatures, weapon):
    again = 0
    fin = 0
    while True:
        if fin == 1:
            return
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("What would you like to do?")
        Decision = valid_input("(Please enter 1 or 2?)\n")
        if Decision == "1":
            if house(creatures, weapon) == 1:
                fin = 1
        else:
            cave(creatures, again)
            weapon = "sword"
            again = 1


def house(creatures, arme):
    print_pause("You approach the door of the house.\n")
    print_pause("You are about to knock when the door opens"
                "and out steps a " + creatures + ".")
    print_pause("Eep! This is the " + creatures + "'s house!\n")
    print_pause("\nThe " + creatures + " attacks you!\n")
    if "sword" not in arme:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.\n")
    while True:
        choice = valid_input("Do you want to (1) fight or (2) run away?")
        if choice == "1":
            if "sword" in arme:
                if sword() == 1:
                    return 1
            else:
                if no_sword(creatures) == 1:
                    return 1
            break
        if choice == "2":
            print_pause("\n You run back into the field"
                        "\n Luckily, you don't seen to have been"
                        "\nfollowed")
            firstchoice(creatures, arme)
            break


def sword():
    print_pause("As the gorgon moves to attack,"
                "you unsheath your new sword.\n")
    print_pause("The Sword of Ogoroth shines brightly in your hand as you"
                "brace yourself for the attack.\n")
    print_pause("But the gorgon takes one look at your shiny new toy"
                "and runs away!\n")
    print_pause("You have rid the town of the gorgon. You are victorious!\n")
    if play_again() == 1:
        return 1


def no_sword(creatures):
    print_pause("You do your best...")
    print_pause(f"but your dagger is no match for"
                "the wicked " + creatures + ".")
    print_pause("You have been defeated!")
    if play_again() == 1:
        return 1


def cave(bestiole, historique):
    print_pause("You peer cautiously into the cave.\n")
    fusil = "sword"
    if historique == 0:
        print_pause("It turns out to be only a very small cave.\n")
        print_pause("Your eye catches a glint of metal behind a rock.\n")
        print_pause("You have found the magical Sword of Ogoroth!\n")
        print_pause("You discard your silly old dagger and"
                    "take the sword with you.")
        print_pause("You walk back out to the field.\n")
    else:
        print_pause("You've been here before, and gotten all the good"
                    "stuff. It's just an empty cave now.\n")
        print_pause("You walk back out to the field.\n")


def play_again():
    print_pause("GAME OVER")
    again = valid_input("If you want to play again,"
                        "press 1? If not, press 2").lower()
    if again == "1":
        print_pause("Excellent! RESTARTING THE GAME ...")
        playing_game()
    else:
        print_pause("Thanks for playing! See you next time.")
        exit()


playing_game()

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    
    if name == "rock":
        return 0
    elif name == "Spock":
		return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
		return 3
    elif name == "scissors":
     	return 4
    else:
        return False
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    
    if number == 0:
       return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2
    	return "paper"
    elif number == 3:
      	return "lizard"
    elif number == 4:
      	return "scissors"
    else:
        
        return False
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
   
    
    
    
    
    # print a blank line to separate consecutive games
    print ""

    # print out the message for the player's choice
    player_choice = raw_input("Enter name.:" )
    
    # convert the player's choice to player_number using the function name_to_number()
    print "Player chooses ", player_choice
    
    player_choice = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    computer_choice = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    print "Computer chooses ", number_to_name(computer_choice)

    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five
    difference = (computer_choice - player_choice) % 5
    

    # use if/elif/else to determine winner, print winner message
        
    if difference == 1 or difference == 2:
        print "Computer Wins!"
        
    elif difference == 3 or difference == 4:
        print "Player Wins!"
        
    elif difference == 0:
        print "It's a tie!"
        
    else:
        return False

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")






###########################################################################
##                                                                         #
##! /usr/bin/env python3                                                   #
## Program Description: A text adventure game                               #
##                                                                         #
###########################################################################


##################################################################################
#--------------------------------------------------------------------------------#
# STORY 
# This program is a game where a warrior is stuck in a building in a war
# for a long time as he was busy fighting the rival. Now, he is out of weapons,
# he must reach to the other soldier with weapons. Once, he finds the
# path to the comrade with weapons. So that they can defeat the opponent soldiers. 
#--------------------------------------------------------------------------------#
##################################################################################

#TODO: 
# rules/about

# IMPORT STATMENTS
import random


# DECLARING VARIABLES    
# The items that the player starts the game with
weapons = ['Ak47', 'M4Carbine', 'M24sniper', 'Msaw', 'bullets']
war = ['Soldier1']		# People in the game
pos_x = 0		# Player1 starting position in the x axis 
pos_y = 1		# Player1 starting position in the y axis
you_hm = 15.0		# Health meter.This is put here so that you can determine your health while playing the game and use power ups to increase your health.

#MAPS
map_base = '''
                    ----------------
                    |              |__
                    | upstairs     |__  outside
                 == |              |
--------------- ==  ------|   |-----
|             |==         |   | 
|downstairs   |       ----     ----
|             |------|   Balcony   |
--  -----------       -------------
  |  |
--|  |-------
| open area  |
-------------
'''

map_outside = '''
               ----------
              | Adj     |           
              | build   |           
              |__    __ |          ________
/\/\/\/\/\/\/\/\/|  | /\/\//\/\/ /    /|\ \ 
---------------------------------      |   |
                                      /|\  |
---------------------------------  (park)  |   
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\___  ___/
                                     | |
            (misc houses)                        
'''         
# STORY DIALOG
# Introduction to the game
def d_intro():
    print("\nYou are in a basement, a bit confused. You have been fighting the opponents continuously since a long time and noticed a comrade along with a bunch of weapons, in the park.  *SHPAOOSH.\n") 
    input() 
    print("They are too far from the building.\n")
    input()
    print("*Turns on the walkie to reach out the comrade \" *RING.")
    input()
    print("Soldier1:\"Hello, there is an urgent need of weapons\"\n")
    input()
    print("Soldier2:\"I'm in the park located beside the building \"\n")
    input()
    print("Soldier1: \"I have located you , what's the plan?\"\n")
    input()
    print("Fred: \"Find a way and make it to the park\"\n")
    input()
    print("You: \"Roger that.\"\n")

# When you reach outside
def d_outside():
    print("\n The place is empty, there is nobody outside. But one person is standing across the park may be that's soldier2")
    input()
    print("Person across the street: Opponents are attacking make it fast.\"\n") 
    input()

# When you get to the park
def d_park():
    print("\nSoldier2: \"Where are you? We don't have much time.\"")
    input()
    print("\"Let's find a safe cover first.\"")
    print("END PART I")

# MAIN FUNCTIONS
# A function to check what the player has in it's inventory.
# A loop compares the input (item) to each of the items in the list 
# 'weapons.'
def check_items(item):
    x = 0			    # Initializes the value of x
    have = False	            # Initializes the value of have
    for i in range(len(weapons)):    # A loop that lasts the length of the list
        x += 1
        if weapons[x-1] == item:     # Cycles through the items in the list
            have = True             # If a match is found have is set to true
        else: 
            pass 
    return have			    # Returns the value of have
  
# A function to check who is in the war. 
# This works in the same way as the 'check_items' function.
def check_war(name):
    x = 0
    have = False
    for i in range(len(war)):
        x += 1
        if war[x-1] == name: 
            have = True
        else: 
            pass 
    return have

# A function to check the position of the player
def check_pos():
    global pos_x
    global pos_y
    if pos_x < 0:
        print("Warning : Stepped out of the line")
        pos_x = 0
    if pos_y < 0:
        print("Warning: Stepped out of the line")
        pos_y = 0
    if pos_x == 2:
        d_outside()
    if pos_x == 8:
        d_park()

# A function that allows the player to search the surroundings for weapons
def search():    
    # Determines if you have too many weapons
    num_items = len(weapons)
    if num_items < 7:
        i = random.randint(0, 15)
        # Determines if you find weapons
        if i == 0 or 3:			# Find Msaw
            print("You found Msaw, capacity is 20 bullets.")
            weapons.append("Msaw")
        elif i == 1 or 5:		# Find Bullets
            print("Pack consists of 50 bullets")
            weapons.append('Bullets')
        elif i == 2:			# Find other weapons
            w = random.randint(0,2)
            if w == 0:
                print("You found M24sniper")
                weapons.append('M24sniper')
            elif w == 1:
                print("you found a Grenade")
                weapons.append('Grenade')
            elif w == 2:
                print("you found a F2000")
                weapons.append("F2000")  
        else:
            print("You found nothing")
    else:
        print("You can't carry anything else.  If you want to pick something up, you need to drop something.")

# A function that allows player to drop items
def drop():
    print(weapons)
    drop_item = input("\nEnter the index of the item you want to drop (use number keys and the first item is index 0)")
    weapons.pop(int(drop_item))


# A function that defines fighting
# For a description on how fighting works, read the README file.
def fight():

    global soldier1_hm

    # A collection of definitions for the players stats including attack (a),
    # defence (d) and health meter (hp).
    # Main player (soldier1)
    soldier1_a = 5.0   
    soldier2_d = 7.0
    # Second player
    soldier2_a = 9.0
    soldier2_d = 5.0
    soldier2_hm = 10.0 
    # Opponent one
    opponent_a_one = 5.0
    opponent_d_one = 4.0 
    opponent_hm_one = 7.0
    # opponent two
    # There is no need to define opponent_a_two or opponent_a_three 
    opponent_d_two = 6.0 
    opponent_hm_two = 7.0

    # Determines if there are any weapons/ power ups
    have = check_items('M24sniper')
    if have == True:
        soldier1_a += 1.5
        soldier1_d += 0.5
    have = check_items('Grenade')
    if have == True:
         soldier1_a += 3.0
         soldier1_d += 1.0
    have = check_items('F2000')
    if have == True:
         soldier1_a += 0.5
         soldier1_d += 2.0
    else:
        pass

    num_opponent = random.randint(1,2)	# Determines the number of opponents
    turn = 0		       	        # Initializes turns
    fight = True                        # Initializes loop
    print("watch out, there are " + str(num_opponent) + " opponents!")

    while fight == True:
        turn += 1        # Increases value of turn to create a pseudo turntable 
        go = turn  % 2	 # Determines if it is soldiers or opponents turn

        # If the number of opponents is less than three this will set the hm of the other opponents to zero
        if num_opponent == 1:	
            opponent_hm_two = 0
        else:
            pass

        # When you kill the zombie(s)
        if opponent_hm_one <= 0 and opponent_hm_two <= 0:	
            print("You defeated the opponent")
            break
        # When the opponent(s) kills you
        if opponent_hm <= 0:	 
            print("Failed")
            quit()
 
        if go == 1:	 			# Players turn
           super_att = random.randint(1,7)	# Determines the strength of att
           if super_att == 1:
               soldier1_a = 15.0
           elif super_att == 2:
               soldier1_a = 10.0
           elif super_att == 3:
               soldier1_a = 30.0
           elif super_att == 4:
               soldier1_a = 1.0
           else: 
               soldier1_a = 5.0
          
           # Receives input from the user regarding attack
           opt = input("do you wish to attack\n")
           if opt == 'yes':      
               # Recives input from the user regarding which opponent to attack
               dev = input("which opponent would you like to attack\n")
               if dev == "1":         
                   hit = soldier1_a / opponent_d_one
                   opponent_hm_one -= hit
                   print("opponent 1 has " + str(int(opponent_hm_one)) + " hm left")
               elif dev == "2":         
                   hit = soldier1_a / opponent_d_two
                   opponent_hm_two -= hit
                   print("opponent 2 has " + str(int(opponent_hm_two)) + " hm left")
               else: print("invalid input -> looks like you lost your turn")
           elif opt == 'no':
              print("You do not attack") 
           # If the user chooses to not fight there is a on in five chance that they will be able to run away
           elif opt == 'run':
              r = random.randint(0,5)
              if r == 0:
                  print("You got away")
                  break
              else:
                  print("The opponents caught up to you.")
                  pass
           else:
               print("Invalid input.")
       
        elif go == 0:	 	 		# Computer turn
           att = random.randint(1,5)            # Determines if opponent attacks 
           super_att = random.randint(1,3)	# Determines the strength of att
           if super_att == 1:
               opponent_a_one = 20.0
           elif super_att == 2:
               opponent_a_one = 2.0 
           else: 
               opponent_a_one = 6.0

           # Opponent attacks
           if att == 1 or 2 or 3:
               hit = opponent_a_one/soldier1_d 
               soldier1_a_hm -= hit
               print("\nAn opponent attacked and you have " + str(int(soldier1_hm)) + " hm left")
           # opponent does not attack
           else:
               print("\nThe opponent has missed")

# MAIN GAMEPLAY
def main():

    global pos_x
    global pos_y
    global soldier1_hm

    d_intro()
    
    game = True		# Initializes the variable game to True
    while game == True:
        z = random.randint(0,3)		# Randomly decides if player fights zombie
        if z == 3:
            fight()
        check_pos()	# Checks the position of the character
        dev = input("\n what are you going to do\n").lower()
     
        # Quits the game
        if dev == "quit": 
            game = False
        # For moving around
        elif dev == "left":
           pos_x -= 1
        elif dev == "right":
           pos_x += 1
        elif dev == "up":
           pos_y += 1
        elif dev == "down":
           pos_y -= 1
        # Tells the player respective x and y positions
        elif dev == 'pos x':
            print(pos_x)
        elif dev == 'pos y':
            print(pos_y) 
        # Prints a map base on position
        elif dev == "map":     
            if pos_x <= 2 and pos_y <= 2:
                print(map_base)
                if pos_x == 0 and pos_y == 0:
                    print("You are in the open area")
                elif pos_x == 0 and pos_y == 1:
                    print("You are downstairs")
                elif pos_x == 0 and pos_y == 2:
                    print("You are downstairs")
                elif pos_x == 1 and pos_y == 1:
                    print("You are in the balcony")
                elif pos_x == 1 and pos_y == 2:
                    print("You are upstairs")
                elif pos_x == 1 and pos_y == 3:
                    print("You are upstairs")
                elif pos_x == 2:
                    print("You are outside")
            elif pos_x > 2 and pos_x <= 8 and pos_y == 2:
                print(map_outside)
                if pos_x > 2 and pos_x <= 7 and pos_y == 2:
                    print("You are on the road to the park")
                    if pos_x == 4:
                        print("You are infront of adjacent house")
                if pos_x == 8 and pos_y == 2:
                    print("You are in the park")
            else:
                print("Out of map.You are somewhere? \nTry moving up or down!")
        # Misc commands
        elif dev == "check items": # Displays items in weapons
            print(weapons)
        elif dev == "health":	   # Shows how many health points you have
            print(soldier1_hm)
        elif dev == "Weapon":	   # You should find a weapon to increase hm
            have = check_items("Msaw")
            if have == True:
                hp_up = random.randint(2, 5)
                soldier1_hm += hm_up
                weapons.remove('Msaw')
                print("Soldier1 hm increased by " + str(hm_up))
            elif have == False:
                print("You don't have any weapons. Need to find weapons")
            else:
                print("something went wrong")
        elif dev == "Find weapon":	   # You want to find a weapon to inrease hm
            have = check_items("bullets")
            if have == True:
                hp_up = random.randint(4, 7)
                soldier1_hm += hm_up
                weapons.remove('bullets')
                print("Your hm increased by " + str(hm_up))
            elif have == False:
                print("You don't have any weapons")
            else:
                print("Something went wrong")
        elif dev == "search":	# Search for weapons
            search()
        elif dev == "drop":	# Drops weapons
            drop() 
        else: 
            print("What is this \"" + dev + "\" ")

# The introduction
print("\n \n \n \nHello and welcome to the game. In this game you are a soldier fighting the opponents, type in 'start' to begin.") 
opt = input()
if opt == 'start': 
    main()
elif opt == 'how to play':
    print("\n\n\n\nHOW TO PLAY:  \n\nMAIN CONTROLS:  There are several functions you can do in this game. To move around you simply enter which way you want to go. \n For example, if you want to go left, type in \"left\".  It is important to note that your movements are tracked using a grid system.You can find your position in the x or y plane at any time by inputting \"pos x\" or \"pos y\".\nTo print a map so you can know where in the world you are, input \"map\". It will show you a map and tell you where you are.\nAs you might assume, you are carrying weapons.  To see what you are holding you can input \"check items\".  You can also drop weapons by inputting \"drop\" or check if you can pick anything up from your environment by inputting \"search\".\nIf you want to know how many health points you have, type in \"health\"   \n \nFIGHTING:  You can also fight zombies in this game.At any one time you can fight one or two opponents but keep in mind, your soldier2,does not help you while you fight.  First you will be told how many opponents you are fighting. Then you can choose to fight by typing in \"yes\" or you can choose to get away from the fight by typing in \"run\" and \"no\" to do neither.To choose which zombie you wish to attack, press \"1\" for opponent one, or \"2\" for opponent two.\nIf your hm is low after fighting some opponents you can find new weapons by typing \"weapons\" or \"find weapon\". Remember that you need to have weapons to fight. \nThat is it.  Also, sometimes you can kill an opponent into negative hm.  Don't worry about that, you are just getting good at the game.")
    if input() == 'start':
	
        main()
    elif input() == 'quit':
       exit 
else:
    print("Sorry, you have been killed by an opponent\n.")
    
    # TESTING CODE
    # runs the 'check_items' fuction and returns an output based on the weapons
    #have = check_items('M4carbine')
    #if have == True: print("you have that")
    #elif have == False: print("you do not have that")
    #else: print("something went wrong")
##################################################################################
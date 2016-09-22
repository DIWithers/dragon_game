# 1. Start with a message:
#   -you encountered a dragon 
# 2. While loop will keep the game going
#   - User must enter 1 or 2
#   - If something else, let them know and give options
# 3. If they choose "run" (1 or 2), call them a coward and give them the opt of playing again
#   -- they can always just exit
# 4. If they choose fight, then init the hero and dragon health
#  - Bonus: hero and dragon are classes (otherwise dictionary)
# 5. Ask the user if they want 1, 2, 3 (attack, spell or defend)
#   - If user enters something bogus, handle it (i.e. dragon gets a shot etc)
#   -opt. add a method to the hero class ie. hero.fight(), hero.spell()
# 6. update the dragon health based on the outcome
#   -import random module
# 7. randomize the dragon's attack (based on hero's defense or spell)
# 8. update hero health
# 9. check if anyone is dead and handle
# 10. if both alive, repeat to 5
import sys
import time
import random
import math
from dragon_game_classes import Hero
from dragon_game_classes import Dragon

# begin_game = raw_input("Would you like to play the Dragon Game? Choose Y or N  ")
# print begin_game
# if (begin_game != "Y"):  
#   print("Please type Y or N")
# elif (begin_game != "N"):
#   print("Please type Y or N")
# elif (begin_game == "N"):
#     print("Too bad, goodbye")
# elif (begin_game == "Y"):

        



def begin_game():
    
    print ("  ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___")
    time.sleep(.3)
    print ("~~ ~--__          ......====\\~~    .:::.    ~~//====......          __--~ ~~")
    time.sleep(.3)
    print ("         ~\ ...::::~~~~~~  //|||    .:::::.    |||\\  ~~~~~~::::... /~")
    time.sleep(.3)
    print ("        -~~\_            //  |||***.(:::::).***|||  \\            _/~~-")
    time.sleep(.3)
    print ("             ~\_        // *******.:|\^^^/|:.******* \\        _/~")
    time.sleep(.3)
    print ("                \      / ********.::(>: :<)::.******** \      /")
    time.sleep(.3)
    print ("                 \   /  ********.::::\\|//::::.********  \   /")
    time.sleep(.3)
    print ("                  \ /   *******.:::::(o o):::::.*******   \ /")
    time.sleep(.3)
    print ("                   /.   ******.::::'*|V_V|***`::.******   .\ ")
    time.sleep(.3)
    print("                      ~~--****.:::'***|___|*****`:.****--~~")
    time.sleep(.3)
    print("                            *.::'***//|___|\\*****`.* ")
    time.sleep(.3)
    print("                            .:'  **/##|___|##\**    .")
    time.sleep(.3)
    print("                           .    (v(VVV)___(VVV)v)")
    time.sleep(.5)
    print("")
    time.sleep(1)
    print("         Soon after you begin your journey, you come across a precipice. ")
    time.sleep(1)
    print("       From below you hear a low grumble. The ground begins to shake and a dragon emerges from the deep. He towers above you. ")
    time.sleep(2)
    hero_choice = raw_input(" *** What do you do? RUN or FIGHT?   " )
    if (hero_choice != "RUN") and (hero_choice != "FIGHT"): 
        print hero_choice
        exit_choice = raw_input("*** You can always just quit and escape your problems by not making a choice. Type EXIT to quit *** ")
        if (exit_choice == "EXIT"):
            print("Too bad, goodbye")
            sys.exit()
            # need to make another option
    elif (hero_choice == "RUN"):
        print("*** Your children will have no stories to tell of you. However, you will live another day. Goodbye ***")
        sys.exit()
    elif (hero_choice == "FIGHT"):
        print(" *** You steel yourself against the incoming battle and ready your weapon. *** ")
        time.sleep(1)
        print("      Remember, you have a choice to attack on your turn, or defend.   ")
        time.sleep(1)
        print("      If you choose to defend, your defense will increase but you will lose your chance to attack.")
        time.sleep(1)
        print("      Choose wisely, hero....   ")
        time.sleep(2)

        while (hero.health > 0 and dragon.health > 0):
            if (hero.isTurn == True):
                if (hero.defense > 10):
                    hero.defense = 10
                if (hero.health <= 5):
                    print("You are dying! A courageous shopkeeper appears in your view and offers you a healing potion")
                    if (hero.purse < 1):
                        print("You don't have enough money to buy any potions!")
                    elif (hero.purse >= 1):
                        last_resort = raw_input("Do you accept? Y or N  ")
                        if (last_resort != "Y" and last_resort != "N"):
                            last_resort = raw_input("Do you accept? Y or N  ")
                        if (last_resort == "N"):
                            print("The shopkeeper grumbles and disappears again to watch you die.")
                        if (last_resort == "Y"):
                            hero.purse -= 1
                            print("     You quickly throw the shopkeeper 1 coin and he throws back a small bottle...")
                            time.sleep(1)
                            print("        Can you catch it......?")
                            time.sleep(2)
                            last_resort_roll = random.random() * 10
                            last_resort_roll = int(math.floor(last_resort_roll)) + 1
                            if (last_resort_roll >= 3):
                                print("     You catch it! You gain 10HP!")
                                hero.health += 10
                                time.sleep(1)
                            else:
                                print("     You miss! The bottle crashes to the ground and you turn your attention back to the dragon.")
                                time.sleep(1)

                a_or_d = raw_input("Attack or defend. Choose A or D, hero.  ")
                if (a_or_d == "A"):
                    hero.roll = random.random() * 20
                    hero.roll = int(math.floor(hero.roll)) + 1
                    if (hero.roll > dragon.defense):
                        print ("*** YOU ATTACK! ***")
                        time.sleep(1)
                        print ("***Success! You injure the dragon! ")
                        dragon.health -= 5
                        check_health()
                        hero.isTurn = False
                        dragon.isTurn = True
                    elif (hero.roll <= dragon.defense):
                        print ("*** YOU ATTACK! ***")
                        time.sleep(1)
                        print ("*** You lunge and miss! No damage to the dragon... ")
                        hero.isTurn = False
                        dragon.isTurn = True
                if (a_or_d == "D"):
                    hero.defense += 5
                    health_roll = random.random() * 5
                    health_roll = int(math.floor(health_roll)) + 1
                    hero.health += health_roll
                    print("Lucky you, you gained " + str(health_roll) + " health!")
                    hero.isTurn = False
                    dragon.isTurn = True
            time.sleep(1)

            if (dragon.isTurn == True):
                dragon.roll = random.random() * 20
                dragon.roll = int(math.floor(dragon.roll)) + 1
                if (dragon.roll > hero.defense):
                    print("*** The dragon attacks! ***")
                    time.sleep(1)
                    print("*** Hot flames sear your skin! ***")
                    hero.health -= 5
                    check_health()
                    hero.isTurn = True
                    dragon.isTurn = False
                    time.sleep(1)
                elif (dragon.roll <= hero.defense):
                    print("*** The dragon attacks! ***")
                    time.sleep(1)
                    print("*** The hot flames barely miss your head. No damage to hero. ")
                    hero.isTurn = True
                    dragon.isTurn = False
                    time.sleep(1)
            time.sleep(3)

def check_health():
    if (hero.health <= 0):
        time.sleep(1)
        print("         You died, Hero. Good game.")
        time.sleep(1)
        print("")
        print("             (   .      )")
        print("        )           (              )")
        print("         .  '   .   '  .  '  .")
        print("     (    , )       (.   )  (   ',    )")
        print("     ). , ( .   (  ) ( , ')  .' (  ,    )")
        print("  (_,) . ), ) _) _,')  (, ) '. )  ,. (' )")
        print("  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        player_choice = raw_input("Would you like to play again? Y or N  ")
        hero.health = 20
        dragon.health = 30
        if (player_choice != "Y" and player_choice != "N"):
            player_choice = ("It's not that hard...Y or N  ")
        elif (player_choice == "Y"):
            begin_game()
        elif (player_choice == "N"):
            print("Thanks for playing! Goodbye")
            sys.exit()
    elif (dragon.health <= 0):
        print("       You defeated the dragon! The peasants rejoice!")
        print("")
        time.sleep(.2)
        print("                .''.  ")
        time.sleep(.2)
        print(" .''.      .        *''*    :_\/_:     . ")
        time.sleep(.2)
        print("        :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'. ")
        time.sleep(.2)
        print("    .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=- ")
        time.sleep(.2)
        print(":_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.' ")
        time.sleep(.2)
        print(": /\ : :::::     *_\/_*     -= o =-  /)\    '  * ")
        time.sleep(.2)
        print(" '..'  ':::'     * /\ *     .'/.\'.   ' ")
        time.sleep(.2)
        print("     *            *..*         : ")
        time.sleep(.2)
        print("       * ")
        time.sleep(.2)
        print("        * ") 
        time.sleep(.2)
        player_choice = raw_input("Would you like to play again? Y or N  ")
        hero.health = 20
        dragon.health = 30
        if (player_choice != "Y" and player_choice != "N"):
            player_choice = ("It's not that hard...Y or N  ")
        elif (player_choice == "Y"):
            begin_game()
        elif (player_choice == "N"):
            print("Thanks for playing! Goodbye")
            sys.exit()
    

player_choice = raw_input("   Would you like to play The Dragon Game? Y or N  ")
if (player_choice != "Y" and player_choice != "N"):
    player_choice = ("  It's not that hard...Y or N  ")
elif (player_choice == "Y"):
    hero = Hero(5, "sword", 20, 10, True, 5, True, 5)
    dragon = Dragon(13, 30, 13, True, 5, False)
    begin_game()
elif (player_choice == "N"):
    print("  Goodbye!  ")
    sys.exit()

        
        


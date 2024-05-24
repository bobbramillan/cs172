#bb3323 Bavanan Bramillan
#Partner: William Wranovsky wbw32

######TODO######    
#import the Monster and Hero classes here
from characters import Monster as m1, Hero as h1

import random

# This function has two Characters fight
# it returns the winner or None on a tie
def monster_battle(h1, m1):
   
    print("Starting Battle Between")
    print(m1.getName() + ": " + m1.getDescription())
    print(h1.getName() + ": " + h1.getDescription())
    
    #Whose turn is it?
    attacker = None
    defender = None

    ######TODO######    
    #Select Randomly whether h1 or m1 is the initial attacker
    #the other is the initial defender
    initial = random.randint(1,2)
    if initial == 1:
        attacker = m1
        defender = h1
    else:
        attacker = h1
        defender = m1
        
    print(attacker.getName() + " goes first.")
    
    #Loop until someone is unconsious (health < 1) or choose to stop
    stop = False
    while( m1.getHealth() > 0 and h1.getHealth() > 0 and not stop ):
        
        #It will be nice for output to record the damage done
        before_health = defender.getHealth()            

        #Check if the attacker is a monster
        if(isinstance(attacker, Monster)):
            #check if defender is defending, if so print out info about the defense
            if(defender.isDefending()):
                print("Our hero is defending with", defender.getDefenseName(), "!")
            
            
            ######TODO######    
            #Have the attacker react.
            #Have the attacker attack.
            #Call the print_results function with the necessary info.


        else:
            # Ask the user for the next action: attack, defend, or stop.
            action = input('Pick one of these (a)ttack, (d)efend, or sto(p): ')
        
            ######TODO######    
            #Based on the input, either attack, defend, or end loop
            #If they chose to attack, have the attacker react, attack and then
            #call the print_results function with the necessary info.

        
        ######TODO######
        #Swap attacker and defender
        

    ######TODO######    
    #Print out who won.
    #Return who won.
    print("Battle is over. let's see who has won...")
    return f'{m1.getName} is victorious!'
    
    
    
#This function prints the status updates
def print_results(attacker, defender, attack, hchange):
    res = attacker.getName() + " used " + attack
    res += " on " + defender.getName() + "\n"
    res += "The attack did " + str(hchange) + " damage."
    print(res)
    print(attacker.getName() + " at " + str(attacker.getHealth()))
    print(defender.getName() + " at " + str(defender.getHealth()))


#----------------------------------------------------
if __name__=="__main__":
    
    ######TODO######    
    #Get Monster's name, description, maxHealth, weaponName, weaponDamage, and motivation from the user here.
    #Instantiate a Monster using that info. Note that weaponDamage should be a floating point number.
    
    m1.getName = input("Enter monster's name: ")
    m1.getDescription = input(" Enter monster's description: ")
    m1.getHealth = input("Enter a number for monster's health: ")
    m1.getWeaponName = input("Enter monster's weapon name: ")
    m1.getWeaponDamage = float(input("Enter monster's weapon damage (as a number): "))
    m1.getMotivation = input("Enter monster's motivation: ")

    myMonster = m1  #this should be an instance of your Monster class
    
    ######TODO######    
    #Get the Hero's name,description, maxHealth, weaponName, weaponDamage, defenseName from the user here.
    #Instantiate a Hero using that info. Note that weaponDamage should be a floating point number.

    h1.getName = input("Enter hero's name: ")
    h1.getDescription = input("Enter the hero's description: ")
    h1.getHealth = input("Enter a number for the hero's health: ")
    h1.getWeaponName = input("Enter hero's weapon name: ")
    h1.getWeaponDamage = float(input("Enter hero's weapon damage (as a number): "))
    h1.getDefenseName = input("Enter the hero's defense name: ")

    
    myHero =  h1  #this should be an instance of your Hero class
    
    winner = monster_battle(myHero, myMonster)
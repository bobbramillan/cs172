#bb3323 Bavanan Bramillan 
#Partner: William Wranovsky wbw32

# This class defines a generic Character
# It includes attributes and many implemented methods, in addition to an abstract
# methods __str__ and react
from abc import ABC, abstractmethod

### DO NOT CHANGE ANYTHING BELOW IN THIS Character CLASS ####
class Character(ABC):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage):
        self.__name = name
        self.__health = maxHealth
        self.__description = description
        self.__weaponName = weaponName
        self.__weaponDamage = weaponDamage

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def react(self):
        pass
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description
    
    def getWeaponName(self):
        return self.__weaponName
    
    def getWeaponDamage(self):
        return self.__weaponDamage
    
    def attack(self, enemy):
        enemy.takeDamage(self.__weaponDamage)
    
    def takeDamage(self, amount):
        self.__health -= amount
    
    def getHealth(self):
        return self.__health
    
    
## TODO: Create a Monster class that inherits from the Character class.
class Monster(Character):
    def __init__(self, name, description, maxHealth , weaponName, weaponDamage, motivation):
        #TODO
        #Initialize parent class with provided information
        #Also create an attribute for motivation (a string)
        
        super().__init__(name, description, maxHealth, weaponName, weaponDamage)
        self.__motivation = motivation

    def __str__(self):
        #TODO
        #Return a string in the form:
        #<name> is a <description>
        #Weapon: <weapon>
        #Current Health: <health>
        #Motivation: <motivation>
        monsterName = self.getName
        monsterDescr = self.getDescription
        monsterWeapon = self.getWeaponName
        monsterHealth = self.getHealth
        monsterMotiv = self.__motivation

        return f'{monsterName} is a {monsterDescr}' + "\n" + 'Weapon: {monsterWeapon}'+ "\n" + 'Current Health: {monsterHealth}' + "\n" + 'Motivation: {monsterMotiv}'
    
    def react(self):
        #TODO
        #return a string in the form:
        #<name> laughs maniacally.
        
        return f'{self.getName} laughs maniacally.'
    
    def getMotivation(self):
        #TODO
        #Return the monster's motivation
        
        return self.__motivation

## TODO: Create a Hero class that inherits from the Character class.
class Hero(Character):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage, defenseName="", defenseStatus = False):
        #TODO
        #Initialize parent class with provided information
        #Also creates attributes for defense name (string), and defending status (boolean)
        
        super().__init__(name, description, maxHealth, weaponName, weaponDamage)
        self.__defenseName = defenseName
        self.__defenseStatus = defenseStatus

        
    def __str__(self):
        #TODO
        #Return a string in the form:  
        #Our hero <name> is a <description>
        #Weapon: <weapon>
        #Defense: <defenseName>
        #Current Health: <health>
        #Defense Status: <isDefending>

        heroName = self.getName
        heroDescr = self.getDescription
        heroWeapon = self.getWeaponName
        heroDefense = self.__defenseName
        heroHealth = self.getHealth
        heroStat = self.isDefending
        
        return f'Our hero {heroName} is a {heroDescr}' + "\n" + f'Weapon: {heroWeapon}' + "\n" + f'Defense: {heroDefense}' + "\n" + f'Current Health: {heroHealth}' + "\n" + f'Defense Status: {heroStat}'

        
    def react(self):
        #TODO
        #Return a string in the form:
        #<name> charges bravely.
        
        return f'{self.getName} charges bravely.'
        
    def getDefenseName(self):
        #TODO
        #Return the defense name   

        return self.__defenseName
    
    def isDefending(self):
        #TODO
        #Return the defense status
        
        return self.__defenseStatus
    
    def defend(self):
        #TODO
        #Changes defense status to True
      
        self.__defenseStatus = True
        
    def takeDamage(self, amount):
        #TODO
        #Check defense status
        #If it is enabled (True), reduce the amount by 50%, and change the defense status to false.
        #Regardless, apply the final amount to the hero by calling its parent class' takeDamage method.

        if self.__defenseStatus == True:
            amount /= 2
            self.__defenseStatus == False
        else:
            Character.takeDamage(self, amount)
        

# Test your Monster and Hero classes here before you work on the main.py file
if __name__ == "__main__":
    # Milestone 1: Create an instance of Monster and test its methods

    print('*** Testing Monster Class ***')
    monsterTest = Monster ('The Brain', 'Highly intelligent and scheming mouse', 10 , 'Laser beam', 2, 'to take over the world!')
    print(monsterTest)
    print('\nMotivation:', monsterTest.getMotivation())
    print('React:', monsterTest.react())
    print()

    # Milestone 2: Create an instance of Hero and test its methods
    
    print('*** Testing Hero Class ***')
    heroTest = Hero ('Puss in Boots', 'Proud and honorable fighter', 10 , 'sword', 2, 'Cute Eyes tactic ')
    print(heroTest)
    print('\nDefense:', heroTest.getDefenseName())
    heroTest.defend()
    print('Is Defending?', heroTest.isDefending())
    print('React:', heroTest.react())
    print()
    heroTest.takeDamage(3)
    print(heroTest)
    
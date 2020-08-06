''' This program demonstrates how to use classes and objects. '''

class Enemy:
    ''' The Enemy class has life, name and functions that
    do something.'''

    def __init__(self, name, life, level):
        ''' The init function runs on instantiation and sets up all
        attributes. '''

        self._life = life
        self._name = name
        self._level = level
        # add the new enemy object to the enemy_list list
        enemy_list.append(self)

    def get_life(self):
        ''' This function returns the amount of life remaining.'''
        return self._life
    
    def get_name(self):
         ''' This fuction returns the name.'''

         return self._name

    def get_level(self):
         ''' This fuction returns the name.'''

         return self._level

    def attacked(self):
        ''' This fuction subtracts 1 from the objects health. '''
        
        print("Ouch!")
        self._life -= 1
        
def show_all():
    '''This fuction displays details of all enemies in enemy_list'''

    for enemy in enemy_list:
        print(enemy.get_name())

def life_check():
    ''' This function asks the user for an interger, and then returns the names
    of all enemies who have at least that much life left.'''


    # get the input from the user
    check = int(input("Enter amount:"))
    # loop through enemy_list, checking if each object has enough life left
    for enemy in enemy_list:
        if enemy.get_life() > check:
        # print the enemy name if it does
            print(enemy.get_name(), "HP:", enemy.get_life(), "Lvl:", enemy.get_level())
 

def create_enemy():
    ''' This function allows the user to create a new enemy, entering the name
    life for it. '''

    # get the name and life as inputs from the user
    new_name = input("New Enemies name: ")
    new_life = int(input("Enemies health: "))
    # create the new enemy object
    Enemy(new_name, new_life)
# The enemy list stores all enemy objects

enemy_list = []
# create an enemy object and store in variable called enemy1
Enemy("Dr Evil", 40, 4)
Enemy("Darth Vader", 50, 2)
Enemy("The Riddler", 30, 5)


life_check()


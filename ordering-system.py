''' This program is a ordering system for staff to use to add food and drink
to a tab that adds the number of items and charges the total price to the user
'''
 
class Food:
    ''' In the menu each food item is assigned to a type of food it is on the
    the menu. '''
 
    def __init__(self, name, price, course, availibilty):
        ''' Set the attributes of the menu. '''
 
        self._name = name
        self._price = price
        self._course = course
        self._availibilty = availibilty
 
        # add food to the list
        food_list.append(self)
 
    def get_name(self):
        ''' Return the name of the food item'''
        return self._name
 
    def get_price(self):
        ''' Return the price of the food item'''
        return self._price
 
    def get_course(self):
        ''' Return the course of the food item'''
        return self._course
 
    def get_availibilty(self):
        ''' Return the availibilty of the selected food item'''
        return self._availibilty
 
 
class Course:
    ''' Class for the course that food can be assigned too '''
 
    def __init__(self, cname):
 
        self._cname = cname
        # add course to the list
        course_list.append(self)
 
    def get_cname(self):
        ''' Return the course of the food '''
        return self._cname
 
 
 
def generate_food():
    ''' Import the csv file that stores all the food items'''
 
    import csv
    with open('TomsGarage.csv', newline='') as csvfile:
              filereader = csv.reader(csvfile)
              for line in filereader:
                  Food(line[0], int(line[1]), line[2], int(line[3]))
 
 
 
def food_details(cname):
    ''' Print class code, class list and count of students.'''
 
    # Clear the listbox first
    food_listbox.clear()
    # Loop through all food and find the one whose name matches the one we selected
    for food in food_list:
        if food.get_course() == cname:
            food_listbox.append(food.get_name())


def add_food(name):
    '''Adds selected food to final order box'''

    for food in food_list:
        if food.get_name() == name:
            order_listbox.append(food.get_name())

    

 
 
food_list = []
course_list = []
 
# add courses 
Course("Starter")
Course("Main")
Course("Dessert")
 
 
 
# create the application interface
from guizero import App, Text, ListBox, PushButton, TextBox, Box, Combo, error, yesno
 
app = App(title="Tom's Garage", layout="grid")
 
 
cbox = Box(app, grid=[0,0])
fbox = Box(app, grid=[1,0])
obox = Box(app, grid=[2,0])
 
 
 
# This section has the GUI widgets in the cbox area
heading = Text(cbox, text="Click on a Button to select a course")
 
# Loop through the course_list and create a button for each one
 
for course in course_list:
    course_btn = PushButton(cbox, text=course.get_cname(), width=10, height=3)
    course_btn.bg = (129, 217, 222)
    course_btn.text_color = (255, 255, 255)
    course_btn.update_command(food_details, [course.get_cname()])
 
 
food_listbox = ListBox(fbox)
food_listbox.update_command(add_food)
order_listbox = ListBox(obox)
 
# start the program
generate_food()
app.display()

                    

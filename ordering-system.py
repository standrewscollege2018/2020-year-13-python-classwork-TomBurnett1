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
        if food.get_availibilty() == 0:
            if food.get_course() == cname:
                food_listbox.append(food.get_name())
                food_listbox.append(food.get_price())


def add_food(name):
    '''Adds selected food to final order box'''
    # loop through all food and find the one who's name matches the one that we selected
    for food in food_list:
        if food.get_name() == name:
            # appeneding the food name to the order listbox
            ordered_list.append(food)
            order_listbox.append(food.get_name())

def clear_order():
    ''' Clear the listbox'''
    order_listbox.clear()

def undo():
    ''' Undo the last order that was appended to the list '''
    # deleting the last item that was appended to the list
    del ordered_list[-1]
    # updating the listbox to redisplay the context of the listbox
    update_order_listbox()


def update_order_listbox():
    order_listbox.clear()
    # note: need to clear cost of order also
    for food in ordered_list:
        order_listbox.append(food.get_name())

def finish_order():
    finalise_order = app.yesno("Are you done?", "Are you finished with your order")
    if finalise_order == True:
        print("Fin")
    else:
        print("No")



def admin_access():

    '''This brings up a password for the user and if correct, grants access to admin'''
    
    admin_password = app.question("Wait a minute...", "Please enter your password")

    if admin_password == "pass":
        # showing the admin tab where the admin only has access to so they can add, delete and change the availiblity of items
        admin_tab.show()

    else:
        # error for the admin if they enter the wrong password so they are told that it was incorrect and they need to reenter their password
        app.error("WRONG BOY!", "The password was wrong")


def admin_food_details(cname):
    ''' Print class code, class list and count of students.'''
 
    # Clear the listbox first
    admin_food_listbox.clear()
    # Loop through all food and find the one whose name matches the one we selected
    for food in food_list:
        if food.get_course() == cname:
            admin_food_listbox.append(food.get_name())



def admin_functions(name):
    admin_choice = app.question("Hol Up?", "What would you like to do: Type delete to delete the food from the menu or type change to change the availability of the selected food")
    if admin_choice == "delete":
        print("Deleted")
    elif admin_choice == "change":
        print("Changed")
    else:
        app.error("WHAYMINUTE!", "THATS NOT EITHER (*Michael Grunt*)")




food_list = []
course_list = []
ordered_list = []
 
# add courses 
Course("Starter")
Course("Main")
Course("Dessert")
 
 
 
# create the application interface
from guizero import App, Text, ListBox, PushButton, TextBox, Box, Combo, error, yesno, Window, question
 
app = App(title="Tom's Garage", layout="grid")
admin_tab = Window(app, title="Admin Menu", layout="grid")
admin_tab.hide()

 
# box for the course buttons to sit inside
cbox = Box(app, grid=[0,0])
# box for the displayed food to sit inside
# also the admin button for a user to gain admin privilages
fbox = Box(app, grid=[1,0])
# box for the orders that the waiter has selected to display in.
# also the buttons to clear and order
obox = Box(app, grid=[2,0])

afbox = Box(admin_tab, grid=[0,3])
 


# This section has the GUI widgets in the cbox area
 
# Loop through the course_list and create a button for each one
 
for course in course_list:
    course_btn = PushButton(cbox, text=course.get_cname(), width=10, height=3)
    course_btn.bg = (129, 217, 222)
    course_btn.text_color = (255, 255, 255)
    course_btn.update_command(food_details, [course.get_cname()])


admin_button = PushButton(cbox, text="Admin", command=admin_access, width=10, height=3)
admin_button.bg = (129, 217, 222)
admin_button.text_color = (255, 255, 255)

food_listbox = ListBox(fbox)
food_listbox.update_command(add_food)
order_listbox = ListBox(obox)
delete_button = PushButton(obox, text="Undo", command=undo)
clear_button = PushButton(obox, text="Clear", command=clear_order)
finish_button = PushButton(obox, text="Finish", command=finish_order)
cost_lbl = Text(obox, text="Total Cost: total_cost")



for course in course_list:
    course_btn = PushButton(afbox, text=course.get_cname(), width=10, height=3)
    course_btn.bg = (129, 217, 222)
    course_btn.text_color = (255, 255, 255)
    course_btn.update_command(admin_food_details, [course.get_cname()])

admin_food_listbox = ListBox(afbox)
admin_food_listbox.update_command(admin_functions)





# start the program
generate_food()
app.display()

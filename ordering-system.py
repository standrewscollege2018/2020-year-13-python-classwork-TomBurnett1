#Got any gym tips Sir?
''' This program is a ordering system for staff to use to add food and drink
to a tab that adds the number of items and charges the total price to the user
'''

class Food:
    ''' In the menu each food item is assigned to a type of food it is on the
    the menu. '''
    #each food has a name, a price, belongs to a course, and also has an availability
    def __init__(self, name, price, course, availability):
        ''' Set the attributes of the menu. '''
 
        self._name = name
        self._price = price
        self._course = course
        self._availability = availability
        print(self._availability)
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
 
    def get_availability(self):
        ''' Return the availibilty of the selected food item. '''
        return self._availability
 
    def set_availability(self):
        if self._availability == 0:
            self._availability = 1
        else:
            self._availability = 0

 
class Course:
    ''' Class for the course that food can be assigned too '''
    #each course has a name to it
    def __init__(self, cname): 
 
        self._cname = cname
        # add course to the list
        course_list.append(self)
 
    def get_cname(self):
        ''' Return the course of the food '''
        return self._cname
 
 
 
def generate_food():
    ''' Import the csv file that stores all the food items'''
    #imports the csv and opens it thus bringing in the information we need
    #how many days do you gym Sir?
    import csv
    with open('TomsGarage.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            #Each line represents a coloumn in the csv file, 
            Food(line[0], int(line[1]), line[2], int(line[3]))



'''def append_list_as_row(row_contents):
    # Open file in append mode
    with open(TomsGarage.csv, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)'''
 
 
def food_details(cname):
    ''' Print class code, class list and count of students.'''
 
    # Clear the listbox first
    food_listbox.clear()
    # Loop through all food and find the one whose name matches the one we selected
    for food in food_list:
        if food.get_course() == cname and food.get_availability() == 0:
            food_listbox.append(food.get_name())


def add_food(name):
    '''Adds selected food to final order box'''    
    # loop through all food and find the one who's name matches the one that we selected
    for food in food_list:
        if food.get_name() == name:
            # appeneding the food name to the order listbox
            ordered_list.append(food)
            #creates a variable for displaying purposes, it takes the name and the price and formats it in a nice display ( Food - $xxx )
            #Yo seriously how much can you bench Sir?
            foodprice = (food.get_name() + " - $" + str(food.get_price()))
            #adds the vaariable to our order listbox
            order_listbox.append(foodprice)
    #runs an functions to keep the total price correct with what was ordered.
    update_total_price()


def update_total_price():
    #This function keeps the price of the order accurate, it takes each price of food added to the final order listbox and adds it to a total.
    #Starts the price as 0 as to simulate nothing in the order
    total_price = 0
    #for each food in the listbox, the function will loop through until the list is fully looped
    for f in ordered_list:
        total_price += f.get_price()
    cost_lbl.value = "Total price: $" + str(total_price)
            

def clear_order():
    ''' Clear the listbox'''
    if len(ordered_list)==0:
        error("Error", "There is nothing in the order to clear")
    else:
        order_listbox.clear()
        del ordered_list[:]
        update_total_price()

def undo():
    ''' Undo the last order that was appended to the list '''
    # deleting the last item that was appended to the list
    if len(ordered_list)==0:
        error("Error", "There is nothing in the order to undo")
    else:
        del ordered_list[-1]
    # updating the listbox to redisplay the context of the listbox
    update_order_listbox()
    update_total_price()


def update_order_listbox():
    order_listbox.clear()
    # note: need to clear cost of order also
    for food in ordered_list:
        foodprice = (food.get_name() + " - $" + str(food.get_price()))
        order_listbox.append(foodprice)

def finish_order():
    total_price = 0
    for f in ordered_list:
        total_price += f.get_price()

    if len(ordered_list)==0:
        error("Error", "There is nothing in the order to complete")
    else:
        finalise_order = app.yesno("Are you done?", "Are you finished with your order")
        if finalise_order == True:
            new_order = [total_price]
            for food in ordered_list:
                new_order.append(food.get_name())
 


            '''Add new food using details entered. '''
            import csv
            with open('TomsGarage_Reciept.csv', 'a', newline='') as csvfile:
                
                writer = csv.writer(csvfile)

                writer.writerow(new_order)
            ordered_list.clear()
            order_listbox.clear()

        
        else:
            None



def admin_access():

    '''This brings up a password for the user and if correct, grants access to admin'''
    
    admin_password = app.question("Wait a minute...", "Please enter your password")

    if admin_password == "wagamamas":
        # showing the admin tab where the admin only has access to so they can add, delete and change the availiblity of items
        admin_tab.show()

    else:
        # error for the admin if they enter the wrong password so they are told that it was incorrect and they need to reenter their password
        app.error("WRONG BOY!", "The password was wrong")


def admin_food_details(cname):
    '''Print class code, class list and count of students.'''
 
    # Clear the listbox first
    admin_update_listboxes()
    # Loop through all food and find the one whose name matches the one we selected
    for food in food_list:
        if food.get_course() == cname:
            if food.get_availability() == 0:
                admin_listbox_available.append(food.get_name())
            else:
                admin_listbox_unavailable.append(food.get_name())


'''def admin_functions(name):
    admin_choice = admin_tab.question("Hol Up?", "What would you like to do: Type delete to delete the food from the menu or type change to change the availability of the selected food")
    if admin_choice == "delete":
        print("Deleted")
    elif admin_choice == "change":
        print("Changed")
    else:
        app.error("WHAYMINUTE!", "THATS NOT EITHER!")'''

def admin_add_food():
    ''' Add new food using details entered. '''

    if name_text.value == "" or price_text.value == "" or course_text.value == "":
        success_lbl.text_color = (230,50,10)
        success_lbl.value = "Please complete all fields"
        # error(title, text)
        error("ERROR!", "Please complete all fields!")

    else:

        Food(name_text.value, price_text.value, course_text.value, 1)
        new_item = [name_text.value, price_text.value, course_text.value, 1]
        import csv
        with open('TomsGarage.csv', 'a') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(new_item)

        success_lbl.text_color = (30,230,15)
        success_lbl.value = "New Food added"
        name_text.clear()
        price_text.clear()
        course_text.clear()


def admin_delete_food():
    '''Deletes an item off the menu.'''
    
    if admin_listbox_available.value == None:
        delete_lbl.text_color = (230,50,10)
        delete_lbl.value = "Please select a food item to delete"
        # error pop up message
        error("ERROR!:", "Please select a food item to delete")
    else:
        # check if they really want to delete the selected student using a yes or no popup 
        check_delete = yesno("ALERT!", "Are you sure you want to delete this food item?")
        if check_delete == True:
            # Get the index of the food item we are deleting (position in ordered_list)
            i=0
            for food in food_list:
                if food.get_name() == admin_listbox_available.value:   
                    del food_list[i]
                else:
                    i += 1
            # delete the objects from student names and student list
            
            import csv
            with open('TomsGarage.csv', 'w', newline='') as csvfile:

                writer = csv.writer(csvfile)
                for f in food_list:
                    new_item = [f.get_name(), f.get_price(), f.get_course(), f.get_availability()]
                    writer.writerow(new_item)
            delete_lbl.text_color = (210, 45, 17)
            delete_lbl.value = "Food item has been deleted"
            admin_update_listboxes()

def admin_change_availability():
    ''' Change availability of selected item. '''

    if admin_listbox_available.value == None and admin_listbox_unavailable.value == None:
        delete_lbl.text_color = (230,50,10)
        delete_lbl.value = "Please select a food item to change"
        # error pop up message
        error("ERROR!:", "Please select a food item to delete")
    elif admin_listbox_available.value != None:
        for food in food_list:
            if food.get_name() == admin_listbox_available.value:   
                food.set_availability()
                import csv
                with open('TomsGarage.csv', 'w', newline='') as csvfile:

                    writer = csv.writer(csvfile)
                    for f in food_list:
                        new_item = [f.get_name(), f.get_price(), f.get_course(), f.get_availability()]
                        writer.writerow(new_item)
                admin_update_listboxes()
    else:
        for food in food_list:
            if food.get_name() == admin_listbox_unavailable.value:   
                    food.set_availability()
                    
                    import csv
                    with open('TomsGarage.csv', 'w', newline='') as csvfile:

                        writer = csv.writer(csvfile)
                        for f in food_list:
                            new_item = [f.get_name(), f.get_price(), f.get_course(), f.get_availability()]
                            writer.writerow(new_item)
                    admin_update_listboxes()

def admin_update_listboxes():
    ''' Update the available and unavailable listboxes. '''

    admin_listbox_available.clear()
    admin_listbox_unavailable.clear()



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
# box for the orders that the waiter has selected to display in, also the buttons to clear and order  
obox = Box(app, grid=[2,0])

# Admin row 1
aabox = Box(admin_tab, grid=[1,0])
abbox = Box(admin_tab, grid=[2,0])
acbox = Box(admin_tab, grid=[3,0])
agbox = Box(admin_tab, grid=[4,0])
 
# Admin row 2

adbox = Box(admin_tab, grid=[1,1])
aebox = Box(admin_tab, grid=[2,1])
afbox = Box(admin_tab, grid=[3,1])

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
order_listbox = ListBox(obox, width=200, height=200)
delete_button = PushButton(obox, text="Undo", command=undo)
clear_button = PushButton(obox, text="Clear", command=clear_order)
finish_button = PushButton(obox, text="Finish", command=finish_order)
cost_lbl = Text(obox, text="Total Cost:")

success_lbl = Text(afbox)


for course in course_list:
    course_btn = PushButton(aabox, text=course.get_cname(), width=10, height=3)
    course_btn.bg = (129, 217, 222)
    course_btn.text_color = (255, 255, 255)
    course_btn.update_command(admin_food_details, [course.get_cname()])

admin_listbox_available = ListBox(abbox)
admin_listbox_unavailable = ListBox(acbox)

# This section has the GUI widgets in the admin_add_food area
heading = Text(aebox, text="Add new Food")
name_lbl = Text(aebox, text="Name")
name_text = TextBox(aebox)
price_lbl = Text(aebox, text="Price")
price_text = TextBox(aebox)
course_lbl = Text(aebox, text="Course")
course_text = Combo(aebox, options=['Starter','Main','Dessert'])
add_btn = PushButton(aebox, text="Add Food", width=20,command=admin_add_food)


delete_btn = PushButton(agbox, text="Delete", width=5, command=admin_delete_food)


delete_lbl = Text(agbox)
availability_btn = PushButton(agbox, text="Change", width=5, command=admin_change_availability)



# start the program
generate_food()
app.display()

''' This program is a student management system, allowing users to add student
records and run reports.'''
from guizero import App

class Student:
    ''' The student class has a name, age, phone number, gender and a list classes
    All students are automatically set as enrolled when instantiated.
    Each student belongs to sutdent_list. '''

    def __init__(self, name, age, phone, gender, classes):
        ''' This init function runs on instatiation and sets up all attributes. '''

        self._name = name
        self._age = age
        self._phone = phone
        self._gender = gender
        self._classes = classes
        self._enrolled = True
        # add the new student object to the student_list list
        student_list.append(self)

    def get_name(self):
        ''' THis function returns the name of the student. '''
        return self._name

    def get_age(self):
        ''' This function returns the age of the student. '''
        return self._age

    def get_phone(self):
        ''' This function returns the phone number of the student. '''
        return self._phone

    def get_gender(self):
        ''' This function returns the gender of the student. '''
        return self._gender

    def get_classes(self):
        ''' This fuction returns the list of classes assigned to a student. '''
        return self._classes
    
    def get_enroll(self):
        return self._enroll

def generateStudents():
    import csv
    with open('myRandomStudents.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            classes=[]
            i=4
            while i in range (4, 9):
                classes.append(line[i])
                i+=1
            Student(line[0], int(line[1]), line[2],line[3], classes)

def add_student():
    ''' THis function allows users to add new students to the list. '''

    # get the name, age, phone number, gender, and what classes they have
    print("Please enter the students details:")
    new_name = input("Students name:")
    # ask for student age. Use while loop to ensure we get an integer
    ask_age = True
    while ask_age == True:
        try:
            new_age = int(input("Students age:"))
            ask_age = False
        except:
            print("Invaild input. Please enter an integer.")
            
    new_phone = int(input("Students Phone number:"))
    new_gender = input("Students gender:")
    new_classes = []
    add_class = True
    while add_class == True:
        new_class = input("Please enter the students classes")
        if new_class == "end" or new_class=="End":
            add_class = False
        elif new_class == "":
            print("Please enter a class code.")
        else:
            new_classes.append(self)
    # create the new student object
    Student(new_name, new_age, new_phone, new_gender, new_classes)

def class_list():
    ''' Get list of students in selected class. '''

    class_code = input("Enter class code:")
    total = 0
    for student in student_list:
        if class_code.upper() in student.get_classes():
            print(student.get_name())
            total+= 1
    print("Total Students:", total)

    
def show_all():
    ''' This function shows the names of all students. '''

    for student in student_list:
        print(student.get_name())


def search():
    ''' Display details of student. '''
    name = input("Enter the students name:")
    total = 0
    for student in student_list:
        if name.lower() in student.get_name().lower():
            total+= 1
            show_details(student)
    print("Total of students:", total)

def show_details(student_to_show):
    ''' Display details of student. '''

    print("----------------")
    print(student_to_show.get_name())
    print("----------------")
    print("Age:", student_to_show.get_age())
    print("Phone Number:", student_to_show.get_phone())
    print("Gender:", student_to_show.get_gender())
    print("Classes:", student_to_show.get_classes())
    print("")
    
################################################################################################

class Teacher:
    ''' The teacher class that stores data in the teach_list class '''

    def __init__(self, name, classes):
        ''' This init function runs on instatiation and sets up all attributes. '''

        self._name = name
        self._classes = classes

        # add the new student object to the teacher_list list
        teacher_list.append(self)

    def get_name(self):
        ''' This function returns the name of the student. '''
        return self._name

    def get_age(self):
        ''' This function returns the age of the student. '''
        return self._age

def add_teacher():
    ''' THis function allows users to add new students to the list. '''

    # get the name, age, phone number, gender, and what classes they have
    print("Please enter the teachers details:")
    new_teacher = input("Teachers name:")
    # ask for student age. Use while loop to ensure we get an integer

    new_gender = input("Students gender:")
    new_classes = []
    add_class = True
    while add_class == True:
        new_class = input("Please enter the Teachers Classes:")
        if new_class == "end" or new_class=="End":
            add_class = False
        elif new_class == "":
            print("Please enter a class code.")
        else:
            new_classes.append(self)
    # create the new student object
    Teacher(new_name, new_gender, new_classes)


    

# The student list stores all student data
student_list = []
teacher_list = []
# create an student object and store in variable called student
Student("Tom", 17, 226747810, "Male", ["Digital Technologies", "Mathetmatics", "English", "Art Design", "Art Photography"])
Student("Leon", 17, 224743453, "Male", ["Digital Technologies", "Mathetmatics", "English", "Geography", "Science"])

    
run_program = True
while run_program == True:
    print("Main Menu\n----------")
    print("1. Search")
    print("2. Add Student")
    print("3. Class List")
    print("4. Quit")
    selection = int(input("Selection:"))
    if selection == 1:
        search()
    elif selection == 2:
        add_student()
    elif selection == 3:
        class_list()
    elif selection == 4:
        run_program = False
    else:
        print("Enter a number from 1-4")



''' This program is the starter code for the student management system that we are building a GUI for
 It should be used for each new task. 
 It has class definitions and generates all students and teachers, otherwise has no functionality.
 You will need to have this saved in the same folder as the teachers.csv and myRandomStudents.csv files.
 '''




class Teacher:
    ''' Teachers have a name and a class they are attached to. '''
    
    def __init__(self, tname, tclass):
        ''' Set the attributes of the new teacher. '''
        
        self._tname = tname
        self._tclass = tclass
        # add new teacher to the list of all teachers
        teacher_list.append(self)

    def get_tname(self):
        ''' Return name of teacher. '''
        
        return self._tname
    
    def get_tclass(self):
        ''' Return the class. '''
        
        return self._tclass

class Student:
    ''' The student class has a name, age, phone number, gender and a list of classes they are enrolled in. 
    All students are automatically set as enrolled when instantiated.
    Each student belongs to student_list. '''
    
    def __init__(self, name, age, phone, gender, classes):
        ''' This function sets the attributes of the new student.
        It sets every student to being enrolled by default. 
        It also adds the new student to student_list. '''
        
        self._name = name
        self._age = age
        self._phone = phone
        self._gender = gender
        self._classes = classes
        self._enrolled = True
        
        student_list.append(self)
        student_names.append(name)
        
    def get_name(self):
        ''' Return the name of the student. '''
        
        return self._name

    def get_age(self):
        ''' Return the age of the student. '''
        
        return self._age
    
    def get_phone(self):
        ''' Return the phone number of the student. '''
        
        return self._phone
    
    def get_gender(self):
        ''' Return the gender of the student. '''
        
        return self._gender
    
    def get_classes(self):
        ''' Return the list of classes the student is signed up for. '''
        
        return self._classes
    
    def get_enrolled(self):
        ''' Return whether or not a student is currently enrolled. '''
        
        return self._enrolled

def generate_teachers():
    ''' Import teachers from the teachers csv file. '''
    
    import csv
    # Notice the encoding setting. This avoids the byte order mark (BOM)
    # appearing. This looks like: ﻿
    with open('teachers.csv', encoding="utf-8-sig", newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            Teacher(line[0], line[1])

def generate_students():
    ''' Import students from the myRandomStudents csv file. '''
    
    import csv
    with open('myRandomStudents.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            classes=[]
            i=4
            while i in range(4, 9):
                classes.append(line[i])
                i+=1
            Student(line[0], int(line[1]), line[2],line[3], classes)

  
# Empty lists to store all teachers and students
teacher_list = []     
student_list = []

# List of names of the students
student_names = []

# Create some students to start with
Student("Jack", 16, "0273956577", "Male", ["GRA", "MAT", "ENG"])
Student("Jill", 15, "0271111111", "Female", ["MAT", "ART"])
Student("Matt", 17, "0217771117", "Male", ["MAT", "PHY", "ART"])

generate_teachers()
generate_students()

def display_details():
    ''' Display details of selected student. '''
    
    for student in student_list:
        if student_listbox.value == student.get_name():
            student_name.value = student.get_name()
            student_age.value = "Age:" + str(student.get_age())
            student_phone.value = "Phone: " + str(student.get_phone())


def search():
    ''' Get names of students matching the search. '''
    
    # Clear the search box
    student_listbox.clear()
    
    for student in student_list:
        
        if search_textbox.value.lower() in student.get_name().lower():
            
            student_listbox.append(student.get_name())
    
    
def add_student():
    ''' Add new student using details entered. '''

    if name_text.value == "" or age_text.value == "" or phone_text.value == "" or class_listbox == None:
        success_lbl.text_color = (230,50,10)
        success_lbl.value = "Please complete all fields"
        # error(title, text)
        error("ERROR!", "Please complete all fields!")

    else:
        Student(name_text.value, age_text.value, phone_text.value, gender_combo.value, class_listbox.value)
        success_lbl.text_color = (30,230,15)
        success_lbl.value = "New Student added"
        name_text.clear()
        phone_text.clear()
        age_text.clear()
        class_listbox.clear()
        name_text.focus()
    
def delete_student():
    ''' Deleting a selected student '''

    if student_listbox.value == None:
        delete_lbl.text_color = (230,50,10)
        delete_lbl.value = "Please select a student to delete"
        # error pop up message
        error("ERROR!:", "Please select a student to delete")
    else:
        # check if they really want to delete the selected student using a yes or no popup 
        check_delete = yesno("ALERT!", "Are you sure you want to delete this student?")
        if check_delete == True:
            # Get the index of the sutdent we are deleting (position in student_names)
            i = student_names.index(student_listbox.value)
            # delete the objects from student names and student list
            del(student_names[i])
            del(student_list[i])
            delete_lbl.text_color = (210, 45, 17)
            delete_lbl.value = "Student has been deleted"
            search()
        
    
    


    
# create the application interface
from guizero import App, Text, ListBox, PushButton, TextBox, Box, Combo, error, yesno

app = App(title="Student management system", layout="grid")

# Set up the Box areas for our layout
add_box = Box(app, grid=[0,0], layout="grid")
search_box = Box(app, grid=[1,0])
delete_box = Box(app, grid=[2,0])

# This section has the GUI widgets in the add_box area
heading = Text(add_box, text="Add new student", grid=[0,0])
name_lbl = Text(add_box, text="Name", grid=[0,1])
name_text = TextBox(add_box, grid=[1,1])
age_lbl = Text(add_box, text="Age", grid=[0,2])
age_text = TextBox(add_box, grid=[1,2])
phone_lbl = Text(add_box, text="Phone", grid=[0,3])
phone_text = TextBox(add_box, grid=[1,3])
gender_lbl = Text(add_box, text="Gender", grid=[0,4])
gender_combo = Combo(add_box, options=["Male", "Female", "Other"], grid=[1,4])
class_lbl = Text(add_box, text="Classes", grid=[0,5], align="top")
class_listbox = ListBox(add_box, ["GRA", "BIO", "PHY", "MAT", "DTC", "ART", "ENG", "XYZ"], grid=[1,5], multiselect=True)
add_button = PushButton(add_box, text="Add student", grid=[0,6, 2, 1], width=20,command=add_student)
success_lbl = Text(add_box, grid=[0,7,2,1])

# This section has the GUI widgets in the delete_box area


delete_button = PushButton(delete_box, text="Delete Student", grid=[0,0], width=20, command=delete_student)
delete_lbl = Text(delete_box)


# This is section where you add any GUI widgets to the search_box area
heading = Text(search_box, text="Search", color=(210, 45, 17))

search_textbox = TextBox(search_box)
search_button = PushButton(search_box, text="Search", command=search)

student_listbox = ListBox(search_box, command=display_details)

student_name = Text(search_box)
student_age = Text(search_box)
student_phone = Text(search_box)
student_gender = Text(search_box)

# Start the program
app.display()

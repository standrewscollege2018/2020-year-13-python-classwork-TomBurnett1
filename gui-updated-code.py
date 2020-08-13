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
    # appearing. This looks like: ï»¿
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
    student_listbox.clear()
    student_name.clear()
    student_age.clear()
    student_phone.clear()
    
    for student in student_list:
        if search_textbox.value.lower() in student.get_name().lower():
            student_listbox.append(student.get_name())

        







      
# create the application interface
from guizero import App, Text, ListBox, PushButton, TextBox
 
app = App(title="Student management system")
 
# This is section where you add any GUI widgets
heading = Text(app, text="List of Students", color=(210, 45, 17))

# Search Engine 
search_textbox = TextBox(app)
search_button = PushButton(app, text="Search", command=search)
 
 
student_listbox = ListBox(app, command=display_details)
 
student_name = Text(app)
student_age = Text(app)
student_phone = Text(app)
student_gender = Text(app)
 
# Start the program
app.display()

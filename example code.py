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
    # appearing. This looks like: 
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

def teacher_details(tname):
    ''' Print class code, class list and count of students.'''

    # Clear the listbox first
    class_listbox.clear()
    # Loop through all teachers and find the one whose name matches the one we selected
    for teacher in teacher_list:
        if tname == teacher.get_tname():
            # Display teacher name
            teacher_label.value = tname
            # Get the class code
            class_label.value = "Class: " + teacher.get_tclass()
            tclass = teacher.get_tclass()
            # Count up how many students are enrolled
            count = 0
            for student in student_list:
                if tclass in student.get_classes():
                    count += 1
                    # If student is enrolled, add their name to the listbox
                    class_listbox.append(student.get_name())
            class_count_label.value = "Enrolled: " + str(count)         

def student_details():
    ''' Display student details in a new window. '''

    details = Window(app, title=class_listbox.value, width=350, height=150)
    name_label = Text(details)
    age_label = Text(details)
    phone_label = Text(details)
    classes_label = Text(details, text="Classes: ")
    for student in student_list:
        if class_listbox.value == student.get_name():
            name_label.value = "Name: " + student.get_name()
            age_label.value = "Age: " + str(student.get_age())
            phone_label.value = "Phone: " + str(student.get_phone())
            student_classes = student.get_classes()
            for c in student_classes:
                classes_label.value += c + " "


# Empty lists to store all teachers and students
teacher_list = []     
student_list = []

# Create some students to start with
Student("Jack", 16, "0273956577", "Male", ["GRA", "MAT", "ENG"])
Student("Jill", 15, "0271111111", "Female", ["MAT", "ART"])
Student("Matt", 17, "0217771117", "Male", ["MAT", "PHY", "ART"])

generate_teachers()
generate_students()

# Import all the classes we need from Guizero
from guizero import App, PushButton, Text, ListBox, Window

# create the application interface
app = App(title="Student management system", layout="grid")

# This is section where you add any GUI widgets

# Loop through the teacher_list and create a button for each one
row=0
column=0
for teacher in teacher_list:
    # We only want 3 columns of buttons
    if column == 3:
        column = 0
        row += 1
    else:
        # Each button displays the name of the teacher
        teacher_btn = PushButton(app, text=teacher.get_tname(), width=10, height=3, grid=[column,row])
        # We use update_command() instead of command because we want to send a parameter to the teacher_details() function
        teacher_btn.update_command(teacher_details, [teacher.get_tname()])
        column += 1

teacher_label = Text(app, grid=[0, row+1])
class_label = Text(app, grid=[0, row+2])
class_listbox = ListBox(app, grid=[0, row+3])
class_listbox.update_command(student_details)
class_count_label = Text(app, grid=[0, row+4])

# Start the program
app.display()

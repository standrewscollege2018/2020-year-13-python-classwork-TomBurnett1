''' Example of how widgets work and gui's.'''

# import the widgets we need from guizero
from guizero import App, Text

# create the main window
app = App(layout="grid",title="My first guizero app", bg=(200,200,200), height=400, width=600)


# Create a text label
# the first parameter is the location of the widget
header = Text(app, grid=[0,0], text="welcome to my program", font="Calibri", size=15, color="blue")

label = Text(app, grid=[1,0], text="Hi How are you?")






# starts the program by displaying the main window
app.display()

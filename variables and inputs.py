''' This program demonstrates variables and inputs. '''

# variables can store one pice of information
# name them sensibley, use lower case and underscores between word (snakecase)
first_name = "John"
print("Hello {}".format(first_name))


# we can do maths operations on variables that have numbers
number = 5
print(number*2)

# we use input() to get input from the user
# unput should be assigned to a variable
name = input("What is your name?")

print("Hello {}".format(name))

# by default, input() takes string (text) as input
# we can "cast" a variable, setting it to a data type
age = int(input("Enter your age:"))

print("You are {} years old".format(age))

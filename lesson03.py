#!/usr/bin/env python3

# Now that we've learned how to output text, let's also learn how to read text
# (we call it input) from our user!

# Python has a handy function called input() to read text from the user. You
# can pass in a "prompt" as an "argument" to the input() function.

# Before we get into the specifics, let's go back a bit and learn a bit about
# functions.

# Functions are a way for programmers to group together many different
# operations that can be repeated. Functions optionally take in arguments, and
# can  optionally return a value at the end.

# Let's look back at the print() function for a moment. The print() function
# took in a variable or a string as its argument.

# When you type in print( in your IDE, it should show you all the arguments
# that print() takes in - it has a "values" argument, along with some optional
# arguments that can be passed into this function.

# When the Python authors wrote the print() function, they specified that
# print() should take in the "values" argument. In their function, they use the
# "values" argument as a "variable" to tell the computer to output that variable
# to the computer screen.

# Depending on the argument being passed in, the print() function will behave
# differently.

# If I do:

print("my name is")

# I get a very different outcome from when I do:

print("your name is")

# Functions can do several different things (in print's case, it does one
# thing - it outputs text onto the computer screen). Some functions return
# a value, while others don't.

# The input() function takes in an argument as well - they take in argument
# called "prompt". These names are just helpful "tips" for programmers like
# you and I to know what these arguments are for.

# Since the input() function returns a value at the end, we can take that
# value and assign it to a variable. We can do that like this:

name = input('What is your name: ')

# The input() function "prompts" (or "asks") the user what their name is.
# When the user enters their name onto the computer screen and hits "Enter",
# the function returns back a value containing the string that the user
# entered.

# What we then do is store that value in the "name" variable, so that we can
# use it later on in our program!

# When we want to force a string to an integer value, Python also gives us a
# function to do that. We can use the int() function to "force" a value to
# become a string - if it's not a string, Python will choke and exit the
# program:

some_string = '527263'
some_number = int(some_string) # this forces the string '527263' to become an
                               # int so that we can perform calculations on it
# [Crazymonkeycoder]: Note to self: the str() function can change a int to a string again
# so for example...
some_new_string = str(some_number) 
print(some_new_string + 'yay')
# By the way... 
# if you try to add a int to a string, this will happen
#Traceback (most recent call last):
  #File "/Users/(name)thepurplepig/Desktop/codelab/coding-tutorial/lesson04.py", line 50, in <module>
    #print("The sum is: " + a)
#TypeError: can only concatenate str (not "int") to str
# Ya you see
################################################################################
# LESSON 3
################################################################################
# Now that we got the user's name, let's also ask their age and output it to
# them (just in case they forgot!).

# Ask the user "What is your age: " and assign it to the variable "age".

# Then, print out:
# Your name is: <their actual name>

# Finally, we'll also remind them their age by printing out:
# You are <their actual age> years old!

# Remember, you can use the + operator to combine text!

age = input("What is your age: ")
print("Your name is: " + name + "\n" + "You are: " + age + " years old!" + '\n')
print(some_number+2)
print('I\'m a boy') 
print('"I\'m ALIVE," Frankenstine said.')
print("\"I'm ALIVE,\" Frankenstine said.")
print(some_number+2)

################################################################################
# LESSON 3 - EXTRA CREDIT!
################################################################################
# Try to print out the following line:
#
# "I'm ALIVE," Frankenstein said.

#!/usr/bin/env python3

# Now that you know how to write comments, let's get into some real
# programming! We're going to learn how to use the print() function.

# If you remember from before, the print() function is used to "print" some
# text onto the screen. Continuing from our last lesson, we're going to...
# You guessed it - print the Lorem Ipsum text onto the screen!

# To print from your program, you have to pass the print() function some
# string. A "string" is a list of characters (think of them as things like
# your ABCs, numbers like 123s, and special characters that you see on your
# keyboard like !@#$).

# Before we can pass in a string to a function, we have to "create" a
# variable to hold that string.

# A variable is just a piece of memory that the program assigns to hold some
# piece of information. The information that it holds can be a poem, a
# number that's being used in a complex calculation, or an "object" that holds
# data and instructions for performing *even more complex* calculations!

shakespeare_birthday = 1564 # this just assigns a number to the variable
first_president = 'George Washington' # this assigns a string to the variable

# To create a variable in Python, all we do is use the assignment operator.
# An operator is just like the mathematical symbols that you learned in
# elementary: +-*/=

# In Python, the assignment operator is =. When we create a variable, we always
# need a *unique* name for the variable:

best_cat = 'Garfield'

# The name can be anything, but we should try to stay organized and create
# names that make sense for future readers. Variable names must start with a
# lower case letter, an upper case letter, or an underscore (_), but can be
# followed by the alphabet, numbers, or an underscore.

_tH1S__1S____a__VaL1d__nAm3___4_PyTh0N = 'but please use something sane...'

# Variables can also be re-assigned to something else:

best_cat = 'Cornish Rex'

# Once you create a variable, we can print it to the screen so that we can see
# the creation you've made!

# To print text onto the screen, all you need to do is pass in the variable
# that you created to the print() function:

print(best_cat) # this will print "Cornish Rex" since that was the last
                # assignment we made to the variable "best_cat"

# You can also pass in the string directly into the print() function if you
# don't care about storing it in a variable (for example, you might not be
# doing anything special with the text):

print('The best cat in the world is.......')
print(best_cat)

# Print will always create a "line break" at the end of your string, so that
# every print() function is on a new line:

print('PPP   Y   Y  TTTTT  H  H   OO   N    N')
print('P  P   Y Y     T    H  H  O  O  NN   N')
print('PPP     Y      T    HHHH  O  O  N  N N')
print('P       Y      T    H  H  O  O  N   NN')
print('P       Y      T    H  H   OO   N    N')

# You can force a new line in the middle of the string to appear by inserting
# "\n" in your string:

print('\n\n      /\\_/\\\n /\\  / o o \\\n//\\\\ \\~(*)~/\n`  \\/   ^ /\n   | \\|| ||\n   \\ \'|| ||\n    \\)()-())\n')

# The \ character (also called the backslash) is a special character in
# strings, since it can be used to store and output characters (like a new
# line). It can be used for these special situations:
# * To emit a quote (') character, use \'
# * To emit a backslash (\) character, use \\
# * To emit a new line, use \n
# * To emit a tab, use \t

print('Quote: -->\'<--')
print('Backslash: -->\\<--')
print('New line: -->\n<--')
print('Tab: -->\t<--')

# To combine text, you can use the + operator like so:

print('I think ' + best_cat + ' is the best cat in the world!')

################################################################################
# LESSON 2
################################################################################
# Let's create a new variable called 'placeholder_text' and assign it the first
# paragrah of the Lorem Ipsum text. Once we assign it, let's print it out!
placeholder_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
print(placeholder_text)
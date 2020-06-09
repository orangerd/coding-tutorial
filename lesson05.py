#!/usr/bin/env python3

# Today, we're going to start off by learning about conditionals. Python has
# several conditional operators, but we're just going to learn about the basic
# if-elif-else syntax today.

# First, let's go through the "if" conditional syntax. "if" in Python allows
# you to specify what to do *if* a condition has been met. Just like we say in
# English, "If I have a million dollars, I'd buy a ticket to Mars," Python has
# the ability to change its behavior based on a certain condition was
# satisfied or not (by the way, even if I had a million dollars, I probably
# wouldn't go to Mars :-P).

# Let's take a look at how an "if" condition looks like in Python:

x = 5
y = 10

if x == 5:
  print('Yup, x is equal to 5!')

if x < y:
  print('Double yup!!')
  print("You're absolutely correct that x is less than y since 5 < 10!")

if x > y:
  print('WOAH, you must be going CrAzY!!!')

# Let's break this down a bit. First, we created 2 variables, x and y. We
# didn't explicitly learn this, but when we say "x = 5", we're *assigning*
# the value of 5 to x. That tells the computer to keep the value of 5 whenever
# we reference the variable 'x' later on in our program. It's like giving a
# name to a person called 'x', and telling them that their age is 5 (or maybe
# that 5 represents how many dollars he/she has, or maybe the number of
# siblings they have, or...).

# We then get to our first "if" condition - "if x == 5:". Yowza! That syntax
# looks very similar to our assignment syntax! What the...

# An "if" condition in Python is always ALWAYS AAALLLWWWAAAYYYSSS followed by
# something called an "expression". An expression is something like:
# * x is equal to 5
# * x is greater than y
# * x is less than y
# * x + y is greater than 10

# It's something Python can use to "check" whether something is true or false.
# But, the syntax "x = 5" was already taken for "assignment" (and assignment
# isn't something Python can "check" - how in the world do you check that
# "x, you are now 5 years old!" as being true or false...?! That's just a
# declaration that they *are* indeed 5 years old!). So instead, Python uses
# two equal signs (we call it "equal-equal") to check whether "x" is indeed
# 5 years old or not (because anyone less than 5 isn't allowed on the
# merry-go-round!).

# When we write "if x == 5:", what we're really saying is "check to see that
# the value of 'x' is really really really equal to 5". If so, we go straight
# down to something called the "statements".

# SCREEEEEECH! But, before we get to "statements", there's one REALLY crucial
# thing that many people forget when writing a conditional expression! Look
# closely at that syntax:
#
# if x == 5:
#
# GASP! There's this double dot thing at the end (it's called a "colon"). This
# is an important part of the conditional expression in Python. Without it,
# Python will scream and yell and holler at you like it's the end of the world.
# Without it, Python doesn't know whether you're continuing your sentence (the
# conditional expression) or if you're done with it. It's like saying "if I
# have a million ..." - Python just thinks you've dropped dead before you
# finished that sentence of yours!

# And, now we're back to our "statements". A statement (or a "block of
# statements") is an indented piece of code that Python executes if the
# conditional expression was indeed true (was 'x' really equal to 5 when I came
# across that condition???). When Python encounters the conditional expression:
#
# if x == 5:
#
# it first checks to see whether that was true or not (we obviously know it's
# true, since we just assigned "x = 5" a few lines before). If so, it runs all
# the code that's underneath that "if" statement.

# But, how does Python know when to stop executing stuff if that condition was
# true? That's where indentation comes in.

# In Python, we use indentation (just like in your English essays - you use 2
# spaces before the start of a paragraph), but Python doesn't really care if
# you use 2 spaces, 4 spaces, 10 spaces, or 100 spaces (seriously, don't do
# that, though). As long as you're consistently using the same number of spaces
# at the beginning of the line, it considers all those statements to be part
# of the same block.

# So, when we have a block of code like this:

if x < 10:
  print('Okie dokie, we passed the first test...\n')
  if x > 1:
    print('Phew, second test passed as well...\n')
    if y == 10:
      print('Wow, all of that stuff was true!!!')
      print("Isn't it amazing when things JUST WORK?!")
      print('Yeah, it truly is amazing!!!')

# Python first checks to see whether "x < 10" is true (it should be, since we
# didn't "re-assign" or set a new value for x - it's still 5 just like it was
# about a 100 lines before).
# 1st block:
#   It prints out that we passed our first test.
#   Then, Python checks if "x > 1". That's true as well.
#   2nd block:
#     It prints out that we passed our second test.
#     Then, Python checks if "y == 10". Ultimate test! That's true also!
#     3rd block:
#       It prints out that the world is amazing
#       And that when things work
#       It truly is MAGICAL!

# Now that we know how "if" conditional expressions and statement blocks work,
# let's move onto some of the easier bits and pieces of Python conditionals.

# We know that Python checks the conditional expression when it encounters an
# "if". What if we want to tell Python to do something else when that
# conditional expression was not true (we call it "false")???

# Here comes "else" to the rescue! When the conditional expression that it
# evaluates doesn't end up being true, we can tell Python to do some other
# things instead. We use the "if-else" syntax to tell Python what to do:

if x > 10:
  print("Wow, that's odd... when did x change its value?!")
  print('Is the universe still... fine???')
else:
  print("Nope, everything's normal")
  print("x hasn't changed its age yet")

# When Python evaluates the conditional expression "if x > 10", it checks
# whether x (which still has the value 5) is greater than 10. That's obviously
# not true, and we provide Python with an alternative set of instructions to
# execute in case it's false.

# Python will go through the block of statements (again, it's indented to tell
# Python where the paragraph ends) under the "else" clause to tell us that
# the universe hasn't collapsed yet (phew!).

# What if we wanted to tell Python to try out multiple things. Like, maybe:
# * if you're 15 and over, you can ride the roller coaster
# * if you're 10 and over, you can enter the haunted house
# * if you're 5 and over, you can ride the merry-go-round
# * otherwise, you can head on over to the sandbox

# That's where the if-elif-else statement comes in handy! This is what it looks
# like:

if x >= 15:
  print('You can ride the roller coaster')
elif x >= 10:
  print('You can enter the haunted house')
elif x >= 5:
  print('You can ride the merry-go-round')
else:
  print('Sorry, you can only play in the sandbox')

# When Python executes this, it checks to see what the value of 'x' is. If it
# matches the first condition (x >= 15), it'll execute the statement block
# under that conditional expression.

# One thing to note here - if it matches one of those conditional expression,
# Python won't go and check any of the other conditional expressions. Python
# always evaluates things top-to-bottom (the first one that matches wins!).

# So, if x was 217538, even though it would match *every single one* of those
# conditioanl expressions (because 217538 >= 15, and 217538 >= 10, and
# 217538 >= 5 as well - OBVIOUSLY), it would only execute the first statement
# block because that's the first conditional expression that matched.

# If we wanted to evaluate multiple of these conditional expressions instead
# of just the "first one wins", we can just split our conditional expressions
# into multiple "if" statements instead:

if x >= 15:
  print('You can eat a steak')
if x >= 10:
  print('You can eat a hamburger')
if x >= 5:
  print('You can eat ice cream')
if x >= 0:
  print('You can drink milk')

# Now, if x was 217538, we'd print out that x can eat a steak, hamburger, ice
# cream, and drink milk!

# It's all about understanding how/when to use certain conditional syntaxes!

################################################################################
# LESSON 5
################################################################################
# We're going to give our odd/even calculator another spin.

# First, let's get a number from our user by prompting them:
# "Enter a number: "

# We'll store that in a variable, then tell them whether or not the number was
# even or odd. If it's even, we'll print "EVEN", otherwise we'll print "ODD".

# Do you still remember how we find out if a number is even or odd? Look back
# at lesson04.py if you forgot!

#!/usr/bin/env python3

# Now, let's talk a little bit about loops. Loops are a way we can ask Python
# to do some repetitive stuff. A loop is quite simple - all it does is does
# the same thing over, and over, and over, and over, and over again.

# Let's dive right into what it looks like (and there are many variations of
# loops, so this isn't the only one we're going to learn about):

#for x in range(0, 5, 2):
  #print(x)

# There's a couple of new concepts here - let's break it apart a bit.

# First, we have this syntax called the "for-in" loop. The "for-in" loop is
# a type of loop where it assigns a variable with some value every time it
# goes through the loop. In the case above, it assigns a value to the variable
# "x" every time it goes through the loop.

# But what value does it assign to "x"? That's where the "range()" function
# becomes important.

# The range() function takes in a starting number (also called the starting
# index), and adds 1 to it UNTIL it reaches the 2nd argument (remember, an
# argument is a value passed into a function - the 0 is the 1st argument to
# range(), while the 5 is the 2nd argument to range()).

# Simply put, all this program is doing is:

# 1st loop
#x = 0
#print(x)

# 2nd loop
#x = x + 1 # x = 1
#print(x)

# 3rd loop
#x = x + 1 # x = 2
#print(x)

# 4th loop
#x = x + 1 # x = 3
#print(x)

# 5th loop
#x = x + 1 # x = 4
#print(x)

# And that's the end of it - but why didn't it print out 5, then? That's
# because secretly (behind-the-scenes) Python is doing this for every loop:

#if x < 5:
  #print(x)
  #x = x + 1

# It checks whether x < 5, and if that conditional expression evaluates to
# true, it'll print the value of x and add 1 to x (we call this an increment).

# Now, range() actually takes in a 3rd argument called the "step" value.
# Instead of adding 1 to x every time, we can add 2 (or 3, or 4, or any value)
# to x every time we enter this loop.

# Take a look at this:

# for x in range(10, 0, -2):
 # print(str(x) + ' is an even number < 10')
# z = str(x)
# for x in range(10, 0, -2):
 # print( z + ' is an even number < 10')

# What this loop is doing is it's assigning "x = 10", then checks whether
# "x > 0". If so, it prints out that x is an even number, and decrements x
# by 2 (it basically just does "x = x - 2").

# This lets us skip some values while we go through a "range" of numbers!

# Realize that Python is actually doing something quite smart here - it knows
# that it should do an "x > 0" check rather than a "x < 0" check because the
# "step value" is negative! If the step value were positive, it would do a
# "x < 0" check instead, and won't enter the loop AT ALL (since x = 10, and
# 10 < 0 is definitely not true). Try that out:

# for x in range(10, 0, 2):
#  print(str(x) + " is an even number, but never < 0 so we don't execute :-(")

# The "for-in" loop can also loop over (or iterate over) other things - not
# just a range of numbers. If you pass it a string, it'll loop over every
# letter/number/symbol in that string:

# for x in 'lorem ipsum':
#  print(x)

# This would print out each letter of the string 'lorem ipsum' on each line
# (even with the space in the middle):
#
# l
# o
# r
# e
# m
#
# i
# p
# s
# u
# m

# This can be useful when you're trying to understand (or parse) a user's input
# when you can't fully trust them (remember those times when your user tried
# to "break" your code by entering some gibberish???).

################################################################################
# LESSON 6
################################################################################
# We're going to ask Python to sing us a famous song called the "99 beers on
# the wall"!

# The song goes like this (https://en.wikipedia.org/wiki/99_Bottles_of_Beer):

# 99 bottles of beer on the wall, 99 bottles of beer. Take one down, pass it around, 98 bottles of beer on the wall...
# 98 bottles of beer on the wall, 98 bottles of beer. Take one down, pass it around, 97 bottles of beer on the wall...
# 97 bottles of beer on the wall, 97 bottles of beer. Take one down, pass it around, 96 bottles of beer on the wall...
# ...
# 2 bottles of beer on the wall, 2 bottles of beer. Take one down, pass it around, 1 bottles of beer on the wall...
# 1 bottles of beer on the wall, 1 bottles of beer. Take one down, pass it around, 0 bottles of beer on the wall...
# No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall...

# Programmers love to use this song to test out new languages, because there's
# a lot of interesting things going on here (there's a "decrementing loop" -
# that means the numbers are going *down* instead of *up*), and there's also
# a conditional expression that you could put in. Also, programmers love beer,
# apparently ;-)

# Because this one's going to be a bit harder to implement, here are some
# hints:

# 1) To count down in a range(), use a negative "step value" (the 3rd
#    argument):
#
#    for x in range(100, 0, -1):
#
# 2) Remember that "x" in a "for-in" loop is just another variable (you can
#    call that variable "y" or "counter" or "some_number"). That means that
#    you can do all sort of mathematical operations on it (like adding,
#    subtracting, etc.). For example:
#
# for counter in range(10, 50):
   #  print(str(counter - 1) + ' is 1 less than ' + str(counter))
#
# 3) Once the loop ends, you're free to execute other statements! Your loop is
#    only one part of your program!


################################################################################
# EXTRA CREDIT
################################################################################
# The 99 bottles of beer song above has a slight grammar error. When we get to
# 2 bottles of beer, it currently says:

# 2 bottles of beer on the wall, 2 bottles of beer.
# Take one down, pass it around, 1 bottles of beer on the wall...

# But, it should actually say:
#
# Take one down, pass it around, 1 bottle of beer on the wall...

# If you can fix that (and when we reach "1 bottle of beer"), that's an extra
# credit for this lesson!

# 99 bottles of beer on the wall, 99 bottles of beer. Take one down, pass it around, 98 bottles of beer on the wall...
# 98 bottles of beer on the wall, 98 bottles of beer. Take one down, pass it around, 97 bottles of beer on the wall...
# 97 bottles of beer on the wall, 97 bottles of beer. Take one down, pass it around, 96 bottles of beer on the wall...
# ...
# 2 bottles of beer on the wall, 2 bottles of beer. Take one down, pass it around, 1 bottles of beer on the wall...
# 1 bottles of beer on the wall, 1 bottles of beer. Take one down, pass it around, 0 bottles of beer on the wall...
# No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall...

# SOLUTION 

import time


max_beers = input('enter the max numbers that the beer shelf can hold: ')
inputed_max = int(max_beers)

if inputed_max == 0:
  print('seriously...    Ok, here it is: ')
elif inputed_max > 500:
  print('seriously, I knew you were going to try this :| . Here we go: ')

time.sleep(4)

for bottles_amount in range(inputed_max, 0, -1):
  bottles_amount_next = bottles_amount - 1 
  
  if bottles_amount > 1:
    bottle_type = 'bottles'
  else:
    bottle_type = 'bottle'

  if bottles_amount_next == 1:
    bottle_type_next = 'bottle'
  else:
    bottle_type_next = 'bottles'


  special = str(bottles_amount) + ' ' + bottle_type +' of beer on the wall, ' + str(bottles_amount) + ' ' + bottle_type + ' of beer.' + '\n' + 'Take one down and pass it around, ' + str(bottles_amount_next) + ' ' + bottle_type_next + ' of beer on the wall...'
  print(special)
string_max_beers = str(inputed_max)
print('No more bottles of beer on the wall, no more bottles of beer.' + '\n' + 'Go to the store and buy some more, ' + string_max_beers + 'bottles of beer on the wall...')
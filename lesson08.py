#!/usr/bin/env python3

# We're going to learn about floating points (or just floats) and some funky
# operators with strings.

# Remember that when we tried to divide integer values as is, we got this long
# decimal number? Something like:

a = 5 / 3

print(a) # this prints 1.6666666667

# The variable 'a' contains a value type called floating points (or just
# floats). Floats are just numbers with a decimal point.

# Why does Python need to differentiate between a float and integers, then?!
# They're both numbers!!!

# Well, it's actually not just Python that differentiates them - computers
# represent floats and integers differently when they store them temporarily
# in their brain. The short story is that integers can be stored in a
# computer's brain with a small amount of space, but floats need a larger
# space to fit. Space was a bigger issue a long time ago (when our computers
# took up an entire room!), but not so much these days.

# The other reason is because of accuracy. Try this:

print(1.2 - 1.0)

# When you look at this, it should be obvious that the answer should be 0.2.
# But, when you run this in Python, you'll probably get the answer:
#   0.19999999999999996

# What the...?!

# The reason Python does this is because the representation of floats in a
# computer causes it to become inaccurate at times. This is a problem when
# you're, for example, a big bank processing someone's bank account (we're
# giving you $0.19999999999999996 interest this month). That's why we don't
# rely on floats when accuracy is important - we have other mechanisms to
# make sure that the computer doesn't get confused when doing simple
# calculations like this!

# Floats can be added, subtracted, multiplied, and divided by other floats
# or even integers (and integers can be added, subtracted, multiplied, and
# divided by other integers and floats as well):

print(1.2 + 5)
print(7.2 - 2.2)
print(2 * 1.9)
print(85 / 5)

# The result of all these operations is ALWAYS a float, though (even if the
# value turns out to become an integer, like in the 2nd example, it will still
# return a float: 5.0 in this case).

# Floats can also use the exponents operator, integer division, and modulo
# operators:

print(9.7 ** 5)
print(27.3 // 7.3)
print(27.3 % 7.3)

# You'll rarely use these, so don't worry too much about them!

# The next thing that we're going to cover is some interesting operations that
# we can do to strings.

# From our previous lessons, you remember that we can combine (we call it
# concatenate) strings. When we concatenate strings, we get a new string with
# the strings all stuck together:

a = 'hi, '
b = 'my name is '
c = 'iron man!'

print(a + b + c) # prints "hi, my name is iron man!"

# This allows us to join together different strings to create one giant string
# instead. Naturally, Python chose the + operator, since we're kind of just
# adding together these strings!

# In Python, you can also use the * operator to create many copies of the same
# string. You must multiply with an integer in order for this to work:

a = 'i love python ' * 3

print(a) # prints "i love python i love python i love python"

# We can use this trick to make text art (we also call them ASCII art - ask
# me why it's called ASCII later!):

print('O' + ('_' * 50) + 'o')

################################################################################
# LESSON 8
################################################################################
# For this lesson, try to make your own ASCII art by using string concatenation
# and string multiplication!

# The sky is the limit for your imagination!
#!/usr/bin/env python3

# OK, we're going to do a bit of math lesson now. Let's create a simple
# calculator!

# Doing arithmetic in Python is simple - you can use the basic operators
# to do simple arithmetic:

complex_calculation = 1 + 3 * 10 / 5 - 8

# We're also going to take this opportunity to learn about the modulo operator!

# When we do division, we get a quotient and a remainder (if there is one).
# The modulo operator is used to get the remainder, and we use the % operator:

print(11 % 3) # we should print 2 here, becase 11 / 3 = 3 remainder *2*

# But what if we only wanted to get the quotient? If we try to use the division
# operator using /, we get a surprising result

print(11 / 3) # we should get 3, but...

# In order to get a nice integer value for our quotient, we can use the //
# operator to force Python to emit an integer instead:

print(11 // 3) # ah, we print out 3 now!

################################################################################
# LESSON 4
################################################################################
# We're creating a simple calculator for this lesson. We're going to print out
# the value when we add, subtract, multiply, and divide 2 numbers.

# First, let's get a number from our user by prompting them:
# "Enter your first number: "

# We'll store that in a variable, then ask them for a second number:
# "Enter your second number: "

# Force both of these variables into an integer, then print these things out:
# * The sum is: <the added value>
# * The difference is: <the subtracted value>
# * The product is: <the multiplied value>
# * The quotient is: <the quotient - must be an integer>, and the remainder is: <the remainder>
First_input = input("Enter your first number: ")
Second_input = input("Enter your second number: ")
int1 = int(First_input)
int2 = int(Second_input)
a = int1 + int2
b = str(a)
ab = int1 - int2
ba = str(ab)
abb = int1 * int2
bba = str(abb)
aab = int1 % int2
baa = str(aab)
aabb = int1 // int2
bbaa = str(aabb)
print("The sum is: " + b + '\n' + "The difference is: " + ba + '\n' + "The product is: " + bba + '\n' + "The quotient is: " + bbaa + ", " + "and the remainder is: " + baa)

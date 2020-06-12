#!/usr/bin/env python3

# Time to review our basic operators.
#
# Before we get into it, there are 2 types of operators in Python (and in
# most other languages) - binary operators and unary operators.
#
# Binary operators operate on 2 variables or expressions. The addition operator
# is a binary operator, because it needs a left-hand-side value and a
# right-hand-side value:

answer1 = 5 + 3
answer2 = 5 ** 3
answer3 = 5 == 3

# 5 is our left-hand-side value, and 3 is our right-hand-side value. The +
# operator "adds" those 2 values together ("2" is the keyword here - it's
# BInary).
#
# On the other hand, there are operators that only operate on a single value
# or variable. These are called unary operators Can you guess one that we
# learned about?

answer4 = not(answer3)
answer5 = not(True)

# These are the operators we learned about:
#
# Arithmetic operators (binary operators):
#   +    addition
#   -    subtraction
#   *    multiplication
#   /    floating point division
#   //   integer division
#   %    modulo
#   **   exponent (to the power of)
#
# Boolean comparison operators (binary operators):
#   >    greater than
#   >=   greater than or equal to
#   <    less than
#   <=   less than or equal to
#   ==   equal to
#   !=   not equal to
#
# Boolean logical operators (binary operators)
#   and  conjunction (a AND b - both of them have to be True)
#   or   disjunction (a OR b - one of them have to be True)
#
# Boolean logical operators (unary operators):
#   not  negation (not(a) - if a is True, the result is False)
#
# String operators (binary operators):
#   +    concatenate (combine strings)
#   *    repeat

################################################################################
# LESSON 9
################################################################################
# Let's create a game now. The rule of the game is simple:
#
# The game has 3 rounds. On each round, we create 2 random values (I'll show
# you how we do that below). We then tell the user our 2 values, and ask them
# to tell us which binary comparison operator to use to make our statement
# True.
#
# As an example, let's say we tell them "5" and "3":
#
#   5  [ ]  3
#
#   What binary operator goes in the [ ]?
#
# If the user enters ">", ">=", or "!=", they get a point. Otherwise, they get
# 0 points.
#
# At the end of 3 rounds, we tell them how many points they got.
#
# In order to create a random number, add this to the top of this file:
#   import random
#
# Then, when you want to create a random number:
#   value1 = random.randint(0, 10)
#
# That line creates a random number between 0 and 10 (you can change the
# arguments to test out different values).

################################################################################
# EXTRA CREDIT
################################################################################
# As an extra credit, we'll put in 3 extra rules:
#
#   If the user uses the == operator, it's worth 5 points
#   If the user uses the >= or <= operator, it's worth 3 points
#   If the user uses the > or < operator, it's worth 2 points
#   If the user uses the != operator, it's worth 1 point

# Try to make sure you can calculate the points correctly, and tell the user
# their final score!
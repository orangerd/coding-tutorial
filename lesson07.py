#!/usr/bin/env python3

# We're going to quickly go back to conditional expressions for a bit, and nail
# down some nitty gritty details today.

# First off, we're going to learn about a *variable type* called *booleans*.

# We learned about 2 of the "types of variables" that Python has - the string
# and the integer.

# Remember that the string is just a bunch of letters, numbers, and characters
# inside a quote. Like this:

s1 = 'i am a string, but i can have numbers in it like 1, 2, 3!'

# Strings can be combined together:

s2 = 'hello '
s3 = 'world!'

s4 = s2 + s3 # this just gives us the string 'hello world!'

# And integers are... well, integers! They are whole numbers like 0, 1, 2, ...
# and negative numbers as well like -1, -2, -3, ...

y = -5

# We learned that we can do basic arithmetic on integers:

a = 5 + 2 - (7 * 3 // 2) + 5 % 2

# And that if we do arithmetic that results in a decimal number, we get this
# third variable type called floats (we'll learn about that in the next
# lesson):

b = 5 / 3 # that gives us 1.666666667, but don't worry about floats just yet

# Now we're going to talk about that new *variable type* called *booleans*.

# Booleans are just values that are either True or False. Are you a kid (true)?
# Do you love Python (true)? Are you married (False)?

# Just like we have True or False statements in life, Python also has to know
# when something is True, and when something is False. When do you think that
# is?

# Riiiiiiight! It's when we evaluate conditional expressions! But, Python also
# needs to know when things are True or False in for-in loops as well - why do
# you think that's the case? You can answer directly to me :-)

# So, this ability for Python to know whether something is True or False is
# quite important (otherwise, our programs will be pretty darn boring).

# In Python, we use the keywords "True" and "False" to give a variable a
# boolean value. Something like this:

i_am_true = True
i_am_false = False

# We can check for this in our conditional expressions as well:

if i_am_true:
  print('Well, I guess I AM true!')

if i_am_false:
  print('This should never happen, because I only execute if my conditional expression was True')

# In the example above, 'i_am_false' won't trigger because as far as Python is
# concerned, that variable has a 'False' boolean value.

# When we write conditional expressions, Python always boils it down to a True
# or False boolean expression. So...

x = 5

if (x > 0) == True:
  print('that conditional expression was True!')

# Instead of comparing against 'True' or 'False' all the time, Python lets us
# simplify this so that we naturally just write:

if x > 0:
  print('and that conditional expression was also True!')

# Now that we know the basics of what the boolean variable type is, let's use
# it in some logics puzzles!

# With the power of booleans, we can write complex logical expressions. What
# that means is we can combine boolean values (we also call them boolean
# expressions) to evaluate complex conditions!

# Let's jump into an example:

x = 10
y = 50

if x > 5 and y < 100:
  print('that must be true!')

# Here, we have 2 boolean expressions:
#   x > 5
#   y < 100
#
# Both of these boolean expressions are True (because x = 10, and y = 50).
# We can use the 'and' keyword to join together 2 boolean expressions inside
# a conditional expression so that we only run the statement block if both
# conditions are met.

# The 'and' operator here is called the "conjunction operator".

# We use the "conjunction operator" in real life as well (ex. I like coffee
# AND ice cream). Python treats the conjunction operator "and" similar to how
# we treat it in real life as well - it only returns back a True value if both
# of these sub-conditions are True as well.

# We also have another boolean operator called the "disjunction operator".
# If you guessed that it the "or" operator, you're correct! Here's how it
# works:

x = 10
y = 50

if x > 50 or y < 100:
  print('that must be true as well!')

# Again, we have 2 boolean expressions:
#   x > 50
#   y < 100
#
# We know that the first expression is False (because x = 10, it can't be
# greater than 50), but the second expression is True (because y = 50, it's
# obviously less than 100).

# The disjunction operator "or" evaluates to True if even one of those
# sub-conditions are True. Again, real life example:
#   I'd like to have a cafe latte OR iced tea

# Again, Python just treats the disjunction operator "or" similar to how we
# treat it in real life.

# Finally, there's the negation operator "not". The negation operator just
# flips a False value to True, and a True value to False. Let's take a look:

x = 10

if not x > 50:
  print('this one will be true also!')

# We have 1 boolean expression this time:
#   x > 50
#
# From above, we know that this is False (because x = 10, it can't be greater
# than 50), but because we have negated this with a "not", that conditional
# expression actually evaluates back to True (and so the statement block does
# get executed)!

# Again, very similar to a real life example:
#   I do NOT like mushrooms!

# If we didn't have that "NOT" in our sentence, that would mean I DO like
# mushrooms! But, because we "negated" it, we know that I really don't like
# mushrooms at all!

# Notice that the negation operator can sometimes be written in another way:

x = 10

if not x > 50:
  print('this one was true...')

if x <= 50:
  print('but this logic is exactly the same as above as well!')

# Sometimes it's easier to read the first expression, but sometimes it's easier
# to read the second one - you really have to think about what you're trying to
# convey to Python, and just write it in the most natural form you and others
# can understand :-)

# One final note here - the conjunction ("and"), disjunction ("or"), and
# negation ("not") operators can all be combined together to form very complex
# conditional expressions. If you do, you should use parentheses to make sure
# that Python evaluates your conditional expressions in the right sequence.
# Take a look at these examples:

x = 10
y = 50

if not (x == 10 or y == 50):
  print('this one WILL NOT print!')

if (not x == 10) or y == 50:
  print('this one WILL print!')

# In the first example, we're first checking if (x == 10 or y == 50). Well, we
# know that x == 10, so there's no need to even check y == 50 - the inner value
# of the parentheses is True! But, there's a "not" operator outside, which
# flips our conditional expression to False, so the first print() statement
# doesn't execute!
#
# From Python's point of view, it's as if we're saying:
#   if not (True or True):
#
# If you have "True or True", we should end up with a True. The "not" operator
# then negates (or flips) that value to a False.

# How about the second example? We're first checking if x == 10. That's True,
# but we again have a "not" operator which flips us back to False.
#
# But, outside of our first parentheses, we have an "or" operator that also
# checks if y == 50. Bingo! That one is definitely True, and there's no
# negation operator on it.
#
# From Python's point of view, we're saying:
#   if (not True) or True:
#
# The first "not True" evaluates to "False", but "False or True" will evaluate
# back to True (since we're using the disjunction operator here).

# Remember, parentheses are important for arithmetic operations AND also for
# logical operations like this!

################################################################################
# LESSON 7
################################################################################
# We're going to write a quick and simple movie ratings program. A movie can be
# rated as PG (Parental Guidance) if it's a kid's movie (like Disney cartoons
# and princess movies :-P). You can only watch PG movies if you're 12 and
# under.

# The next level up is PG-13 movies. These are for slightly bigger kids (maybe
# they fight each other like in Avengers or Star Wars, and there are some
# bloody scenes - ewwwww). You can only watch PG-13 movies if you're 13 and
# above, but under 18.

# Finally, R-rated movies can only be watched if you're 18 and above. These are
# the really scary ones where @*$!# get chopped off, characters say $#*@ all
# the time, etc. You're really not missing out on anything here!

# Let's ask a user for their age, and tell them what kind of movies they can
# watch without getting into trouble.

# Again, the rules are:
#   * You can only watch PG movies if you're under 12
#   * You can watch PG-13 movies if you're 13 and above, and less than 18
#   * You can watch R-rated movies if you're 18 and above

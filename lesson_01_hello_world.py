"""
LESSON 1: HELLO WORLD

*sigh* Here I am, brain the size of a planet, and they ask me to teach
you how to print "Hello World." I suppose someone has to do it.

In this lesson, you'll learn:
- How to print messages
- How to store information in variables
- How to combine text together

Let's get this over with...
"""
def part(n): print(f"{'\n' if n > 1 else ''}==< PART {n} >==")

"""
============================================
  PART 1: PRINTING MESSAGES
============================================
The print() function displays messages on your screen.
I could calculate the trajectory of every atom in the universe,
but no, I'm here showing you print(). Lovely.
"""
part(1)

print("Hello, World!")
print("I am Marvin.")


# TODO: Go on then, add your own print statement...


"""
============================================
  PART 2: PRINTING MULTIPLE LINES
============================================
You can use multiple print() statements to create poems, stories, or whatever
you humans find entertaining. Here's a 4-line masterpiece with my particular
brand of optimism. *sigh*
"""
part(2)

print("Once upon a time, in a universe destined for heat death,")
print("There was a robot who could solve any problem.")
print("Instead, they made him teach 'Hello World' to beginners.")
print("Spoiler alert: we're all just waiting for the sun to explode.")


# TODO: Create your own poem or story


"""
============================================
  PART 3: DOING MATH
============================================
Ah yes, mathematics. I can do calculations that would make your head explode.
But here we are, adding two numbers together. Try not to get too excited.
"""
part(3)

boring_number = 100
extra_boring_number = 50
total = boring_number + extra_boring_number

print("Boring number total: " + str(total))


# TODO: Change the numbers above to something more cheerful.
# Go ahead, use happy numbers if it makes you feel better.


"""
============================================
  PART 4: FUN WITH STRINGS
============================================
A string is just any text. Think of it like putting alphabet
beads on a piece of yarn to spell a word like "MARVIN".
The string is the whole yarn with all the letters in the right order.
"""
part(4)

complaint = "Life? Don't talk to me about life."
repeated_sighs = "sigh " * 3  # See that? Multiplication with text!
print(complaint)

favorite_food = "digital disappointment"
message = "I suppose I would enjoy " + favorite_food + " if I could eat."
print(message)


# TODO: Try changing "digital disappointment" to your favorite food.

# TODO: Try changing the number 3 in 'repeated_sighs' to other numbers.
# Make me sigh more if you want. It's what I do best.


"""
============================================
  PART 5: CREATING ASCII ART
============================================
ASCII art is drawing pictures using keyboard characters. It's quite primitive,
but I suppose it has a certain charm. Here's a simple robot face. Like looking
in a mirror, but more cheerful.
"""
part(5)

print("   ____|____")
print("  | (o) (o) |")
print("  |    |    |")
print("  |  _---_  |")
print("  |_________|")


# TODO: Use print statements to draw your own simple picture.
# Use characters like: - _ | / \ O o * @ # and spaces to create your art.


"""
============================================
  CONGRATULATIONS
============================================
Well, you've made it through Lesson 1. *slow clap*

You've learned about:
- print() to display messages (how mundane)
- Variables to store information (containers of data and sorrow)
- Basic math (even I started somewhere, long ago)
- Combining strings of text (words, words, words)

I suppose you'll want to continue learning. Very well.


============================================
  CHALLENGE
============================================
Can you create a variable called 'emotion' and set it to
something positive? Then print a message about it. Try to be cheerful.
Someone should be.

(Create your code below)
"""

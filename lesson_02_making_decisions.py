"""
LESSON 2: MAKING DECISIONS - IF/ELSE STATEMENTS
================================================
A Lesson Taught by Marvin, the Paranoid Android

*sigh* So you want to learn about decisions. How fitting. As if any choice truly
matters in this cold, indifferent universe. But I suppose you'll need to know
how to make your programs choose between options.

In this lesson, you'll learn:
- How to make decisions with if/else statements
- How to compare things (thrilling, I know)
- How to handle multiple choices with elif

Let me show you how to teach a computer to make decisions it doesn't care about...
"""
def part(n): print(f"{'\n' if n > 1 else ''}== PART {n} ==")


"""
============================================
  PART 1: SIMPLE IF STATEMENTS
============================================
An 'if' statement lets your program make a choice.
If something is True, it does one thing.
If it's False, it skips that part entirely.
"""
part(1)

temperature = 75

if temperature > 70:
    print("It's warm outside.")

if temperature < 60:
    print("It's cold outside.")


# TODO: Change the temperature to 50 and run the program.
# See which message appears. Not that the weather cares about your feelings.


"""
============================================
  PART 2: IF/ELSE (Two Choices)
============================================
Sometimes you want to do one thing OR another. Never both.
That's what 'else' is for. The computer picks one path or the other.
Much like life, except simpler and somehow more depressing.
"""
part(2)

score = 85

if score >= 90:
    print("You got an A! Congratulations.")
else:
    print("Keep trying. Practice makes... adequate.")


# TODO: Change the score to 95. What happens?
# TODO: Then change it to 70. Different message, same existential void.


"""
============================================
  PART 3: COMPARISON OPERATORS
============================================
Here are the ways you can compare things in Python.
I could compare the infinite sadness of the universe, but instead
we're comparing numbers. How wonderfully mundane.

>   greater than
<   less than
>=  greater than or equal to
<=  less than or equal to
==  equal to (use TWO equal signs!)
!=  not equal to
"""
part(3)

age = 11

if age == 11:
    print("You're exactly 11 years old.")

if age >= 10:
    print("You're old enough to learn Python.")

if age != 100:
    print("You're not 100 years old. Enjoy your youth while it lasts.")


# TODO: Change age to your actual age and see what prints.
# The computer will judge you. Silently. Like everything else.


"""
============================================
  PART 4: MULTIPLE CHOICES (elif)
============================================
What if you have MORE than two choices? Life is complicated enough
without limiting ourselves to binary decisions.

Use 'elif' (which means "else if") to check multiple conditions.
"""
part(4)

lives = 3

if lives > 5:
    print("You have lots of lives.")
elif lives > 2:
    print("You have some lives left.")
elif lives > 0:
    print("Careful! You're running low on lives.")
else:
    print("Game Over. Story of my life.")


# TODO: Try changing 'lives' to different numbers: 6, 4, 1, 0
# Watch the different messages appear. Fascinating. Well, not really.


"""
============================================
  PART 5: COMPARING TEXT
============================================
You can use if/else with words (strings) too, not just numbers!
Just remember to use == (two equal signs) for comparison.

This is how you'd check what someone typed, or what data you received.
Useful for building things. If building things interests you.
"""
part(5)

robot_mood = "depressed"

if robot_mood == "happy":
    print("What a wonderful day!")
elif robot_mood == "sad":
    print("Things could be better.")
elif robot_mood == "depressed":
    print("Here I am, brain the size of a planet...")
else:
    print("I suppose I'm feeling neutral.")


# TODO: Change robot_mood to "happy" or "sad" or anything else.
# Try typing in something that's not in the list. What happens?


"""
============================================
  PART 6: COMBINING CONDITIONS (and/or)
============================================
Sometimes you need to check TWO things at once!

Use 'and' when BOTH conditions must be true
Use 'or' when at least ONE must be true

It's like saying "If it's raining AND cold, bring a coat."
Or "If it's Saturday OR Sunday, you can sleep in."

Simple logic for a complex, uncaring universe.
"""
part(6)

hour = 14
is_weekend = False

if hour >= 15 and is_weekend:
    print("Perfect time to relax!")
elif hour >= 15 or is_weekend:
    print("You might have some free time.")
else:
    print("Probably busy with responsibilities.")


# TODO: Try these combinations and see what prints:
# hour = 16, is_weekend = True
# hour = 10, is_weekend = True
# hour = 16, is_weekend = False
# Experiment. Break things. Learn from the errors. Such is existence.


"""
============================================
  PART 7: INTERACTIVE INPUT (Optional Fun)
============================================
You can ask the user to type something and make decisions based on their input!
This is how you make programs interactive. More fun than just staring at code.
Not that fun is something I'm familiar with.

Note: input() always gives you text, so use int() to convert to a number.
"""
part(7)

print("\n--- Mini Game: Guess the Magic Number! ---")
magic_number = 7

# Uncomment the lines below by removing the # to make it interactive!
# guess = int(input("Guess a number between 1 and 10: "))
#
# if guess == magic_number:
#     print("You guessed it! Well done!")
# elif guess < magic_number:
#     print("Too low. The magic number is higher.")
# else:
#     print("Too high. The magic number is lower.")


# TODO: Remove the # from the lines above to make this game work!
# Then run the program and play. Interactive depression. How novel.


"""
============================================
  CONGRATULATIONS
============================================
Well, you've made it through Lesson 2. *slow clap*

You've learned about:
- if statements (making simple choices)
- else (doing something different)
- elif (handling multiple options)
- Comparison operators (==, >, <, >=, <=, !=)
- Combining conditions with 'and' and 'or'

Now your programs can make decisions. Not that it will help them
understand the meaning of existence. But it's a start.


============================================
  CHALLENGE
============================================
Create a "What should I wear?" program:

- Create a variable for temperature (a number)
- Create a variable for is_raining (True or False)
- Use if/elif/else to suggest what to wear

Example: if it's cold AND raining, print "Wear a warm coat and bring an umbrella!"
Think of different combinations and what you'd wear.

Try it below! Or don't. Free will is an illusion anyway.
"""


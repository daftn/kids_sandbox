"""
LESSON 2: MAKING DECISIONS - IF/ELSE STATEMENTS
================================================

Welcome to Lesson 2! In this lesson, you'll learn:
- How to make your program make decisions
- How to compare numbers and text
- How to use if, elif, and else statements

Programs need to make choices, just like you do every day!
Let's learn how to teach Python to make decisions.
"""

# ============================================
# PART 1: SIMPLE IF STATEMENTS
# ============================================
# An 'if' statement lets your program make a choice.
# If something is True, it does one thing.
# If it's False, it skips that part.

temperature = 75

if temperature > 70:
    print("It's warm outside! Perfect for playing!")

if temperature < 60:
    print("It's cold! Bring a jacket!")

# TODO: Change the temperature to 50 and run the program.
# What message do you see now?


# ============================================
# PART 2: IF/ELSE (CHOOSING BETWEEN TWO OPTIONS)
# ============================================
# Sometimes you want to do one thing OR another.
# That's what 'else' is for!

score = 85

if score >= 90:
    print("Amazing! You got an A!")
else:
    print("Good job! Keep practicing!")

# TODO: Change the score to 95. What happens?
# TODO: Change the score to 70. What happens now?


# ============================================
# PART 3: COMPARING THINGS
# ============================================
# Here are the ways you can compare things in Python:
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to
# ==  equal to (use TWO equal signs!)
# !=  not equal to

age = 11

if age == 11:
    print("You're exactly 11 years old!")

if age >= 10:
    print("You're old enough to learn Python!")

# TODO: Change age to your actual age.
# What messages do you see?


# ============================================
# PART 4: MULTIPLE CHOICES (ELIF)
# ============================================
# What if you have MORE than two choices?
# Use 'elif' (which means "else if")!

lives = 3

if lives > 5:
    print("You have lots of lives! 💚💚💚")
elif lives > 2:
    print("You have some lives left! 💚💚")
elif lives > 0:
    print("Careful! You're running low on lives! 💚")
else:
    print("Game Over! ☠️")

# TODO: Try changing 'lives' to different numbers: 6, 4, 1, 0
# See how the message changes each time!


# ============================================
# PART 5: CHECKING TEXT
# ============================================
# You can use if/else with words too, not just numbers!

favorite_subject = "math"

if favorite_subject == "math":
    print("Math is awesome! Numbers are everywhere!")
elif favorite_subject == "science":
    print("Science is cool! Let's do experiments!")
elif favorite_subject == "art":
    print("Art is creative! Express yourself!")
else:
    print("Every subject is interesting in its own way!")

# TODO: Change favorite_subject to "science" or "art" or anything else.
# What happens each time?


# ============================================
# PART 6: COMBINING CONDITIONS (AND/OR)
# ============================================
# Sometimes you need to check TWO things at once!
# Use 'and' when BOTH must be true
# Use 'or' when at least ONE must be true

hour = 14  # 2 PM in 24-hour time
is_weekend = False

if hour >= 15 and is_weekend:
    print("Perfect time to play video games!")
elif hour >= 15 or is_weekend:
    print("You might have some free time!")
else:
    print("Probably still at school or doing homework")

# TODO: Try these combinations:
# hour = 16, is_weekend = True
# hour = 10, is_weekend = True
# hour = 16, is_weekend = False
# What message do you get for each?


# ============================================
# PART 7: FUN WITH USER INPUT (INTERACTIVE!)
# ============================================
# You can ask the user questions and make decisions based on their answer!
# Note: input() always gives you text, so use int() to convert to a number

print("\n--- Mini Game: Guess the Magic Number! ---")
magic_number = 7

# Uncomment the lines below by removing the # to make it interactive!
# guess = int(input("Guess a number between 1 and 10: "))
#
# if guess == magic_number:
#     print("🎉 WOW! You guessed it! You're amazing!")
# elif guess < magic_number:
#     print("Too low! The magic number is higher!")
# else:
#     print("Too high! The magic number is lower!")

# TODO: Remove the # from the lines above to make this game work!
# Then run the program and play!


# ============================================
# CONGRATULATIONS!
# ============================================
# You've completed Lesson 2!
# You learned about:
# - if statements (making decisions)
# - else (doing something different)
# - elif (multiple choices)
# - Comparing with ==, >, <, >=, <=, !=
# - Combining conditions with 'and' and 'or'
#
# CHALLENGE: Create a simple "What should I wear?" program
# - Create a variable for temperature
# - Create a variable for is_raining (True or False)
# - Use if/elif/else to suggest what to wear
# Example: if it's cold AND raining, say "Wear a warm coat and bring an umbrella!"
# Try it below!


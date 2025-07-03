
# Instructions:
# 1. Add a try...except block to catch the ValueError.
# 2. Print a message indicating that the input was not a valid number.
# 3. Why: Handles the case where the user provides non-numeric input.

# Explanation:
# ValueError is raised when a function receives an argument of the 
# correct type but an inappropriate value. In this case, int() expects a 
# string representing a number, not an arbitrary string.

# Code that will cause an exception:
user_input = "hello"

try:
    number = int(user_input)  # ValueError
except:
    pass
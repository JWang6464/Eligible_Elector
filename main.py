"""
Assignment: Voter Eligibility Checker
Part of the Cognizant Externship Program

This script prompts the user to enter their age and checks if they are eligible to vote.
If the user is 18 or older, it prints a congratulatory message.
If the user is under 18, it calculates how many years are left until eligibility and displays a friendly message.

Jordan Wang
6/3/2025
"""

# Voter Eligibility Checker

# tbis line asks the user for their age and convert it to an integer
age = int(input("How old are you? "))

# conditional statemnet to check if the user is eligible to vote
if age >= 18:
    # if the user is 18 or older, they're eligible
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    # if the user is under 18, calculate how many years left
    years_left = 18 - age
    print(f"Oops! You’re not eligible yet. But hey, only {years_left} more year{'s' if years_left > 1 else ''} to go!")

# Practice_24

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('cls')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 24', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value
number = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 9, 10]

# Convert To List
number = set(number)

# Show Result
print(number)

# Finish
# Create By Moein Heshmati

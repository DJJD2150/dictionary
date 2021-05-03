# Part of the Python 3 Complete Bootcamp Master Course:  Build 15+ Projects and Games on StackSkills

# What to do:  make a dictionary program.
# Algorithm
# 1. Develop the interface.
# 2. When typing in the words, the output is the definition.
# 3. Modify the program.

import json
from difflib import get_close_matches

# loads the data.json file
data = json.load(open("data.json"))

# # prints the data.json file in the terminal 
# print(data)

# # prints an individual dictionary definition from the data.json file in the terminal 
# print(data[chocolate])

# function that checks if the input you type in to search for is within the data from the json file
# if it isn't, it prints a message saying it's not in the dictionary
# also checks for case sensitivity
def translate(word):
    # converts all of the words in the file to lower case.
    word = word.lower()
    # returns the definition of the word if it's in the dictionary
    if word in data:
        return data[word]
    # same thing, but adjusts for if you typed your input in title case
    elif word.title() in data:
        return data[word.title()]
    # same thing, but adjusts for if you typed your input in upper case
    elif word.upper() in data:
        return data[word.upper()]
    # checks for close matches to the word you typed in
    # compares the word you typed in to the words in the dictionary
    elif len(get_close_matches(word, data.keys())) > 0:
        # puts out a message asking if you meant to type in the closely matching word
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        # creates a variable that lets the user decide if they meant the closely matching word or not
        user_decision = input("press y for yes or n for no")
        # returns the closely matching word's definition if the user types "y"
        if user_decision == "y":
            return data[get_close_matches(word, data.keys())[0]]
        # returns the exception message of a non-existent word if the user types "n"
        elif user_decision == "n":
            return("This word doesn't exist in the dictionary, or you may have typed it incorrectly.  Please check it again.")
        # returns an exception message if the user types something other than "y" or "n"
        else:
            return("You have entered the wrong input.  Please enter y or n.")
    # returns an exception message if the word does not exist
    else:
        return print("This word doesn't exist in the dictionary, or you may have typed it incorrectly.  Please check it again.")

# creates the initial input/ message variable where you type in the word you want to find
word = input("Enter the word you want to find the definition of: ")
# creates an output variable that calls the translate function with word as the parameter 
output = translate(word)
# checks to see whether or not the output is a list of definitions
# if it is, it loops through the list and prints the definitions one by one
# if it isn't, it simply gives the single definition as the output
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

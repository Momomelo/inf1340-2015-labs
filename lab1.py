#!/usr/bin/env python3

""" Graded Lab #1 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def vowel_or_consonant():
    """
    Exercise: Vowel or Consonant
    Reads a letter of the alphabet from the user. (You can assume that it's
    lowercase.) If the user enters a, e, i, o or u then your program should
    display "vowel". If the user enters y then your program should <display></display>
    "sometimes a vowel, sometimes a consonant". Otherwise your program should
    display a message indicating that the letter is a "consonant".
    """

    user_letter = raw_input ("Please enter a letter to see if it is a vowel or consenant!").lower()
    if user_letter == "a" or user_letter == "e" or user_letter == "i" or user_letter == "o" or user_letter == "u":
        print ("vowel")
    elif user_letter == "y":
        print ("sometimes a vowel, sometimes a consonant")
    elif user_letter == "b" or user_letter == "c" or user_letter == "d" or user_letter == "f" or user_letter == "g" or user_letter == "h" or user_letter == "j" or user_letter == "k" or user_letter == "l" or user_letter == "m" or user_letter == "n" or user_letter == "p" or user_letter == "q" or user_letter == "r" or user_letter == "s" or user_letter == "t" or user_letter == "v" or user_letter == "w" or user_letter == "x" or user_letter == "y" or user_letter == "z":
        print ("consonant")
    else:
        print ("That's not a single letter silly!")


#The above code is really silly! bwcause everything is hardcoded.
#Let's learn how to use the len() function to not make everything so hard coded!

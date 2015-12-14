#!/usr/bin/env python3

""" Graded Lab #2 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


"""
Instructions: Add a function to to get input from the user and use that
function in name_that_shape()

The function should prompt the user for input until a legal value is
entered. A legal value is any integer.

"""
def whats_your_input():
  output = ""
  not_an_integer = True

  while not_an_integer is True:
    try:
      output = int(raw_input("Number of sides:"))
      not_an_integer = False
    except:
      ValueError
      print "Input an integer."
      continue

  return output


def name_that_shape(sides):
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs | Expected Outputs
    -------------------------
      < 3  | Error
      3    | triangle
      4    | quadrilateral
      5    | pentagon
      6    | hexagon
      7    | heptagon
      8    | octagon
      9    | nonagon
      10   | decagon
      > 10 | Error

    Errors: ValueError when input is a string or float

    """

    #sides = whats_your_input()

    if sides == 3:
        return("Triangle")
    elif sides == 4:
        return("Quadrilateral")
    elif sides == 5:
        return("Pentagon")
    elif sides == 6:
        return("Hexagon")
    elif sides == 7:
        return("Heptagon")
    elif sides == 8:
        return("Octagon")
    elif sides == 9:
        return("Nonagon")
    elif sides == 10:
        return("Decagon")
    else:
        return("Error")


#name_that_shape()
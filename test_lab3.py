#!/usr/bin/env python3

""" Module to test lab3.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import pytest
import mock
from lab3 import days_in_month

MONTHS_WITH_31 = ["January", "March", "May", "July", "August", "October", "December"]
MONTHS_WITH_30 = ["April", "June", "September", "November"]
MONTHS_WITH_28_or_29 = ["February"]


def test_months_with_31():
    """
    Test months with 31 days
    """
    for item in MONTHS_WITH_31:
        assert days_in_month(item) == 31

def test_months_with_30():
    """
    Test months with 30 days
    """
    for item in MONTHS_WITH_30:
        assert days_in_month(item) == 30

def test_months_with_28_or_29():
    """
    Test months with 28 or 29 days
    """
    for item in MONTHS_WITH_28_or_29:
        assert days_in_month(item) ==  "28 or 29"

def test_months_with_no_caps():
    """
    Test months which are not capitalized properly.
    """
    for item in MONTHS_WITH_30:
        item = item.lower()
        assert days_in_month(item) == 30

    for item in MONTHS_WITH_28_or_29:
        item = item.lower()
        assert days_in_month(item) == "28 or 29"

    for item in MONTHS_WITH_31:
        item = item.lower()
        assert days_in_month(item) == 31


def test_months_with_the_unexpected():
    """
    Test strings which would be really unexpected for the user to input
    """
    for item in MONTHS_WITH_28_or_29 or MONTHS_WITH_30 or MONTHS_WITH_31:
        try:
            assert days_in_month(365)
        except AttributeError:
            return True

        try:
            assert days_in_month("threesixfive")
        except ValueError:
            return True

        try:
            assert days_in_month({"one", "two"})
        except TypeError:
            return True

# Write a test function for the months with 30 days
    #DONE

# Write a test function for the months with 28 or 29 days
    #DONE

# Write a test function for months that are not capitalized properly
    #DONE

# Hint: use the .lower() string method
    #DONE

# Write a test function for unexpected input -> multiple arguments, no arguments, a list, 
    #(list , int = type error)
# Hint: use a try/except block to deal with the exception
# Hint: use data types other than strings as input



#def test_multiple_variables():
#    """
    # tests if multiple variables are accepted.
#    """
#    try:
#        assert pig_latinify("afds", "1234")
#    except TypeError:
#        return True

#"""
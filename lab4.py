#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = "Kei'ichiro Yamamoto"
__email__ = "keiichiro.yamamoto@mail.utoronto.ca"
__copyright__ = "2015 Kei'ichiro Yamamoto"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

"""
This is the oiginal code that is not used anymore!

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it


def bill_of_sale(purchase):

    print ("Amount of purchase: {0:.2f}".format(purchase))
    print ("Provincial tax: {0:.2f}".format(purchase * .05))
    print ("Federal tax: {0:.2f}".format(purchase * .025))
    print ("Total tax: {0:.2f}".format(purchase * .075))
    print ("Total sale: {0:.2f}".format(purchase * 1.075))

"""

PROVINCIAL_TAX = .05
FEDRAL_TAX = .025
RECIEPT = "reciept.txt"
PURCHASE = 115


def provincial_tax(PURCHASE):
    taxed_purchase = PURCHASE * PROVINCIAL_TAX 
    return (str(taxed_purchase))

def federal_tax(PURCHASE):
    taxed_purchase = PURCHASE * FEDRAL_TAX
    return (str(taxed_purchase))

def total_tax(PURCHASE):
    taxed_purchase = PURCHASE * (FEDRAL_TAX + PROVINCIAL_TAX) 
    return (str(taxed_purchase))

def total_cost(PURCHASE):
    sales_tax = 1 + (PROVINCIAL_TAX + FEDRAL_TAX)
    taxed_purchase = PURCHASE * sales_tax
    return (str(taxed_purchase))

with open(RECIEPT, 'w') as returned_reciept:
    returned_reciept.write("Amount of purchase: " + str(PURCHASE) + "\n")
    returned_reciept.write("Provincial tax: " + provincial_tax(PURCHASE) + "\n")
    returned_reciept.write("Federal tax: " + federal_tax(PURCHASE) + "\n")
    returned_reciept.write("Total tax: " + total_tax(PURCHASE) + "\n")
    returned_reciept.write("Total sale: " + total_cost(PURCHASE) + "\n")

returned_reciept.close()

"""
THE CODE NEEDS TO OUTPUT ALL 5 LINES OF CODE OF THE PROVINCIAL TAX, DEFERAL TAX, TOTAL TAX, TOTAL SALE 
THERE IS NO RAW IMPUT. THEY'RE PUT IN AS ARGUMENTS IN THE () OF THE FUNCTION.
"""
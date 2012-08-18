"""
Given 2 int values, return True if one is negative and one is positive. Unless the parameter "negative" is True, then they both must be negative. 

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(1, 1, False) → False
"""

def pos_neg(a, b, negative):
    return a < 0 and b < 0 if negative else (a < 0) ^ (b < 0)
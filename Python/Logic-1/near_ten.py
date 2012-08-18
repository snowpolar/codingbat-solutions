"""
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
"""


def near_ten(num):
    num_mod_10 = num % 10
    return  num_mod_10 <= 2 or num_mod_10 >= 8

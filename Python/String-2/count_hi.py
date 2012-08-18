"""
Return the number of times that the string "hi"
appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""


def count_hi(str):
    return str.count('hi')

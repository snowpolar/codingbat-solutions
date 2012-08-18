"""
Return the number of times that
the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""


def count_code(str):
    return sum(1 for i in range(len(str) - 3)
        if str[i:i + 2] == 'co' and str[i + 3] == 'e'
    )

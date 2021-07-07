from collections import defaultdict

"""
Given two strings, write a method to decide if one is a permutation
of the other.
"""

def is_perm_basic(str1: str, str2: str):
    # if case insensitive
    str1 = str1.lower()
    str2 = str2.lower()

    return sorted(str1) == sorted(str2)

def is_perm_alt(str1: str, str2: str):
    if len(str1) != len(str2):
        return False

    occ = defaultdict(int)
    
    for char in str1:
        occ[char] += 1

    for char in str2:
        occ[char] -= 1

    for char_occ in occ.values():
        if char_occ != 0:
            return False

    return True


print(is_perm_basic("god", "dog"))
print(is_perm_basic("God", "Dog"))
print(is_perm_basic("Bruh", "This is not a perm"))

print(is_perm_alt("god", "dog"))
print(is_perm_alt("Bruh bruh", "bruh bruha"))
print(is_perm_alt("abcdefg", "gafbedc"))

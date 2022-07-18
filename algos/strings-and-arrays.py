"""String and array algorithm practice"""

def is_substring(string1, string2):
    """Determine if string1 is a substring of string2"""
    return string1 in string2

def is_rotation(string1, string2):
    """Determine if string2 is a rotation of string1"""
    double_trouble = string2 + string2
    return is_substring(string1, double_trouble)


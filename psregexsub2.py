import re

s = 'root:x:0:0:root:/root:/bin/bash'
pattern = ':'
replacement = ','

s2 = re.sub(pattern, replacement, s)
print(s2)
print()

pattern = '[AEIOU]'  # global variables
match_counter = 0


# print(re.findall(pattern, s2, re.I))   # list of match strings
# total_no_matches = len(re.findall(pattern, s2, re.I))


def replacement(m):
    global match_counter  # to refer  to global variable
    match_counter += 1
    """
    syntax for the if else conditional operator  (?:)

        true-part-expr if test-condition else false-part-expr
    """
    return '*' if match_counter > 3 else m.group()  # ? :


s3 = re.sub(pattern, replacement, s2, flags=re.I)  # nth sub.
print(s3)
print()

# s3 = re.sub('[AEIOU]', '*', s2, flags=re.I, count=3)
# print(s3)
# print()

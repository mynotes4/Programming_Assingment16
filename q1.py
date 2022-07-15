"""
Question1. Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
Examples
stutter("incredible") ➞ "in... in... incredible?"
stutter("enthusiastic") ➞ "en... en... enthusiastic?"
stutter("outstanding") ➞ "ou... ou... outstanding?"
Hint :- Assume all input is in lower case and at least two characters long.
"""

def shutter(s):
    s1 = s[:2]
    return (2*(s1 + "... ") + s +'?')

s = input("Enter input ")
print(shutter(s))
'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 10
'''

# Q1
colors = {"red": 10, "blue":20, "green": 30}
print(colors)
# {'red': 10, 'blue': 20, 'green': 30}
# It is the same order that I typed. 

# Q2
colors["yellow"] = 40
colors["orange"] = 50
print(colors)
# {'red': 10, 'blue': 20, 'green': 30, 'yellow': 40, 'orange': 50}
# This was the order printed, exactly how it was typed into the shell

# Q3
for key in colors:
    print(key)
# red
# blue
# green
# yellow
# orange
# This was printed, exactly in this order

# Q4

# Q5
print(sum(list(colors.values())))
# One line of code is "sum += val"

# Q6
for key in colors:
    colors[key] += 1
print(colors)

# Q7
for key in sorted(colors):
    print(key)
# sorted them alphabetically

# Q8
# print(colors["pink"])
# This was printed (along with the program traceback):
# KeyError: 'pink'

# Q9
print(colors.get("red"))
print(colors.get("pink"))
# print(colors.get("red")); this printed 11 which was the updated value
# print(colors.get("pink")); this printed none which makes sense because of the "get" function for dictionaries

# Q10
print(colors.get("red", -1))
print(colors.get("pink", -1))
# print(colors.get("red")); this printed 11 which was the updated value
# print(colors.get("pink")); this printed -1 which makes sense because we assigned it's default value

# Q11
x = dict()
y = x
z = x.copy()
print(x is y, x is z)
print( x == y, x == z)
z[2.0]  = "two"
y[3.14159] = "pi"
y[2.71828] = "e"
print(x, z)
y.clear()
print(x, z)

# At the end, X gets cleared because of the alias made before. 
# y.clear() clears the object that x is pointing to

# At the end, Z equals: "{2.0: "two"}" which is the only entry we made in the dictionary
# This makes sense because z was a copy of x, which at the time was a blank dictionary. Then z was given an entry which is the only value it has

# Q12
from string import ascii_lowercase

letters  = dict.fromkeys(ascii_lowercase, 0)
print(letters)

# Q13
k = [2001, 2006, 2011, 2016]                #years of censuses
v = [1039534, 1620693, 1649519, 1704694]    #population
d = dict(zip(k, v))
print(d)

# Q14
inv_d = {v: k for k,v in d.items()}

# Q15
from string import ascii_letters


def LetterFrequencies(x):
    alphabet = dict.fromkeys(ascii_letters, 0)
    for letter in x:
        for key in alphabet:
            if str(letter) == str(key):
                alphabet[key] += 1
            else:
                continue
    return print(alphabet)

text="""Python is an interpreted, interactive, object-oriented programming language.
It incorporates modules, exceptions, dynamic typing, very high level dynamic data types,
and classes. It supports multiple programming paradigms beyond object-oriented programming,
such as procedural and functional programming."""

LetterFrequencies(text)
'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 5
'''

# Part 1
# Q1
full_name = "Julian Patterson"

# Q2
name_len = len(full_name)

# Q3
print(full_name[0])

# Q4
print(full_name[-1])

# Q5
# Ran my program and it printed both the first and last character of my full name

# Q6
# This returns an error because "name_len" returns the number of characters in the string
# However, the indexing of "full_name" starts at 0, so the "name_len" will have an "extra" character


# Part 2
# Q1
first_name = full_name[0:full_name.index(" ")]

# Q2
last_name = full_name[full_name.index(" ") + 1:]

# Q3
print("Hello " + first_name)

# Q4
if len(first_name) > len("nnn"):
    print("greater")
if len(first_name) < len("nnn"):
    print("smaller")
elif len(first_name) == len("nnn"):
    print("they are equal")

# Q5
if "an" in first_name:
    print("There is \"an\" in my name")
else:
    print("There is no \"an\" in my name")


# Part 3
# Q1
index = full_name.index("Pat")

# Q2
final_space = full_name.rindex(" ")

# Q3
print("The last part of my name is " + full_name[final_space + 1:])

# Q4
print("The first part of my name is " + full_name[0: final_space])

# Q5
vowels = "a"

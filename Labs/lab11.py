'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 11
'''

# Part 1:

# A
# Output: "{"a": 1, "b": 2, "e": "error"}"

# B
# Key Error for "d["c"] += 1"

# C
# Output: "{"a": 6, "b": 2}"

# D
# Output: "5 2 8 24"
# First, returns the value for key "L" which is equal to 5. 9, is the default value if it is not found (never used because L is a key)
# Second, returns the value for key "A" which is equal to 2
# Third, returns the value for "6", which is equal to the "default_value" of 8
# Last, it sums all the values in this dictionary, 2 + 3 + 6 + 5 + 8 = 24

# E
# Output: 10
# This function goes iterates through a list in the following way:
# result starts at -5, then it checks if the x[1:], in this case 1, is greater than -5
# Because 1 is greater than -5, result = 1
# Next iteration: result = 1, it checks the next number in the list (10),
# Then since 10 > 1, result = 10
# Finally, it returns 10

# F
# Output 1 : [2, 4, 7, 12]
# Output 2 : [1, 5, 9, 10]
# This will iterate over a matrix and will create a new list containing the indexes you indicated
# ex. n = 2, it will make and return a list of the second indexes of each list

# G
# Output: [9, 4, 1] [36, 25, 16, 9, 4, 1]
# This starts at n, then makes a list of n^2 all the way until 1, using recursion
# If n == 0 then it returns a blank list

# H
# Output: 3 5
# This starts at n, then takes the remainder of 2, then adds it to the total, until
# n reaches 1, if n == 0, then it returns 1

# Part 2:

# 1
def count_special_characters(text):
    d = dict()
    for character in text:
        if str(character).isalnum():
            continue
        else:
            if character == " ":
                continue
            else:
                for key in d:
                    if str(character) == str(key):
                        d[key] += 1
                    else:
                        d.update({str(character): 1})
    return print(d)


Text="""This; sho[uld be ' a 3 Real : Challenge * due ! to # the{ special * characters ^ included ( between
] the _ words:, but 4 remember$, don't # give 3 up [ practise ] makes )$ perfect 2 and & keep ' 3 going#
with # your ^ TRAINING 1 to / make & } sure' you be]come the very6 best. % I $ really need 6 to ^
practise this % text and ^ so9 sho)uld & You. Who'S exhausted " yet? * This @ sentence 2 and $ the 5
whole te*xt doesn't ( make 1too much sense 7 but it is @readable if you% disregard /characters.
Tha$nks!"""
print(count_special_characters(Text))

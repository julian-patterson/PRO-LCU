'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 14
'''

# Part 1
# 1
# D

# 2
# B

# 3
# B

# 4
# D

# Part 2
# 1
# This will print [2, 6, -1, 8], basically all the numbers in L multiplied by 2
# Except for "mm" which is replaced by "-1" due to the error made

# 2
# Prints 10 15 FAIL
# it basically just prints the first two statements, however, when it gets to the last one
# it is impossible to divide by 0 (y-5) y = 5, and this raises an exception

# 3
# Prints 0 10 3 because x = 0, y = 10 and z = 3
# x = 0 because of inital assignment and the exception raised by z/x
# y = 10 because of the exception raised by z/x
# z = 3 because z = z + 1 (before the exception raised)

# 4
# Prints "AD" because res = "A" then in the try block, z cannot be divided by 0
# This goes to the ValueError exception which adds "D" to res

# 5
# Print 3 3 because x = x + 1 = 3; and the first exception block changes z to 3

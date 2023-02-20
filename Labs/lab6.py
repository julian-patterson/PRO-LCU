'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 5
'''

# Part 1
# Q1
ls1 = [0, 1, 2, 3, 5, 4]

# Q2
ls2 = [6, 7, 8, 9, 10, 11]

# Q3
print("Ls1 is greater than Ls2: " + str(ls1 > ls2))
# The result of this is false because of the lexicographic comparision, so because the first element of ls2 is greater than ls1, the comparision operation returns false

# Q4
ls1[5] -= 2
print("ls1 = " + str(ls1))

# Q5
ls3 = ls1 + ls2
print("ls3 = " + str(ls1 + ls2))

# Q6
ls3 = ls3 + ls1
print("ls3 = " + str(ls3))

# Q7
ls1.append(8)
print("ls1 = " + str(ls1))
print("ls3 = " + str(ls3))
# No, ls3 is unchanged because ls3 was defined before as ls3 + ls1 before ls1 was appended

# Q8
ls4 = ls2
print("ls2 = " + str(ls2))
print("ls4 = " + str(ls4))

# Q9
ls2.append(8)
print("ls2 = " + str(ls2))
print("ls4 = " + str(ls4))
# I don't think ls4 will change because it was defined as the old list. However, I could be wrong because there was "alias" made; which is something I have never heard of

# Q10
ls5 = sorted(ls3)
print("ls3 = " + str(ls3))
print("ls5 = " + str(ls5))

# Q11
ls3.sort()
print("ls3 = " + str(ls3))
# Ls3 has now been modified, whereas in Q10 it was unchanged

# Q12

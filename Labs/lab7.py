'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 7
'''

# Part 1
# Q1
full_name = "Julian Patterson"
for letter in full_name:
    print(letter)
    print(letter.lower())
# The first statement "print(letter)" prints the letter iterating through my full name. The second statement "print(letter.lower())" would just print it lower case
# Of course each statement will take one line

# Q2 
result = 0
for letter in full_name:
    print(letter, result)
    result += 1
print(full_name, result)
# First, each letter is printed with which iteration it is. This is a result of the "for" loop
# At the end my full name is printed with the final iteration (in my case 16), this represents the total number of characters in my name, starting at 1 rather than 0

# Q3
result = ''
for letter in full_name:
    result = letter + result

print(result)
# This prints my full name backwards. This is it iterates through my full name and adds the iteration to "result". 
# At the end of this, result will contain each character in my name, however they would be backwards because we started the loop with J (from Julian)
# and end with the n (from Patterson)

# Part 2
ID = "2131249"
ID_digits = list(ID)
print(ID)
print(ID_digits)

# Q1
for digits in ID_digits:
    print(digits, int(digits) % 2 != 0)
# This for loop gives the digit in my student and then takes the remainder of that digit (being divided by 2) and prints if it doesn't equal 0
# Basically it checks if that digit is a multiple of 2 or is divisable by 2

# Q2
result = []
for digit in ID_digits:
    result = [digit] + result
print(result)
# This prints a list of my ID which is backwards, this is the same operation done in P1Q3 except with a list
# we need to keep the [] because result is a list and ID_digits is a list

# Q3
id_backwards = ''.join(result)
print(id_backwards, 'x'.join(result))
# this is printed: "9421312 9x4x2x1x3x1x2"

# Q4
result = []
for digit in ID_digits:
    result = [digit] + result
    continue
print(result)
# No continue doesn't do anything because it is already at the end of loop.
# if continue was before "result = [digit] + result" then result would only equal [], it would be empty

# Part 3
# Q1
# First, i starts at 0 and my_list is a list containing 0, i goes through the first iteration
# My list gets added a new value (2 ** i) which is just 2 to the power i
# This loops continues until i reaches 3,
# Then the list is printed which equals "[0,1,2,4]" since it will not reach 2 ** 3 = 8
my_list = [0]
for i in range(3):
    my_list += [2 ** i]
print(my_list)
# This is right, I was correct

# Q2
# This will first split up the text at every space, then it print every second word in a list, 
# starting backwards of the string (so, the last "be" would print first)
# The final result would be ["be", "not", "be"]
text = "to be or not to be"
print(text.split()[::-2])
# This is right, I was correct

# Q4
# This will iterate through the every second value in the list "array" 
# This will then add that iteration to the variable s, which is defined as 0
# so it will print s which at the end is equal 9 (5 + 3 + 1)
array = [5,4,3,2,1]
s = 0
for n in array[::2]:
    s += n
print(s)
# This is right, I was correct

# Q4
# This will just print the regular list "x" with no values at all
# This is because we are creating an alias for x, y and then we are clearing those values
# so y will equal [] and hence x will equal []
x = [9,1,0]
y = x
y.clear()
print(x)
# This is right, I was correct

# Q5
# First, this program establishes a list, 1-10 and result = 0
# Then, it iterates through the range of the len of x which is equal to 10: 10 digits in the list x
# Then in the for loop, it checks if the iteration remainder of 2 is equal to 0; basically if the iteration is a multiple of 2
# Then if this is true, it adds the iteration to result
# If the is not true, it continues in the program 
# The numbers that will be added are those in the spot 0, 2, 4, 6, 8 so (1, 3, 5, 7, 9)
# These digits are all added in result which will equal 25 which is printed at the end of program
x = [1,2,3,4,5,6,7,8,9,10]
result = 0
for i in range(len(x)):
    if (i%2 == 0):
        result += x[i]
print(result)
# This is right, I was correct

# Part 4
# Q1 & Q2
names = input("Enter the names of bidders seperated by spaces: ")
bids = input("Enter their bids seperated by commas: ")

# Q3
names_list = names.split()
bids_list = bids.split(",")
print(names_list)
print(bids_list)

# Q4
for i in (range(len(bids_list))):
    bids_list[i] = int(bids_list[i])

# Q5
sorted_bids = sorted(bids_list)

# Q6 - Q10
for i in (range(len(bids_list))):
    if bids_list[i] == sorted_bids[-1]:
        highest_bidder = names_list[i]
        print(names_list[i] + " had the highest bid of $" + str(bids_list[i]) + ".")
    if bids_list[i] == sorted_bids[-2]:
        print(names_list[i] + " had the second highest bid of $" + str(bids_list[i]) + ", " + highest_bidder +" pays this bid.")

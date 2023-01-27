'''
Julian Patterson 2131249
420-LCU Computer Programming Lab 3
S. Hilal, instructor
'''
# Q1
x1 = int(input("Enter an integer: "))
x2 = int(input("Enter an integer: "))
x3 = input("Enter a float: ")

print("You have entered: " + str(x1) + ", " + str(x2) + " and " + str(x3))

# This is the sum of x1 and x2
print("The sum of x1 and x2: " + str((int(x1)+int(x2))))
print("The product of x1 and x3: " + str((int(x1)*float(x3))))
print("The floor division of x1 by x2: " + str((int(x1) // int(x2))))
print("The division of x1 by x2: " + str((int(x1)/int(x2))))
print("The floor division of x3 by x1: " + str((float(x3)//int(x1))))

# Q2
y = int(input("Enter an integer between 12 and 100: "))

print("The number in decimal is: " + str(y))
print("The number in binary is: " + bin(y))
print("The number in hex is: " + hex(y))

# Q3
n = int(input("Enter an integer: "))

print("The number is positive: " + str((n > 0)))

# Q4
n = int(input("Please enter a positive integer: "))
tmp = (n % 2)

print("The number is even: " + str(tmp == 0))

# Q5
'''
First; 

tmp = float( 17 // 5)
17 // 5 = 3 (since 17 / 5 = 3.4)
float(17 // 5) = 3.0

Then; 
tmp*3 = 9.0
And the remainder of floor division by 5 is equal to 4.0

So, 
val = 4.0 (which is a float)
'''

# Q6
'''
First; 
tmp = float(-17 // 5)
-17 // 5 = -4
float(-17 // 5) = -4.0

Then; 

val = tmp * 2 ** 2
tmp*2 = -8.0


So, 
val = 64.0

tmp = float(-17 // 5)
val = tmp * 2 ** 2
print(val)
'''

# Q7
temp = float(input("Please enter you body temperature: "))
print("Normal: " + str(98.1 <= temp <= 99.1))

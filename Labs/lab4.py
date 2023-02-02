'''
Julian Patterson 2131249
420-LCU Computer Programming Lab 4
S. Hilal, instructor
'''

# Q1
'''
score = int(input("Please enter a numeric grade: "))

if score >= 93:
    print("Your numeric grade is " + str(score) + " and your letter grade is A")

elif score >= 84:
    print("Your numeric grade is " + str(score) + " and your letter grade is B")

elif score >= 75:
    print("Your numeric grade is " + str(score) + " and your letter grade is C")

elif score >= 60:
    print("Your numeric grade is " + str(score) + " and your letter grade is D")

else:
    print("Your numeric grade is " + str(score) + " and your letter grade is F")
'''

# Q2
'''
The difference between program 1 and 2 is quite important.

In program 1, the program will check the temperature, and since the first condition is met, it stop.
In other words, if/elif/else all work "together", if one condition is met than the rest do not matter.
This will result in printing of "too hot"

In program 2, the program will check the temperature, the first if condition will be met, however, so does the second condition.
In other words, each if statement needs to checked, they do not work "together"
This will result in printing of "too hot" and "just right"
'''


# Q3
'''
total = 0
message = "Please enter an integer (or 0 to exit): "
user_input = int(input(message))

while user_input != 0:
    user_input = int(input(message))
    if (user_input % 5) == 0:
        total += user_input
    else:
        continue

print("Total = " + str(total))
'''
# needs to be fixed - adding doesn't work


# Q4
'''
z = int(input("Enter a number z between 3 and 6: "))
product = 1
counter = 1

while counter <= z:
    product *= (counter ** 3)
    counter += 1

print("The product of cubes for z = " + str(z) + " is " + str(product))
'''
# The product had to be initialized because in the while loop we could not assign the product
# If we were to assign the product in the while then we would be constantly be reassigning it and it would not longer have the desired value
# Furthermore, we needed to use the "+=" operation which can only be used when a variable is already assigned
# Finally, the product of 1 ^ 3 is equal to 1 so there will not be any difference in the final product computation


# Q5


import random
secret = random.randrange(1, 100)
print(secret)
guesses = 0
selection = int(input(
    "Gamemodes: \n 1. Guess up to 10 times \n 2. Keep guessing until the user figures it out \nPlease select a gamemode 1 or 2: "))

if selection == 1:
    while guesses <= 9:
        user_guess = int(input("Guess a random number: "))
        if user_guess < secret:
            print("Your guess was too low. Try again. ")
            guesses += 1
        if user_guess > secret:
            print("Your guess was too high. Try again. ")
            guesses += 1
        if user_guess == secret:
            print("Your guess is right. Congratulations. It only took " +
                  str(guesses) + " tries. ")
            print("Thank you for playing and have nice day. ")
            break
    if guesses > 9:
        print("Thank you for playing!")
        print("You have exceeded the number of guesses")

if selection == 2:
    user_guess = int(input("Guess a random number: "))
    while user_guess != secret:
        user_guess = int(input("Guess a random number: "))
        if user_guess < secret:
            print("Your guess was too low. Try again. ")
            guesses += 1
        if user_guess > secret:
            print("Your guess was too high. Try again. ")
            guesses += 1

    print("Your guess is right. Congratulations. It only took " +
          str(guesses) + " tries. ")
    print("Thank you for playing and have nice day. ")

'''
else:
    print("Please select the correct gamemode; 1 or 2")
    selection = int(input(
        "Gamemodes: \n 1. Guess up to 10 times \n 2. Keep guessing until the user figures it out \nPlease select a gamemode 1 or 2: "))
'''

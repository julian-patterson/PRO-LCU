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
replace_u = full_name.replace("u", "-")
replace_i = replace_u.replace("i", "-")
replace_a = replace_i.replace("a", "-")
replace_a2 = replace_a.replace("a", "-")
replace_e = replace_a2.replace("e", "-")
replace_o = replace_e.replace("o", "-")
print(replace_o)

# Q6
print(full_name[0].lower() + full_name[1:].upper())

# Q7
header = "From jsmith@gmail.com Wed Feb 03 9:32:39 2021 \n"
print(header[header.find("@"): header.find(" ", header.find("@"))])


# Part 4
print("""
Please enter a password following this citeria:
    1. Composed of letters and digits only
    2. Minimum length of 8 characters and maximum length of 15 characters
    3. Must start with a capital letter
    4. Must end with 4 digits
    5. At least 1 small letter
""")
usr_password = input("Enter a password: ")
password_success = False

while password_success == False:
    if 8 <= len(usr_password) <= 15:
        if usr_password.isalnum() == True:
            if usr_password[0].isupper() == True:
                if usr_password[-4:].isdigit() == True:
                    if usr_password.isupper() == False:  # if this is true then all alphabetic characters are uppercase
                        password_success = True
                        break
                    else:
                        print(
                            "Password incorrect; password must have at least one lower case character")
                        break
                else:
                    print("Password incorrect; last four characters must be a digit")
                    break
            else:
                print("Password incorrect; first letter must be capitalized")
                break
        else:
            print("Password incorrect; must be only alphanumeric")
            break
    else:
        print("Password incorrect; must be between [8: 15] characters")
        break
if password_success == True:
    print("Password accepted!")

# Q3
check_number = input("Please enter card number: ")
list_check_number = list(check_number)
total = 0
int_check_number = []
check = None

while True:
    for i in list_check_number:
        if i.isdigit():
            int_check_number.append(int(i))
        else:
            check = False
            break
    if len(check_number) == 16:
        check = True
        for i in int_check_number:
            if i <= 9:
                check = True
            else:
                check = False
                break
        for i in int_check_number:
            total += i
        if total % 2 == 0:
            check = True
            break
        else:
            check = False
            break
    else:
        check = False
        break

print(check)


# Q4
text = input("Input your text: ")
total = 0
split_text = text.split()
for i in split_text:
    if (i[0].isupper()):
        total += 1
    else:
        continue
print(total)


# Q5
numbers = input("Enter numbers seperated by a comma: ")
split_numbers = numbers.split(",")
list_number = []
string_sorted_numbers = []
for i in split_numbers:
    list_number.append(int(i))
sorted_numbers = sorted(list_number)
for i in sorted_numbers:
    string_sorted_numbers.append(str(i))
print(",".join(string_sorted_numbers))

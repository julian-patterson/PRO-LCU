'''
Julian Patterson 2131249
420-LCU Computer Programming
Friday February 17, 2023
S. Hilal, instructor
Assignment 1
'''

# Plan A Constants:
A_SALARY = 735      # Plan_A base weekly salry for plan A, in dollars
A_HOURS = 35        # Plan_A # of base working hours per week
A_OVERTIME = 30     # Plan_A pay for each overtime hour, in dollars
A_EVENING = 10      # Plan_A additional pay per evening hour, in dollars
A_WEEKEND = 15      # Plan_A additional pay per weekend hour, in dollars

# Plan B Constants:
B_SALARY = 885      # Plan_B base weekly salry for plan A, in dollars
B_HOURS = 40        # Plan_B # of base working hours per week
B_OVERTIME = 30     # Plan_B pay for each overtime hour, in dollars
B_EVENING = 12      # Plan_B additional pay per evening hour, in dollars
B_WEEKEND = 14      # Plan_B additional pay per weekend hour, in dollars

# Plan C Constants:
C_SALARY = 962      # Plan_C base weekly salry for plan A, in dollars
C_HOURS = 43        # Plan_C # of base working hours per week
C_OVERTIME = 30     # Plan_C pay for each overtime hour, in dollars
C_EVENING = 14      # Plan_C additional pay per evening hour, in dollars
C_WEEKEND = 13      # Plan_C additional pay per weekend hour, in dollars

# Menu
MENU = """
Welcome to the "Best Salary Plan" Calculator
    1. Enter Employee name and hours worked
    2. Determine the Best Salary Plan base on hours worked
    3. Exit
Enter your selected option: """

# Setting overtime hours by default to 0; is checked later on in program
a_overtime_hours = 0
b_overtime_hours = 0
c_overtime_hours = 0

while True:
    selection = input(MENU)

    if selection == "1":
        # Asking for user input
        user_name = input("Enter your name: ")
        regular_hours = int(
            input("Enter total number of hours worked per week: "))
        evening_hours = int(input("Enter number of evening hours: "))
        weekend_hours = int(input("Enter number of weekend hours: "))

    elif selection == "2":
        # Checking to see if user did any overtime and calculating totals in plans A,B, or C
        if regular_hours > A_HOURS:
            a_overtime_hours = regular_hours - A_HOURS
        a_total = A_SALARY + a_overtime_hours*A_OVERTIME + \
            evening_hours*A_EVENING + weekend_hours*A_WEEKEND

        if regular_hours > B_HOURS:
            b_overtime_hours = regular_hours - B_HOURS
        b_total = B_SALARY + b_overtime_hours*B_OVERTIME + \
            evening_hours*B_EVENING + weekend_hours*B_WEEKEND

        if regular_hours > C_HOURS:
            c_overtime_hours = regular_hours - C_HOURS
        c_total = C_SALARY + c_overtime_hours*C_OVERTIME + \
            evening_hours*C_EVENING + weekend_hours*C_WEEKEND

        # Printing totals
        print("Plan A gross weekly salary is: $" + str(a_total))
        print("Plan B gross weekly salary is: $" + str(b_total))
        print("Plan C gross weekly salary is: $" + str(c_total))

        # Checking which total is greater and printing recommendation
        if a_total >= b_total > c_total:
            print(user_name + " , you should choose plan A")

        elif a_total >= c_total > b_total:
            print(user_name + " , you should choose plan A")

        elif b_total >= c_total > a_total:
            print(user_name + " , you should choose plan B")

        elif b_total > a_total > c_total:
            print(user_name + " , you should choose plan B")

        elif c_total > b_total > a_total:
            print(user_name + " , you should choose plan C")

        elif c_total > a_total > b_total:
            print(user_name + " , you should choose plan C")

    elif selection == "3":
        print("Thanks for using the Best Salary Plan Calculator. Exiting....")
        break

    else:
        print("Invalid option. Please choose a valid option. ")

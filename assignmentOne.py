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

while True:
    menu_selection = input("""Welcome to the "Best Salary Plan" Calculator
        1. Enter Employee name and hours worked
        2. Determine the Best Salary Plan base on hours worked
        3. Exit
        Enter your selected option: """)
    if menu_selection == 1:
        user_name = input("Enter your name: ")
        regular_hours = input("Enter total number of hours worked per week: ")
        evening_hours = input("Enter number of evening hours: ")
        weekend_hours = input("Enter number of weekend hours: ")
        break
    if menu_selection == 2:
        print("congrats")

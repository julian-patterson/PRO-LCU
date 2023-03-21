'''
Julian Patterson 2131249
420-LCU Computer Programming, Section 5
S. Hilal, instructor
Assignment 2
'''


# Data tables and totals for calculations
Names = []              # names
IDs = []                # students' IDs
Prog = []               # program codes
Tests = []              # Test grades (2 grades/student)
Labs = []               # Lab grades (3 grades/student)
Proj = []               # Project grades
Grds = []               # Total grades
LGrds = []              # letter grades
Data = []               # Overall Data
TestList = []           # List of all tests
LabList = []            # List of all labs
ProjectList = []        # list of all projects
Test1 = []              # List of all test 1
Test2 = []              # List of all test 2
Lab1 = []               # List of all lab 1
Lab2 = []               # List of all lab 2
Lab3 = []               # List of all lab 3
lab_score_total = 0     # Total of all the lab scores
test_score_total = 0    # Total of all the test scores


# Program Menu:
MENU = '''\nWelcome to the Simple Class Calculator. Here's the list of available:
    1- Enter a student record (Name, ID, Program, and 6 grades seperated by commas, no spaces).
    2- Display the full class data in a table format sorted in alphabetical order based on full name.
    3- Calculate and Display the class descriptive statistics.
    4- Display the record of a given student. 
    5- Display a list of the students whose total grade is below the average.
    6- Update an evaluation grade for one student.
    7- Exit
Select an option by entering its number or 7 to exit: '''


# Function for checking (over range and digit) the scores of tests, labs and projects
def score_check(list, type):
    if type == "test":
        for i in list:
            if str(i).isdigit():
                if i <= 25:
                    test_score_total += int(i)
                    TestList.append(int(i))
                    Test1.append(int(i[0]))
                    Test2.append(int(i[1]))
                    return True, test_score_total, TestList, Test1, Test2
                else:
                    return print("Record Rejected. Test score must be below 25"), False
            else:
                return print("Record Rejected. Test score must be a digit"), False

    if type == "lab":
        for i in list:
            if str(i).isdigit():
                if i <= 10:
                    lab_score_total += int(i)
                    LabList.append(int(i))
                    Lab1.append(i[0])
                    Lab2.append(i[1])
                    Lab3.append(i[2])
                    return True, lab_score_total, LabList
                else:
                    return print("Record Rejected. Lab score must be below 10"), False
            else:
                return print("Record Rejected. Lab score must be a digit"), False

    if type == "project":
        for i in list:
            if str(i).isdigit():
                if i <= 20:
                    project_score_total += int(i)
                    ProjectList.append(int(i))
                    return True, project_score_total, ProjectList
                else:
                    return print("Record Rejected. Project score must be below 10"), False
            else:
                return print("Record Rejected. Project score must be a digit"), False


# Function for calculating average
def average(list):
    return sum(list)/len(list)


# Main program and menu selection
while True:
    selection = input(MENU)
    if selection == "1":
        temp_student_record = input("Enter Student Record: ")
        record = temp_student_record.split(",")

        if len(record) == 9:
            temp_name = record[0].replace(" ", "")
            if temp_name.isalpha():
                if record[1].isdigit():
                    if len(record[1]) == 6:
                        for id in IDs:
                            if int(id) != int(record[1]):
                                if record[2] == "HH" or "HP" or "B2":
                                    if score_check(record[3:5], "test"):
                                        if score_check(record[5:8], "lab"):
                                            if score_check(record[-1], "project"):
                                                print("Record Accepted. ")
                                                overall_grade = (((int(record[-1])/20*0.2) + (
                                                    lab_score_total/30*.30) + (test_score_total/50*0.5))*100)

                                                if int(overall_grade) >= 87:
                                                    letter_grade = "A"

                                                elif 75 <= int(overall_grade) <= 86:
                                                    letter_grade = "B"

                                                elif 65 <= int(overall_grade) <= 74:
                                                    letter_grade = "C"

                                                else:
                                                    letter_grade = "F"

                                                Data.append(record[0], int(record[1]), record[2], TestList, LabList, int(
                                                    record[-1]), int(overall_grade), letter_grade)
                                                Names.append(record[0])
                                                IDs.append(int(record[1]))
                                                Prog.append(record[2])
                                                Tests.append(TestList)
                                                Labs.append(LabList)
                                                Proj.append(record[-1])
                                                Grds.append(int(overall_grade))
                                                LGrds.append(
                                                    str(overall_grade))
                                                break

                                else:
                                    print(
                                        "Invalid program ented. Please enter HH, HP, or B2")
                                    break
                            else:
                                print("ID is duplicated. Record Rejected. ")
                                break
                    else:
                        print("ID must be 6 digits. Record Rejected. ")
                        break
                else:
                    print("ID must be an integer. Record Rejected")
                    break
            else:
                print("Name must be a string. Record Rejected. ")
                break
        else:
            print("Record must contain 9 items. Record Rejected. ")
            break

    elif selection == "2":
        Data.sort()
        x = "{:12s} {:6d} {:3s} {:8s} {:12s} {:3d} {:3d} {:1s}"
        for i in Data:
            print(x.format(i[0], i[1], i[2], i[3],
                  i[4], i[5], i[6], i[7]))

    elif selection == "3":
        print("Number of students entered: " + str(len(Names)))

        print("Class average based on total grade: " + str(average(Grds)))

        mode = []
        A_count = LGrds.count("A")
        mode.append([A_count, "A"])

        B_count = LGrds.count("B")
        mode.append([B_count, "B"])

        C_count = LGrds.count("C")
        mode.append([C_count, "C"])

        F_count = LGrds.count("F")
        mode.append([F_count, "F"])

        mode.sort()
        for i in mode:
            previous_count = int(i[0])
            previous_letter = i[1]
            if int(i[0]) < previous_count:
                print("The class mode is " + str(i[1]))
                break
            elif int(i[0]) == previous_count:
                print("The class mode is " +
                      str(i[1]) + " and " + str(previous_letter))

        print("Evaluation Averages: T1: " + str(float(average(Test1))*100/25)) + " T2: " + str(float(average(Test2)*100/25)) + " L1: " + str(float(average(Lab1) *
                                                                                                                                                   100/10)) + " L2: " + str(float((average(Lab2)*100/10)) + " L3: " + str(float(average(Lab3)*100/10)) + " Proj: " + str(float(average(ProjectList)*100/20)))

        print("Letter Grade distribution: A: " + str(LGrds.count("A")) + " B: " +
              str(LGrds.count("B")) + " C: " + str(LGrds.count("C")) + " F: " + str(LGrds.count("F")))

        print("Highest Grade for T1: " + str(max(Test1)*100/25) + " Lowest Grade for T1: " + str(min(Test1)*100/25) +
              " Highest Grade for T2: " + str(max(Test2)*100/25) + " Lowest Grade for T2: " + str(min(Test2)*100/25))

    elif selection == "4":
        id_input = input("Enter the student's ID: ")
        for record in Data:
            if record[1] == int(id_input):
                print("Name: " + str(record[0]) + "    ID: " + str(record[1]))
                print("Test Grades: " + str(record[3]).strip(" []") + " Lab Grades: " + str(
                    record[4]).strip(" []") + " Project Grade: " + str(record[5]))
                print("Total Grade: " +
                      str(record[6]) + "     Letter Grade: " + str(record[7]))

    elif selection == "5":
        overall_class_average = average(Grds)
        for i in Data:
            if i[6] <= overall_class_average:
                print(i[0])
            else:
                continue

    elif selection == "6":
        id_input = input("Enter the student's ID: ")
        grade_input = input("Which grade to update: ")
        for record in Data:
            if record[1] == int(id_input):
                if grade_input == "T1":
                    for i in record[3]:
                        print("The current T1 grade is " + str(i[0]))
                        update = input("Enter the new T1 grade: ")
                        i[0] = int(update)
                elif grade_input == "T2":
                    for i in record[3]:
                        print("The current T2 grade is " + str(i[1]))
                        update = input("Enter the new T2 grade: ")
                        i[1] = int(update)
                elif grade_input == "L1":
                    for i in record[4]:
                        print("The current L1 grade is " + str(i[0]))
                        update = input("Enter the new L1 grade: ")
                        i[0] = int(update)
                elif grade_input == "L2":
                    for i in record[4]:
                        print("The current L2 grade is " + str(i[1]))
                        update = input("Enter the new L2 grade: ")
                        i[1] = int(update)
                elif grade_input == "L3":
                    for i in record[4]:
                        print("The current L3 grade is " + str(i[2]))
                        update = input("Enter the new L3 grade: ")
                        i[2] = int(update)
                else:
                    print("The current PR grade is " + str(record[5]))
                    update = input("Enter the new PR grade: ")
                    record[5] = int(update)

    elif selection == "7":
        break

    else:
        print("Please enter a valid option. Please select a number between 1 and 7")
